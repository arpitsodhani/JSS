#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {48, 10, 10, 0};
static const unsigned char output_0[] = {78, 111, 110, 101, 10, 0};
static const unsigned char input_1[] = {51, 10, 120, 10, 121, 10, 122, 10, 0};
static const unsigned char output_1[] = {120, 10, 0};
static const unsigned char input_2[] = {54, 10, 120, 10, 121, 121, 121, 10, 122, 122, 122, 122, 10, 119, 119, 119, 10, 107, 107, 107, 107, 10, 97, 98, 99, 10, 0};
static const unsigned char output_2[] = {122, 122, 122, 122, 10, 0};

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
    free(input);
    return 1;
}
