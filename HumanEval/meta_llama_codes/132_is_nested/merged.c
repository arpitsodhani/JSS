#include <stdio.h>
#include <string.h>

int main() {
    char s[1000];
    int d = 0, m = 0, balanced = 1;
    fgets(s, 1000, stdin);
    for (int i = 0; s[i] && s[i] != '\n'; i++) {
        d += (s[i] == '[') - (s[i] == ']');
        if (d < 0) balanced = 0;
        if (d > m) m = d;
    }
    if (d != 0) balanced = 0;
    printf("%s\n", (m >= 2 && balanced) ? "True" : "False");
    return 0;
}
