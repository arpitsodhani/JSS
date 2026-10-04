#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {50, 10, 74, 117, 112, 105, 116, 101, 114, 10, 78, 101, 112, 116, 117, 110, 101, 10, 0};
static const unsigned char output_0[] = {83, 97, 116, 117, 114, 110, 10, 85, 114, 97, 110, 117, 115, 10, 0};
static const unsigned char input_1[] = {50, 10, 69, 97, 114, 116, 104, 10, 77, 101, 114, 99, 117, 114, 121, 10, 0};
static const unsigned char output_1[] = {86, 101, 110, 117, 115, 10, 0};
static const unsigned char input_2[] = {50, 10, 77, 101, 114, 99, 117, 114, 121, 10, 85, 114, 97, 110, 117, 115, 10, 0};
static const unsigned char output_2[] = {86, 101, 110, 117, 115, 10, 69, 97, 114, 116, 104, 10, 77, 97, 114, 115, 10, 74, 117, 112, 105, 116, 101, 114, 10, 83, 97, 116, 117, 114, 110, 10, 0};
static const unsigned char input_3[] = {50, 10, 78, 101, 112, 116, 117, 110, 101, 10, 86, 101, 110, 117, 115, 10, 0};
static const unsigned char output_3[] = {69, 97, 114, 116, 104, 10, 77, 97, 114, 115, 10, 74, 117, 112, 105, 116, 101, 114, 10, 83, 97, 116, 117, 114, 110, 10, 85, 114, 97, 110, 117, 115, 10, 0};
static const unsigned char input_4[] = {50, 10, 69, 97, 114, 116, 104, 10, 69, 97, 114, 116, 104, 10, 0};
static const unsigned char output_4[] = {10, 0};
static const unsigned char input_5[] = {50, 10, 77, 97, 114, 115, 10, 69, 97, 114, 116, 104, 10, 0};
static const unsigned char output_5[] = {10, 0};
static const unsigned char input_6[] = {50, 10, 74, 117, 112, 105, 116, 101, 114, 10, 77, 97, 107, 101, 109, 97, 107, 101, 10, 0};
static const unsigned char output_6[] = {10, 0};

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
    free(input);
    return 1;
}
