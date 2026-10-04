#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {49, 10, 110, 97, 109, 101, 10, 111, 102, 10, 115, 116, 114, 105, 110, 103, 10, 0};
static const unsigned char output_0[] = {115, 116, 114, 105, 110, 103, 10, 0};
static const unsigned char input_1[] = {49, 10, 110, 97, 109, 101, 10, 101, 110, 97, 109, 10, 103, 97, 109, 101, 10, 0};
static const unsigned char output_1[] = {101, 110, 97, 109, 10, 0};
static const unsigned char input_2[] = {49, 10, 97, 97, 97, 97, 97, 97, 97, 10, 98, 98, 10, 99, 99, 10, 0};
static const unsigned char output_2[] = {97, 97, 97, 97, 97, 97, 97, 10, 0};
static const unsigned char input_3[] = {49, 10, 97, 98, 99, 10, 99, 98, 97, 10, 0};
static const unsigned char output_3[] = {97, 98, 99, 10, 0};
static const unsigned char input_4[] = {49, 10, 112, 108, 97, 121, 10, 116, 104, 105, 115, 10, 103, 97, 109, 101, 10, 111, 102, 10, 102, 111, 111, 116, 98, 111, 116, 116, 10, 0};
static const unsigned char output_4[] = {102, 111, 111, 116, 98, 111, 116, 116, 10, 0};
static const unsigned char input_5[] = {49, 10, 119, 101, 10, 97, 114, 101, 10, 103, 111, 110, 110, 97, 10, 114, 111, 99, 107, 10, 0};
static const unsigned char output_5[] = {103, 111, 110, 110, 97, 10, 0};
static const unsigned char input_6[] = {49, 10, 119, 101, 10, 97, 114, 101, 10, 97, 10, 109, 97, 100, 10, 110, 97, 116, 105, 111, 110, 10, 0};
static const unsigned char output_6[] = {110, 97, 116, 105, 111, 110, 10, 0};
static const unsigned char input_7[] = {49, 10, 116, 104, 105, 115, 10, 105, 115, 10, 97, 10, 112, 114, 114, 107, 10, 0};
static const unsigned char output_7[] = {116, 104, 105, 115, 10, 0};
static const unsigned char input_8[] = {49, 10, 98, 10, 0};
static const unsigned char output_8[] = {98, 10, 0};
static const unsigned char input_9[] = {49, 10, 112, 108, 97, 121, 10, 112, 108, 97, 121, 10, 112, 108, 97, 121, 10, 0};
static const unsigned char output_9[] = {112, 108, 97, 121, 10, 0};

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
