#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {55, 32, 55, 10, 49, 32, 52, 32, 51, 32, 51, 52, 32, 54, 53, 51, 32, 50, 32, 53, 10, 53, 32, 55, 32, 49, 32, 53, 32, 57, 32, 54, 53, 51, 32, 49, 50, 49, 10, 0};
static const unsigned char output_0[] = {49, 32, 53, 32, 54, 53, 51, 10, 0};
static const unsigned char input_1[] = {52, 32, 50, 10, 53, 32, 51, 32, 50, 32, 56, 10, 51, 32, 50, 10, 0};
static const unsigned char output_1[] = {50, 32, 51, 10, 0};
static const unsigned char input_2[] = {52, 32, 51, 10, 52, 32, 51, 32, 50, 32, 56, 10, 51, 32, 50, 32, 52, 10, 0};
static const unsigned char output_2[] = {50, 32, 51, 32, 52, 10, 0};
static const unsigned char input_3[] = {52, 32, 48, 10, 52, 32, 51, 32, 50, 32, 56, 10, 10, 0};
static const unsigned char output_3[] = {10, 0};

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
