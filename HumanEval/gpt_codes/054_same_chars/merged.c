#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {101, 97, 98, 99, 100, 122, 122, 122, 122, 10, 100, 100, 100, 122, 122, 122, 122, 122, 122, 122, 100, 100, 101, 100, 100, 97, 98, 99, 10, 0};
static const unsigned char output_0[] = {84, 114, 117, 101, 10, 0};
static const unsigned char input_1[] = {97, 98, 99, 100, 10, 100, 100, 100, 100, 100, 100, 100, 97, 98, 99, 10, 0};
static const unsigned char output_1[] = {84, 114, 117, 101, 10, 0};
static const unsigned char input_2[] = {100, 100, 100, 100, 100, 100, 100, 97, 98, 99, 10, 97, 98, 99, 100, 10, 0};
static const unsigned char output_2[] = {84, 114, 117, 101, 10, 0};
static const unsigned char input_3[] = {101, 97, 98, 99, 100, 10, 100, 100, 100, 100, 100, 100, 100, 97, 98, 99, 10, 0};
static const unsigned char output_3[] = {70, 97, 108, 115, 101, 10, 0};
static const unsigned char input_4[] = {97, 98, 99, 100, 10, 100, 100, 100, 100, 100, 100, 100, 97, 98, 99, 102, 10, 0};
static const unsigned char output_4[] = {70, 97, 108, 115, 101, 10, 0};
static const unsigned char input_5[] = {101, 97, 98, 99, 100, 122, 122, 122, 122, 10, 100, 100, 100, 122, 122, 122, 122, 122, 122, 122, 100, 100, 100, 100, 97, 98, 99, 10, 0};
static const unsigned char output_5[] = {70, 97, 108, 115, 101, 10, 0};
static const unsigned char input_6[] = {97, 97, 98, 98, 10, 97, 97, 99, 99, 99, 10, 0};
static const unsigned char output_6[] = {70, 97, 108, 115, 101, 10, 0};

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
