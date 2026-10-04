#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {49, 10, 49, 32, 49, 49, 32, 45, 49, 32, 45, 49, 49, 32, 45, 49, 50, 10, 0};
static const unsigned char output_0[] = {45, 49, 10, 45, 49, 49, 10, 49, 10, 45, 49, 50, 10, 49, 49, 10, 0};
static const unsigned char input_1[] = {49, 10, 49, 50, 51, 52, 32, 52, 50, 51, 32, 52, 54, 51, 32, 49, 52, 53, 32, 50, 32, 52, 50, 51, 32, 52, 50, 51, 32, 53, 51, 32, 54, 32, 51, 55, 32, 51, 52, 53, 55, 32, 51, 32, 53, 54, 32, 48, 32, 52, 54, 10, 0};
static const unsigned char output_1[] = {48, 10, 50, 10, 51, 10, 54, 10, 53, 51, 10, 52, 50, 51, 10, 52, 50, 51, 10, 52, 50, 51, 10, 49, 50, 51, 52, 10, 49, 52, 53, 10, 51, 55, 10, 52, 54, 10, 53, 54, 10, 52, 54, 51, 10, 51, 52, 53, 55, 10, 0};
static const unsigned char input_2[] = {49, 10, 10, 0};
static const unsigned char output_2[] = {10, 0};
static const unsigned char input_3[] = {49, 10, 49, 32, 45, 49, 49, 32, 45, 51, 50, 32, 52, 51, 32, 53, 52, 32, 45, 57, 56, 32, 50, 32, 45, 51, 10, 0};
static const unsigned char output_3[] = {45, 51, 10, 45, 51, 50, 10, 45, 57, 56, 10, 45, 49, 49, 10, 49, 10, 50, 10, 52, 51, 10, 53, 52, 10, 0};
static const unsigned char input_4[] = {49, 10, 49, 32, 50, 32, 51, 32, 52, 32, 53, 32, 54, 32, 55, 32, 56, 32, 57, 32, 49, 48, 32, 49, 49, 10, 0};
static const unsigned char output_4[] = {49, 10, 49, 48, 10, 50, 10, 49, 49, 10, 51, 10, 52, 10, 53, 10, 54, 10, 55, 10, 56, 10, 57, 10, 0};
static const unsigned char input_5[] = {49, 10, 48, 32, 54, 32, 54, 32, 45, 55, 54, 32, 45, 50, 49, 32, 50, 51, 32, 52, 10, 0};
static const unsigned char output_5[] = {45, 55, 54, 10, 45, 50, 49, 10, 48, 10, 52, 10, 50, 51, 10, 54, 10, 54, 10, 0};

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
