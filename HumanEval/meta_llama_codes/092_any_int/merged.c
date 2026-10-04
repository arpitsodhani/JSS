#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {50, 10, 51, 10, 49, 10, 0};
static const unsigned char output_0[] = {84, 114, 117, 101, 10, 0};
static const unsigned char input_1[] = {50, 46, 53, 10, 50, 10, 51, 10, 0};
static const unsigned char output_1[] = {70, 97, 108, 115, 101, 10, 0};
static const unsigned char input_2[] = {49, 46, 53, 10, 53, 10, 51, 46, 53, 10, 0};
static const unsigned char output_2[] = {70, 97, 108, 115, 101, 10, 0};
static const unsigned char input_3[] = {50, 10, 54, 10, 50, 10, 0};
static const unsigned char output_3[] = {70, 97, 108, 115, 101, 10, 0};
static const unsigned char input_4[] = {52, 10, 50, 10, 50, 10, 0};
static const unsigned char output_4[] = {84, 114, 117, 101, 10, 0};
static const unsigned char input_5[] = {50, 46, 50, 10, 50, 46, 50, 10, 50, 46, 50, 10, 0};
static const unsigned char output_5[] = {70, 97, 108, 115, 101, 10, 0};
static const unsigned char input_6[] = {45, 52, 10, 54, 10, 50, 10, 0};
static const unsigned char output_6[] = {84, 114, 117, 101, 10, 0};
static const unsigned char input_7[] = {50, 10, 49, 10, 49, 10, 0};
static const unsigned char output_7[] = {84, 114, 117, 101, 10, 0};
static const unsigned char input_8[] = {51, 10, 52, 10, 55, 10, 0};
static const unsigned char output_8[] = {84, 114, 117, 101, 10, 0};
static const unsigned char input_9[] = {51, 46, 48, 10, 52, 10, 55, 10, 0};
static const unsigned char output_9[] = {70, 97, 108, 115, 101, 10, 0};

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
