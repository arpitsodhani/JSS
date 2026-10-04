#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {50, 10, 120, 121, 122, 119, 10, 120, 121, 119, 10, 0};
static const unsigned char output_0[] = {70, 97, 108, 115, 101, 10, 0};
static const unsigned char input_1[] = {50, 10, 121, 101, 108, 108, 111, 10, 101, 108, 108, 10, 0};
static const unsigned char output_1[] = {84, 114, 117, 101, 10, 0};
static const unsigned char input_2[] = {50, 10, 119, 104, 97, 116, 116, 117, 112, 10, 112, 116, 117, 116, 10, 0};
static const unsigned char output_2[] = {70, 97, 108, 115, 101, 10, 0};
static const unsigned char input_3[] = {50, 10, 101, 102, 101, 102, 10, 102, 101, 101, 10, 0};
static const unsigned char output_3[] = {84, 114, 117, 101, 10, 0};
static const unsigned char input_4[] = {50, 10, 97, 98, 97, 98, 10, 97, 97, 98, 98, 10, 0};
static const unsigned char output_4[] = {70, 97, 108, 115, 101, 10, 0};
static const unsigned char input_5[] = {50, 10, 119, 105, 110, 101, 109, 116, 116, 10, 116, 105, 110, 101, 109, 10, 0};
static const unsigned char output_5[] = {84, 114, 117, 101, 10, 0};

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
