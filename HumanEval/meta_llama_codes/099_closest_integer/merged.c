#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    char text[128];
    if (scanf("%127s", text) != 1) return 1;
    size_t len = strlen(text);
    if (len >= 2 && text[0] == '"' && text[len - 1] == '"') text[len - 1] = '\0';
    char *number = text[0] == '"' ? text + 1 : text;
    double value = strtod(number, NULL);
    long long whole = (long long)value;
    double fraction = value >= 0 ? value - whole : whole - value;
    if (fraction >= 0.5) whole += value >= 0 ? 1 : -1;
    printf("%lld\n", whole);
    return 0;
}
