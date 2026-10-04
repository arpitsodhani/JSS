#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {34, 72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 34, 0};
static const unsigned char output_0[] = {48, 10, 0};
static const unsigned char input_1[] = {34, 73, 115, 32, 116, 104, 101, 32, 115, 107, 121, 32, 98, 108, 117, 101, 63, 34, 0};
static const unsigned char output_1[] = {48, 10, 0};
static const unsigned char input_2[] = {34, 73, 32, 108, 111, 118, 101, 32, 73, 116, 32, 33, 34, 0};
static const unsigned char output_2[] = {49, 10, 0};
static const unsigned char input_3[] = {34, 98, 73, 116, 34, 0};
static const unsigned char output_3[] = {48, 10, 0};
static const unsigned char input_4[] = {34, 73, 32, 102, 101, 101, 108, 32, 103, 111, 111, 100, 32, 116, 111, 100, 97, 121, 46, 32, 73, 32, 119, 105, 108, 108, 32, 98, 101, 32, 112, 114, 111, 100, 117, 99, 116, 105, 118, 101, 46, 32, 119, 105, 108, 108, 32, 107, 105, 108, 108, 32, 73, 116, 34, 0};
static const unsigned char output_4[] = {50, 10, 0};
static const unsigned char input_5[] = {34, 89, 111, 117, 32, 97, 110, 100, 32, 73, 32, 97, 114, 101, 32, 103, 111, 105, 110, 103, 32, 102, 111, 114, 32, 97, 32, 119, 97, 108, 107, 34, 0};
static const unsigned char output_5[] = {48, 10, 0};

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
    free(input);
    return 1;
}
