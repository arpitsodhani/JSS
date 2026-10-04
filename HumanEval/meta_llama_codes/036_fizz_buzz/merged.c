#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {53, 48, 10, 0};
static const unsigned char output_0[] = {48, 10, 0};
static const unsigned char input_1[] = {55, 56, 10, 0};
static const unsigned char output_1[] = {50, 10, 0};
static const unsigned char input_2[] = {55, 57, 10, 0};
static const unsigned char output_2[] = {51, 10, 0};
static const unsigned char input_3[] = {49, 48, 48, 10, 0};
static const unsigned char output_3[] = {51, 10, 0};
static const unsigned char input_4[] = {50, 48, 48, 10, 0};
static const unsigned char output_4[] = {54, 10, 0};
static const unsigned char input_5[] = {52, 48, 48, 48, 10, 0};
static const unsigned char output_5[] = {49, 57, 50, 10, 0};
static const unsigned char input_6[] = {49, 48, 48, 48, 48, 10, 0};
static const unsigned char output_6[] = {54, 51, 57, 10, 0};
static const unsigned char input_7[] = {49, 48, 48, 48, 48, 48, 10, 0};
static const unsigned char output_7[] = {56, 48, 50, 54, 10, 0};

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
    free(input);
    return 1;
}
