

int main() {
    run();
    return 0;
}

void run(void) {

    int n, sum=0; scanf("%d", &n);
    for(int i=0; i<n; i++) {
        int x; scanf("%d", &x);
        if(i%3==0) sum+=x*x;
        else if(i%4==0) sum+=x*x*x;
        else sum+=x;
    }
    printf("%d\\n", sum);
}
