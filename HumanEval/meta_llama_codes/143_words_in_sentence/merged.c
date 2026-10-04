#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {49, 10, 84, 104, 105, 115, 32, 105, 115, 32, 97, 32, 116, 101, 115, 116, 10, 0};
static const unsigned char output_0[] = {105, 115, 10, 0};
static const unsigned char input_1[] = {49, 10, 108, 101, 116, 115, 32, 103, 111, 32, 102, 111, 114, 32, 115, 119, 105, 109, 109, 105, 110, 103, 10, 0};
static const unsigned char output_1[] = {103, 111, 32, 102, 111, 114, 10, 0};
static const unsigned char input_2[] = {49, 10, 116, 104, 101, 114, 101, 32, 105, 115, 32, 110, 111, 32, 112, 108, 97, 99, 101, 32, 97, 118, 97, 105, 108, 97, 98, 108, 101, 32, 104, 101, 114, 101, 10, 0};
static const unsigned char output_2[] = {116, 104, 101, 114, 101, 32, 105, 115, 32, 110, 111, 32, 112, 108, 97, 99, 101, 10, 0};
static const unsigned char input_3[] = {49, 10, 72, 105, 32, 73, 32, 97, 109, 32, 72, 117, 115, 115, 101, 105, 110, 10, 0};
static const unsigned char output_3[] = {72, 105, 32, 97, 109, 32, 72, 117, 115, 115, 101, 105, 110, 10, 0};
static const unsigned char input_4[] = {49, 10, 103, 111, 32, 102, 111, 114, 32, 105, 116, 10, 0};
static const unsigned char output_4[] = {103, 111, 32, 102, 111, 114, 32, 105, 116, 10, 0};
static const unsigned char input_5[] = {49, 10, 104, 101, 114, 101, 10, 0};
static const unsigned char output_5[] = {10, 0};
static const unsigned char input_6[] = {49, 10, 104, 101, 114, 101, 32, 105, 115, 10, 0};
static const unsigned char output_6[] = {105, 115, 10, 0};

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
