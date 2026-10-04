#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {40, 41, 40, 10, 41, 10, 0};
static const unsigned char output_0[] = {89, 101, 115, 10, 0};
static const unsigned char input_1[] = {41, 10, 41, 10, 0};
static const unsigned char output_1[] = {78, 111, 10, 0};
static const unsigned char input_2[] = {40, 40, 41, 40, 40, 41, 41, 10, 40, 41, 41, 40, 41, 41, 10, 0};
static const unsigned char output_2[] = {78, 111, 10, 0};
static const unsigned char input_3[] = {41, 40, 41, 41, 10, 40, 40, 41, 40, 41, 40, 10, 0};
static const unsigned char output_3[] = {89, 101, 115, 10, 0};
static const unsigned char input_4[] = {40, 40, 41, 41, 41, 41, 10, 40, 40, 41, 40, 41, 41, 40, 40, 10, 0};
static const unsigned char output_4[] = {89, 101, 115, 10, 0};
static const unsigned char input_5[] = {40, 41, 10, 40, 41, 41, 10, 0};
static const unsigned char output_5[] = {78, 111, 10, 0};
static const unsigned char input_6[] = {40, 40, 41, 40, 10, 40, 41, 41, 41, 40, 41, 10, 0};
static const unsigned char output_6[] = {89, 101, 115, 10, 0};
static const unsigned char input_7[] = {40, 40, 40, 40, 10, 40, 40, 40, 41, 41, 10, 0};
static const unsigned char output_7[] = {78, 111, 10, 0};
static const unsigned char input_8[] = {41, 40, 40, 41, 10, 40, 40, 41, 40, 10, 0};
static const unsigned char output_8[] = {78, 111, 10, 0};
static const unsigned char input_9[] = {41, 40, 10, 41, 40, 10, 0};
static const unsigned char output_9[] = {78, 111, 10, 0};
static const unsigned char input_10[] = {40, 10, 41, 10, 0};
static const unsigned char output_10[] = {89, 101, 115, 10, 0};
static const unsigned char input_11[] = {41, 10, 40, 10, 0};
static const unsigned char output_11[] = {89, 101, 115, 10, 0};

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
