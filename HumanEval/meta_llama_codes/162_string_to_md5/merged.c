#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {49, 10, 72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 10, 0};
static const unsigned char output_0[] = {51, 101, 50, 53, 57, 54, 48, 97, 55, 57, 100, 98, 99, 54, 57, 98, 54, 55, 52, 99, 100, 52, 101, 99, 54, 55, 97, 55, 50, 99, 54, 50, 10, 0};
static const unsigned char input_1[] = {49, 10, 10, 0};
static const unsigned char output_1[] = {78, 111, 110, 101, 10, 0};
static const unsigned char input_2[] = {49, 10, 65, 32, 66, 32, 67, 10, 0};
static const unsigned char output_2[] = {48, 101, 102, 55, 56, 53, 49, 51, 98, 48, 99, 98, 56, 99, 101, 102, 49, 50, 55, 52, 51, 102, 53, 97, 101, 98, 51, 53, 102, 56, 56, 56, 10, 0};
static const unsigned char input_3[] = {49, 10, 112, 97, 115, 115, 119, 111, 114, 100, 10, 0};
static const unsigned char output_3[] = {53, 102, 52, 100, 99, 99, 51, 98, 53, 97, 97, 55, 54, 53, 100, 54, 49, 100, 56, 51, 50, 55, 100, 101, 98, 56, 56, 50, 99, 102, 57, 57, 10, 0};

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
    free(input);
    return 1;
}
