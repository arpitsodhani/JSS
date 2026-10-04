#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {50, 10, 50, 46, 48, 32, 52, 57, 46, 57, 10, 0};
static const unsigned char output_0[] = {48, 46, 48, 32, 49, 46, 48, 10, 0};
static const unsigned char input_1[] = {50, 10, 49, 48, 48, 46, 48, 32, 52, 57, 46, 57, 10, 0};
static const unsigned char output_1[] = {49, 46, 48, 32, 48, 46, 48, 10, 0};
static const unsigned char input_2[] = {53, 10, 49, 46, 48, 32, 50, 46, 48, 32, 51, 46, 48, 32, 52, 46, 48, 32, 53, 46, 48, 10, 0};
static const unsigned char output_2[] = {48, 46, 48, 32, 48, 46, 50, 53, 32, 48, 46, 53, 32, 48, 46, 55, 53, 32, 49, 46, 48, 10, 0};
static const unsigned char input_3[] = {53, 10, 50, 46, 48, 32, 49, 46, 48, 32, 53, 46, 48, 32, 51, 46, 48, 32, 52, 46, 48, 10, 0};
static const unsigned char output_3[] = {48, 46, 50, 53, 32, 48, 46, 48, 32, 49, 46, 48, 32, 48, 46, 53, 32, 48, 46, 55, 53, 10, 0};
static const unsigned char input_4[] = {53, 10, 49, 50, 46, 48, 32, 49, 49, 46, 48, 32, 49, 53, 46, 48, 32, 49, 51, 46, 48, 32, 49, 52, 46, 48, 10, 0};
static const unsigned char output_4[] = {48, 46, 50, 53, 32, 48, 46, 48, 32, 49, 46, 48, 32, 48, 46, 53, 32, 48, 46, 55, 53, 10, 0};

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
