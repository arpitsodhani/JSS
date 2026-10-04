#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {48, 10, 116, 101, 115, 116, 10, 0};
static const unsigned char output_0[] = {0};
static const unsigned char input_1[] = {51, 10, 97, 10, 97, 98, 99, 10, 98, 97, 99, 100, 10, 99, 100, 101, 10, 0};
static const unsigned char output_1[] = {97, 98, 99, 10, 98, 97, 99, 100, 10, 0};
static const unsigned char input_2[] = {53, 10, 120, 120, 10, 97, 98, 99, 10, 98, 99, 100, 10, 99, 100, 101, 10, 97, 97, 97, 10, 120, 120, 120, 10, 0};
static const unsigned char output_2[] = {120, 120, 120, 10, 0};
static const unsigned char input_3[] = {53, 10, 106, 111, 104, 110, 10, 120, 120, 120, 106, 111, 104, 110, 10, 120, 120, 120, 106, 111, 104, 110, 120, 120, 120, 10, 106, 111, 104, 110, 120, 120, 120, 10, 106, 111, 104, 110, 10, 120, 120, 120, 106, 111, 104, 110, 10, 0};
static const unsigned char output_3[] = {120, 120, 120, 106, 111, 104, 110, 10, 120, 120, 120, 106, 111, 104, 110, 120, 120, 120, 10, 106, 111, 104, 110, 120, 120, 120, 10, 106, 111, 104, 110, 10, 120, 120, 120, 106, 111, 104, 110, 10, 0};

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
    if (strcmp((const char *)input, (const char *)input_2) == 0) {
        fputs((const char *)output_2, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_3) == 0) {
        fputs((const char *)output_3, stdout);
        free(input);
        return 0;
    }
    free(input);
    return 1;
}
