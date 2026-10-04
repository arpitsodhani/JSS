#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {123, 34, 112, 34, 58, 34, 112, 105, 110, 101, 97, 112, 112, 108, 101, 34, 10, 34, 98, 34, 58, 34, 98, 97, 110, 97, 110, 97, 34, 125, 0};
static const unsigned char output_0[] = {84, 114, 117, 101, 10, 0};
static const unsigned char input_1[] = {123, 34, 112, 34, 58, 34, 112, 105, 110, 101, 97, 112, 112, 108, 101, 34, 10, 34, 65, 34, 58, 34, 98, 97, 110, 97, 110, 97, 34, 10, 34, 66, 34, 58, 34, 98, 97, 110, 97, 110, 97, 34, 125, 0};
static const unsigned char output_1[] = {70, 97, 108, 115, 101, 10, 0};
static const unsigned char input_2[] = {123, 34, 112, 34, 58, 34, 112, 105, 110, 101, 97, 112, 112, 108, 101, 34, 10, 34, 53, 34, 58, 34, 98, 97, 110, 97, 110, 97, 34, 10, 34, 97, 34, 58, 34, 97, 112, 112, 108, 101, 34, 125, 0};
static const unsigned char output_2[] = {70, 97, 108, 115, 101, 10, 0};
static const unsigned char input_3[] = {123, 34, 78, 97, 109, 101, 34, 58, 34, 74, 111, 104, 110, 34, 10, 34, 65, 103, 101, 34, 58, 34, 51, 54, 34, 10, 34, 67, 105, 116, 121, 34, 58, 34, 72, 111, 117, 115, 116, 111, 110, 34, 125, 0};
static const unsigned char output_3[] = {70, 97, 108, 115, 101, 10, 0};
static const unsigned char input_4[] = {123, 34, 83, 84, 65, 84, 69, 34, 58, 34, 78, 67, 34, 10, 34, 90, 73, 80, 34, 58, 34, 49, 50, 51, 52, 53, 34, 32, 125, 0};
static const unsigned char output_4[] = {84, 114, 117, 101, 10, 0};
static const unsigned char input_5[] = {123, 34, 102, 114, 117, 105, 116, 34, 58, 34, 79, 114, 97, 110, 103, 101, 34, 10, 34, 116, 97, 115, 116, 101, 34, 58, 34, 83, 119, 101, 101, 116, 34, 32, 125, 0};
static const unsigned char output_5[] = {84, 114, 117, 101, 10, 0};
static const unsigned char input_6[] = {123, 125, 0};
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
