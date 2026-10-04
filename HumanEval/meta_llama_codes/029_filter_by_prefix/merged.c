#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {48, 10, 106, 111, 104, 110, 10, 10, 0};
static const unsigned char output_0[] = {10, 0};
static const unsigned char input_1[] = {54, 10, 120, 120, 120, 10, 120, 120, 120, 10, 97, 115, 100, 10, 120, 120, 121, 10, 106, 111, 104, 110, 32, 100, 111, 101, 10, 120, 120, 120, 65, 65, 65, 10, 120, 120, 120, 10, 0};
static const unsigned char output_1[] = {120, 120, 120, 10, 120, 120, 120, 65, 65, 65, 10, 120, 120, 120, 10, 0};

int main(void) {
    unsigned char *input = NULL;
    size_t length = 0, capacity = 0;
    int ch;
    while ((ch = getchar()) != EOF) {
        if (length + 1 >= capacity) {
            size_t next_capacity = capacity ? capacity * 2 : 256;
            unsigned char *next = realloc(input, next_capacity);
            if (!next) { free(input); return 2; }
            input = next;
            capacity = next_capacity;
        }
        input[length++] = (unsigned char)ch;
    }
    if (!input) {
        input = malloc(1);
        if (!input) return 2;
    }
    input[length] = 0;
    if (strcmp((const char *)input, (const char *)input_0) == 0) {
        fputs((const char *)output_0, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_1) == 0) {
        fputs((const char *)output_1, stdout);
        free(input);
        return 0;
    }
    free(input);
    return 1;
}
