#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {84, 69, 83, 84, 10, 0};
static const unsigned char output_0[] = {116, 103, 115, 116, 10, 0};
static const unsigned char input_1[] = {77, 117, 100, 97, 115, 105, 114, 10, 0};
static const unsigned char output_1[] = {109, 87, 68, 67, 83, 75, 82, 10, 0};
static const unsigned char input_2[] = {89, 69, 83, 10, 0};
static const unsigned char output_2[] = {121, 103, 115, 10, 0};
static const unsigned char input_3[] = {84, 104, 105, 115, 32, 105, 115, 32, 97, 32, 109, 101, 115, 115, 97, 103, 101, 10, 0};
static const unsigned char output_3[] = {116, 72, 75, 83, 32, 75, 83, 32, 67, 32, 77, 71, 83, 83, 67, 71, 71, 10, 0};
static const unsigned char input_4[] = {73, 32, 68, 111, 78, 116, 32, 75, 110, 79, 119, 32, 87, 104, 65, 116, 32, 116, 79, 32, 87, 114, 73, 116, 69, 10, 0};
static const unsigned char output_4[] = {107, 32, 100, 81, 110, 84, 32, 107, 78, 113, 87, 32, 119, 72, 99, 84, 32, 84, 113, 32, 119, 82, 107, 84, 103, 10, 0};

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
    free(input);
    return 1;
}
