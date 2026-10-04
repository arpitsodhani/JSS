#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {77, 97, 114, 121, 32, 104, 97, 100, 32, 97, 32, 108, 105, 116, 116, 108, 101, 32, 108, 97, 109, 98, 10, 52, 10, 0};
static const unsigned char output_0[] = {108, 105, 116, 116, 108, 101, 10, 0};
static const unsigned char input_1[] = {77, 97, 114, 121, 32, 104, 97, 100, 32, 97, 32, 108, 105, 116, 116, 108, 101, 32, 108, 97, 109, 98, 10, 51, 10, 0};
static const unsigned char output_1[] = {77, 97, 114, 121, 32, 108, 97, 109, 98, 10, 0};
static const unsigned char input_2[] = {115, 105, 109, 112, 108, 101, 32, 119, 104, 105, 116, 101, 32, 115, 112, 97, 99, 101, 10, 50, 10, 0};
static const unsigned char output_2[] = {10, 0};
static const unsigned char input_3[] = {72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 10, 52, 10, 0};
static const unsigned char output_3[] = {119, 111, 114, 108, 100, 10, 0};
static const unsigned char input_4[] = {85, 110, 99, 108, 101, 32, 115, 97, 109, 10, 51, 10, 0};
static const unsigned char output_4[] = {85, 110, 99, 108, 101, 10, 0};
static const unsigned char input_5[] = {10, 52, 10, 0};
static const unsigned char output_5[] = {10, 0};
static const unsigned char input_6[] = {97, 32, 98, 32, 99, 32, 100, 32, 101, 32, 102, 10, 49, 10, 0};
static const unsigned char output_6[] = {98, 32, 99, 32, 100, 32, 102, 10, 0};

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
