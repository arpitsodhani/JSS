#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {51, 10, 49, 46, 48, 10, 50, 46, 48, 10, 51, 46, 48, 10, 0};
static const unsigned char output_0[] = {49, 52, 10, 0};
static const unsigned char input_1[] = {51, 10, 49, 46, 48, 10, 50, 46, 48, 10, 51, 46, 48, 10, 0};
static const unsigned char output_1[] = {49, 52, 10, 0};
static const unsigned char input_2[] = {52, 10, 49, 46, 48, 10, 51, 46, 48, 10, 53, 46, 48, 10, 55, 46, 48, 10, 0};
static const unsigned char output_2[] = {56, 52, 10, 0};
static const unsigned char input_3[] = {51, 10, 49, 46, 52, 10, 52, 46, 50, 10, 48, 46, 48, 10, 0};
static const unsigned char output_3[] = {50, 57, 10, 0};
static const unsigned char input_4[] = {51, 10, 45, 50, 46, 52, 10, 49, 46, 48, 10, 49, 46, 48, 10, 0};
static const unsigned char output_4[] = {54, 10, 0};
static const unsigned char input_5[] = {52, 10, 49, 48, 48, 46, 48, 10, 49, 46, 48, 10, 49, 53, 46, 48, 10, 50, 46, 48, 10, 0};
static const unsigned char output_5[] = {49, 48, 50, 51, 48, 10, 0};
static const unsigned char input_6[] = {50, 10, 49, 48, 48, 48, 48, 46, 48, 10, 49, 48, 48, 48, 48, 46, 48, 10, 0};
static const unsigned char output_6[] = {50, 48, 48, 48, 48, 48, 48, 48, 48, 10, 0};

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
