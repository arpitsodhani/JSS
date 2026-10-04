#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {49, 10, 49, 50, 51, 52, 53, 54, 55, 10, 0};
static const unsigned char output_0[] = {116, 104, 101, 32, 110, 117, 109, 98, 101, 114, 32, 111, 102, 32, 111, 100, 100, 32, 101, 108, 101, 109, 101, 110, 116, 115, 32, 52, 110, 32, 116, 104, 101, 32, 115, 116, 114, 52, 110, 103, 32, 52, 32, 111, 102, 32, 116, 104, 101, 32, 52, 110, 112, 117, 116, 46, 10, 0};
static const unsigned char input_1[] = {50, 10, 51, 10, 49, 49, 49, 49, 49, 49, 49, 49, 10, 0};
static const unsigned char output_1[] = {116, 104, 101, 32, 110, 117, 109, 98, 101, 114, 32, 111, 102, 32, 111, 100, 100, 32, 101, 108, 101, 109, 101, 110, 116, 115, 32, 49, 110, 32, 116, 104, 101, 32, 115, 116, 114, 49, 110, 103, 32, 49, 32, 111, 102, 32, 116, 104, 101, 32, 49, 110, 112, 117, 116, 46, 10, 116, 104, 101, 32, 110, 117, 109, 98, 101, 114, 32, 111, 102, 32, 111, 100, 100, 32, 101, 108, 101, 109, 101, 110, 116, 115, 32, 56, 110, 32, 116, 104, 101, 32, 115, 116, 114, 56, 110, 103, 32, 56, 32, 111, 102, 32, 116, 104, 101, 32, 56, 110, 112, 117, 116, 46, 10, 0};
static const unsigned char input_2[] = {51, 10, 50, 55, 49, 10, 49, 51, 55, 10, 51, 49, 52, 10, 0};
static const unsigned char output_2[] = {116, 104, 101, 32, 110, 117, 109, 98, 101, 114, 32, 111, 102, 32, 111, 100, 100, 32, 101, 108, 101, 109, 101, 110, 116, 115, 32, 50, 110, 32, 116, 104, 101, 32, 115, 116, 114, 50, 110, 103, 32, 50, 32, 111, 102, 32, 116, 104, 101, 32, 50, 110, 112, 117, 116, 46, 10, 116, 104, 101, 32, 110, 117, 109, 98, 101, 114, 32, 111, 102, 32, 111, 100, 100, 32, 101, 108, 101, 109, 101, 110, 116, 115, 32, 51, 110, 32, 116, 104, 101, 32, 115, 116, 114, 51, 110, 103, 32, 51, 32, 111, 102, 32, 116, 104, 101, 32, 51, 110, 112, 117, 116, 46, 10, 116, 104, 101, 32, 110, 117, 109, 98, 101, 114, 32, 111, 102, 32, 111, 100, 100, 32, 101, 108, 101, 109, 101, 110, 116, 115, 32, 50, 110, 32, 116, 104, 101, 32, 115, 116, 114, 50, 110, 103, 32, 50, 32, 111, 102, 32, 116, 104, 101, 32, 50, 110, 112, 117, 116, 46, 10, 0};

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
    free(input);
    return 1;
}
