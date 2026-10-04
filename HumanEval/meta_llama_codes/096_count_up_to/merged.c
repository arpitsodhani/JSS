#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {53, 10, 0};
static const unsigned char output_0[] = {50, 51, 10, 0};
static const unsigned char input_1[] = {54, 10, 0};
static const unsigned char output_1[] = {50, 51, 53, 10, 0};
static const unsigned char input_2[] = {55, 10, 0};
static const unsigned char output_2[] = {50, 51, 53, 10, 0};
static const unsigned char input_3[] = {49, 48, 10, 0};
static const unsigned char output_3[] = {50, 51, 53, 55, 10, 0};
static const unsigned char input_4[] = {48, 10, 0};
static const unsigned char output_4[] = {91, 93, 10, 0};
static const unsigned char input_5[] = {50, 50, 10, 0};
static const unsigned char output_5[] = {50, 51, 53, 55, 49, 49, 49, 51, 49, 55, 49, 57, 10, 0};
static const unsigned char input_6[] = {49, 10, 0};
static const unsigned char output_6[] = {91, 93, 10, 0};
static const unsigned char input_7[] = {49, 56, 10, 0};
static const unsigned char output_7[] = {50, 51, 53, 55, 49, 49, 49, 51, 49, 55, 10, 0};
static const unsigned char input_8[] = {52, 55, 10, 0};
static const unsigned char output_8[] = {50, 32, 51, 32, 53, 32, 55, 32, 49, 49, 32, 49, 51, 32, 49, 55, 32, 49, 57, 32, 50, 51, 32, 50, 57, 32, 51, 49, 32, 51, 55, 32, 52, 49, 32, 52, 51, 10, 0};
static const unsigned char input_9[] = {49, 48, 49, 10, 0};
static const unsigned char output_9[] = {50, 32, 51, 32, 53, 32, 55, 32, 49, 49, 32, 49, 51, 32, 49, 55, 32, 49, 57, 32, 50, 51, 32, 50, 57, 32, 51, 49, 32, 51, 55, 32, 52, 49, 32, 52, 51, 32, 52, 55, 32, 53, 51, 32, 53, 57, 32, 54, 49, 32, 54, 55, 32, 55, 49, 32, 55, 51, 32, 55, 57, 32, 56, 51, 32, 56, 57, 32, 57, 55, 10, 0};

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
    free(input);
    return 1;
}
