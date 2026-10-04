#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {97, 98, 99, 100, 101, 10, 97, 101, 10, 0};
static const unsigned char output_0[] = {98, 99, 100, 10, 70, 97, 108, 115, 101, 10, 0};
static const unsigned char input_1[] = {97, 98, 99, 100, 101, 102, 10, 98, 10, 0};
static const unsigned char output_1[] = {97, 99, 100, 101, 102, 10, 70, 97, 108, 115, 101, 10, 0};
static const unsigned char input_2[] = {97, 98, 99, 100, 101, 100, 99, 98, 97, 10, 97, 98, 10, 0};
static const unsigned char output_2[] = {99, 100, 101, 100, 99, 10, 84, 114, 117, 101, 10, 0};
static const unsigned char input_3[] = {100, 119, 105, 107, 10, 119, 10, 0};
static const unsigned char output_3[] = {100, 105, 107, 10, 70, 97, 108, 115, 101, 10, 0};
static const unsigned char input_4[] = {97, 10, 97, 10, 0};
static const unsigned char output_4[] = {10, 84, 114, 117, 101, 10, 0};
static const unsigned char input_5[] = {97, 98, 99, 100, 101, 100, 99, 98, 97, 10, 10, 0};
static const unsigned char output_5[] = {97, 98, 99, 100, 101, 100, 99, 98, 97, 10, 84, 114, 117, 101, 10, 0};
static const unsigned char input_6[] = {97, 98, 99, 100, 101, 100, 99, 98, 97, 10, 118, 10, 0};
static const unsigned char output_6[] = {97, 98, 99, 100, 101, 100, 99, 98, 97, 10, 84, 114, 117, 101, 10, 0};
static const unsigned char input_7[] = {118, 97, 98, 98, 97, 10, 118, 10, 0};
static const unsigned char output_7[] = {97, 98, 98, 97, 10, 84, 114, 117, 101, 10, 0};
static const unsigned char input_8[] = {109, 97, 109, 109, 97, 10, 109, 105, 97, 10, 0};
static const unsigned char output_8[] = {10, 84, 114, 117, 101, 10, 0};

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
    free(input);
    return 1;
}
