#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {49, 10, 65, 115, 68, 102, 10, 0};
static const unsigned char output_0[] = {97, 83, 100, 70, 10, 0};
static const unsigned char input_1[] = {49, 10, 49, 50, 51, 52, 10, 0};
static const unsigned char output_1[] = {52, 51, 50, 49, 10, 0};
static const unsigned char input_2[] = {49, 10, 97, 98, 10, 0};
static const unsigned char output_2[] = {65, 66, 10, 0};
static const unsigned char input_3[] = {49, 10, 35, 97, 64, 67, 10, 0};
static const unsigned char output_3[] = {35, 65, 64, 99, 10, 0};
static const unsigned char input_4[] = {49, 10, 35, 65, 115, 100, 102, 87, 94, 52, 53, 10, 0};
static const unsigned char output_4[] = {35, 97, 83, 68, 70, 119, 94, 52, 53, 10, 0};
static const unsigned char input_5[] = {49, 10, 35, 54, 64, 50, 10, 0};
static const unsigned char output_5[] = {50, 64, 54, 35, 10, 0};
static const unsigned char input_6[] = {49, 10, 35, 36, 97, 94, 68, 10, 0};
static const unsigned char output_6[] = {35, 36, 65, 94, 100, 10, 0};
static const unsigned char input_7[] = {49, 10, 35, 99, 99, 99, 10, 0};
static const unsigned char output_7[] = {35, 67, 67, 67, 10, 0};

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
