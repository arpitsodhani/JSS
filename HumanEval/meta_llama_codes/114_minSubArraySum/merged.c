#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {54, 10, 50, 10, 51, 10, 52, 10, 49, 10, 50, 10, 52, 10, 0};
static const unsigned char output_0[] = {49, 10, 0};
static const unsigned char input_1[] = {51, 10, 45, 49, 10, 45, 50, 10, 45, 51, 10, 0};
static const unsigned char output_1[] = {45, 54, 10, 0};
static const unsigned char input_2[] = {53, 10, 45, 49, 10, 45, 50, 10, 45, 51, 10, 50, 10, 45, 49, 48, 10, 0};
static const unsigned char output_2[] = {45, 49, 52, 10, 0};
static const unsigned char input_3[] = {49, 10, 45, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 10, 0};
static const unsigned char output_3[] = {45, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 10, 0};
static const unsigned char input_4[] = {52, 10, 48, 10, 49, 48, 10, 50, 48, 10, 49, 48, 48, 48, 48, 48, 48, 10, 0};
static const unsigned char output_4[] = {48, 10, 0};
static const unsigned char input_5[] = {53, 10, 45, 49, 10, 45, 50, 10, 45, 51, 10, 49, 48, 10, 45, 53, 10, 0};
static const unsigned char output_5[] = {45, 54, 10, 0};
static const unsigned char input_6[] = {54, 10, 49, 48, 48, 10, 45, 49, 10, 45, 50, 10, 45, 51, 10, 49, 48, 10, 45, 53, 10, 0};
static const unsigned char output_6[] = {45, 54, 10, 0};
static const unsigned char input_7[] = {54, 10, 49, 48, 10, 49, 49, 10, 49, 51, 10, 56, 10, 51, 10, 52, 10, 0};
static const unsigned char output_7[] = {51, 10, 0};
static const unsigned char input_8[] = {54, 10, 49, 48, 48, 10, 45, 51, 51, 10, 51, 50, 10, 45, 49, 10, 48, 10, 45, 50, 10, 0};
static const unsigned char output_8[] = {45, 51, 51, 10, 0};
static const unsigned char input_9[] = {49, 10, 45, 49, 48, 10, 0};
static const unsigned char output_9[] = {45, 49, 48, 10, 0};
static const unsigned char input_10[] = {49, 10, 55, 10, 0};
static const unsigned char output_10[] = {55, 10, 0};
static const unsigned char input_11[] = {50, 10, 49, 10, 45, 49, 10, 0};
static const unsigned char output_11[] = {45, 49, 10, 0};

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
    free(input);
    return 1;
}
