#include <stdio.h>
#include <string.h>

int count_hex_primes(char *s) {
    char primes[] = "2357BD";
    int count = 0;
    for (int i = 0; s[i]; i++) {
        for (int j = 0; primes[j]; j++) {
            if (toupper(s[i]) == primes[j]) {
                count++;
                break;
            }
        }
    }
    return count;
}

int main(void) {
    char s[1000];
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;
    int result = count_hex_primes(s);
    printf("%d\n", result);
    return 0;
}
