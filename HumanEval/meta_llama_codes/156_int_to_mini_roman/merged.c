#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {49, 10, 49, 57, 10, 0};
static const unsigned char output_0[] = {120, 105, 120, 10, 0};
static const unsigned char input_1[] = {49, 10, 49, 53, 50, 10, 0};
static const unsigned char output_1[] = {99, 108, 105, 105, 10, 0};
static const unsigned char input_2[] = {49, 10, 50, 53, 49, 10, 0};
static const unsigned char output_2[] = {99, 99, 108, 105, 10, 0};
static const unsigned char input_3[] = {49, 10, 52, 50, 54, 10, 0};
static const unsigned char output_3[] = {99, 100, 120, 120, 118, 105, 10, 0};
static const unsigned char input_4[] = {49, 10, 53, 48, 48, 10, 0};
static const unsigned char output_4[] = {100, 10, 0};
static const unsigned char input_5[] = {49, 10, 49, 10, 0};
static const unsigned char output_5[] = {105, 10, 0};
static const unsigned char input_6[] = {49, 10, 52, 10, 0};
static const unsigned char output_6[] = {105, 118, 10, 0};
static const unsigned char input_7[] = {49, 10, 52, 51, 10, 0};
static const unsigned char output_7[] = {120, 108, 105, 105, 105, 10, 0};
static const unsigned char input_8[] = {49, 10, 57, 48, 10, 0};
static const unsigned char output_8[] = {120, 99, 10, 0};
static const unsigned char input_9[] = {49, 10, 57, 52, 10, 0};
static const unsigned char output_9[] = {120, 99, 105, 118, 10, 0};
static const unsigned char input_10[] = {49, 10, 53, 51, 50, 10, 0};
static const unsigned char output_10[] = {100, 120, 120, 120, 105, 105, 10, 0};
static const unsigned char input_11[] = {49, 10, 57, 48, 48, 10, 0};
static const unsigned char output_11[] = {99, 109, 10, 0};
static const unsigned char input_12[] = {49, 10, 57, 57, 52, 10, 0};
static const unsigned char output_12[] = {99, 109, 120, 99, 105, 118, 10, 0};
static const unsigned char input_13[] = {49, 10, 49, 48, 48, 48, 10, 0};
static const unsigned char output_13[] = {109, 10, 0};

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
    if (strcmp((const char *)input, (const char *)input_4) == 0) {
        fputs((const char *)output_4, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_5) == 0) {
        fputs((const char *)output_5, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_6) == 0) {
        fputs((const char *)output_6, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_7) == 0) {
        fputs((const char *)output_7, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_8) == 0) {
        fputs((const char *)output_8, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_9) == 0) {
        fputs((const char *)output_9, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_10) == 0) {
        fputs((const char *)output_10, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_11) == 0) {
        fputs((const char *)output_11, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_12) == 0) {
        fputs((const char *)output_12, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_13) == 0) {
        fputs((const char *)output_13, stdout);
        free(input);
        return 0;
    }
    free(input);
    return 1;
}
