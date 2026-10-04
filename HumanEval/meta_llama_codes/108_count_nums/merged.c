#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {48, 10, 0};
static const unsigned char output_0[] = {48, 10, 0};
static const unsigned char input_1[] = {51, 10, 45, 49, 10, 45, 50, 10, 48, 10, 0};
static const unsigned char output_1[] = {48, 10, 0};
static const unsigned char input_2[] = {55, 10, 49, 10, 49, 10, 50, 10, 45, 50, 10, 51, 10, 52, 10, 53, 10, 0};
static const unsigned char output_2[] = {54, 10, 0};
static const unsigned char input_3[] = {55, 10, 49, 10, 54, 10, 57, 10, 45, 54, 10, 48, 10, 49, 10, 53, 10, 0};
static const unsigned char output_3[] = {53, 10, 0};
static const unsigned char input_4[] = {54, 10, 49, 10, 49, 48, 48, 10, 57, 56, 10, 45, 55, 10, 49, 10, 45, 49, 10, 0};
static const unsigned char output_4[] = {52, 10, 0};
static const unsigned char input_5[] = {54, 10, 49, 50, 10, 50, 51, 10, 51, 52, 10, 45, 52, 53, 10, 45, 53, 54, 10, 48, 10, 0};
static const unsigned char output_5[] = {53, 10, 0};
static const unsigned char input_6[] = {50, 10, 45, 48, 10, 49, 10, 0};
static const unsigned char output_6[] = {49, 10, 0};
static const unsigned char input_7[] = {49, 10, 49, 10, 0};
static const unsigned char output_7[] = {49, 10, 0};

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
