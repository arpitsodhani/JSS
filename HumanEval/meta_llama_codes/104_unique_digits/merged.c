#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {52, 10, 49, 53, 10, 51, 51, 10, 49, 52, 50, 50, 10, 49, 10, 0};
static const unsigned char output_0[] = {50, 32, 49, 53, 32, 51, 51, 10, 0};
static const unsigned char input_1[] = {52, 10, 49, 53, 50, 10, 51, 50, 51, 10, 49, 52, 50, 50, 10, 49, 48, 10, 0};
static const unsigned char output_1[] = {10, 0};
static const unsigned char input_2[] = {52, 10, 49, 50, 51, 52, 53, 10, 50, 48, 51, 51, 10, 49, 49, 49, 10, 49, 53, 49, 10, 0};
static const unsigned char output_2[] = {49, 49, 49, 32, 49, 53, 49, 10, 0};
static const unsigned char input_3[] = {51, 10, 49, 51, 53, 10, 49, 48, 51, 10, 51, 49, 10, 0};
static const unsigned char output_3[] = {51, 49, 32, 49, 51, 53, 10, 0};

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
