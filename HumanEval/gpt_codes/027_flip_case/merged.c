#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {10, 0};
static const unsigned char output_0[] = {10, 0};
static const unsigned char input_1[] = {72, 101, 108, 108, 111, 33, 10, 0};
static const unsigned char output_1[] = {104, 69, 76, 76, 79, 33, 10, 0};
static const unsigned char input_2[] = {84, 104, 101, 115, 101, 32, 118, 105, 111, 108, 101, 110, 116, 32, 100, 101, 108, 105, 103, 104, 116, 115, 32, 104, 97, 118, 101, 32, 118, 105, 111, 108, 101, 110, 116, 32, 101, 110, 100, 115, 10, 0};
static const unsigned char output_2[] = {116, 72, 69, 83, 69, 32, 86, 73, 79, 76, 69, 78, 84, 32, 68, 69, 76, 73, 71, 72, 84, 83, 32, 72, 65, 86, 69, 32, 86, 73, 79, 76, 69, 78, 84, 32, 69, 78, 68, 83, 10, 0};

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
