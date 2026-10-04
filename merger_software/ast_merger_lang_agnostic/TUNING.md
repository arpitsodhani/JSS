# Similarity / clustering tuning

Changes to the clause-similarity metric, its fallbacks, and the clustering
threshold. Originals are preserved in `_backup_pre_tuning/`.

Calibrate or re-tune with:

```bash
.venv/bin/python tools/calibrate_merger_similarity.py
```

It builds labelled pairs from `ast_merger_sonent_sols` — **positives** are two
variants of the same clause of the same problem (must cluster), **negatives**
are clauses from different problems (must not) — and reports recall/FPR per
threshold.

## Why this was needed

Every clause of every merged program reported confidence 1.00. That was not
because the candidates were identical (0 of 33 clause groups collapsed to the
same normalized AST), but because the metric could not tell siblings from
unrelated code: at the hardcoded 0.70 threshold, **30% of unrelated clause
pairs** scored above threshold.

## What changed

### 1. Threshold is configurable and actually used

`Composer.__init__` stored `self.threshold` and `merge_clause` then clustered at
a hardcoded `0.7`, so the configured value never reached the clustering.
The value is now plumbed through, defaults come from the language config
(`cluster_threshold`: 0.60 for Python, 0.62 for C/C++/Java), and
`evaluate_clauses.py` gained a `--threshold` flag.

### 2. Similarity metric

`_fast_similarity` was `0.50*jaccard + 0.35*feature + 0.10*size_ratio +
0.05*depth_ratio`. The Jaccard term was a *set* of depth-3 ancestry paths, which
saturates — unrelated Python clauses share nearly every short path — and the
size/depth ratio terms handed every pair a 0.15 floor. It is now a weighted
blend of multiset Jaccards, with no free floor:

| term | weight | what it captures |
|---|---|---|
| 3-grams of the normalized pre-order node sequence | 0.30 | statement/expression ordering |
| node-kind multiset | 0.45 | construct mix |
| weighted depth-4 ancestry paths | 0.20 | nesting shape |
| size ratio | 0.05 | length agreement |

Weights were grid-searched against the labelled pairs.

### 3. Fallbacks

Every path that cannot produce a trustworthy tree-edit distance now degrades to
the fast blend, which is on the same scale, instead of returning an arbitrary
number:

| situation | before | after |
|---|---|---|
| trees differ a lot in size | `size_ratio * 0.5` | fast blend (pre-filter at `ted_min_size_ratio`) |
| low Jaccard pre-filter | `0.3 * jaccard` | removed; blend is continuous |
| tree over 500 nodes | TED returned `max(size)` → similarity term exactly 0 | raises `TreeTooLargeForTED`, caller falls back to the blend |
| no AST available | raw set Jaccard | fast blend |

The old oversize rule is why any large clause looked maximally dissimilar to
everything, including a copy of itself.

### 4. TED cache correctness

`_ted_cache` was keyed on `id(node)`. CPython recycles ids once an object is
freed, so an entry could be returned for an unrelated tree that reused the
address. It is now keyed on a structural digest of the normalized subtree —
correct regardless of object lifetime, and it also lets identical subtrees from
different programs share cache entries.

### 5. Clustering

Was: seed a cluster with the first unvisited index, absorb every unvisited `j`
with `sim(seed, j) >= threshold`. Members were never compared to each other, and
the outcome depended on the order programs appeared in the input file.

Now: complete linkage — a variant joins only if it is within threshold of *every*
current member — with seeds taken in order of decreasing total similarity.

### 6. Deterministic representative

`_cluster_medoid` broke ties by lowest index, so permuting the input file could
change which variant was emitted. Ties now break on the fingerprint's structural
key and then the clause text. Verified: 40 random permutations across 10
problems produce byte-identical `merged.py`.

### 7. New `agreement` field

`confidence = |largest cluster| / |variants|` is quantised — with 5 variants it
can only be 0.2/0.4/0.6/0.8/1.0. Each clause now also reports `agreement`, the
mean pairwise similarity inside the winning cluster, which is continuous.
`confidence` is unchanged in meaning, so existing consumers still work.

## Result

On the labelled pairs:

| metric | threshold | recall | FPR | Youden J |
|---|---|---|---|---|
| before | 0.70 (hardcoded) | 1.000 | **0.300** | 0.700 |
| before, at its best threshold | 0.84 | 0.952 | 0.062 | 0.889 |
| after | 0.60 (default) | 0.988 | 0.083 | **0.905** |

On the 10 merged programs: 31/33 clauses unanimous (was 33/33), average
confidence 0.988, and agreement spread over 0.700–0.959 instead of a constant
1.0. The two non-unanimous clauses are real structural outliers —
`801B/compute_answer` (one variant returns `y` directly where the others build a
list) and `534B/main` (one variant indexes the tuple instead of unpacking it).
