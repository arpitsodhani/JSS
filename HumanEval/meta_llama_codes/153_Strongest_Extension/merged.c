#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {50, 10, 87, 97, 116, 97, 115, 104, 105, 10, 116, 69, 78, 10, 110, 105, 78, 69, 10, 101, 73, 71, 72, 116, 56, 79, 75, 101, 10, 0};
static const unsigned char output_0[] = {87, 97, 116, 97, 115, 104, 105, 46, 101, 73, 71, 72, 116, 56, 79, 75, 101, 10, 0};
static const unsigned char input_1[] = {50, 10, 66, 111, 107, 117, 49, 50, 51, 10, 110, 97, 110, 105, 10, 78, 97, 122, 101, 68, 97, 10, 89, 69, 115, 46, 87, 101, 67, 97, 78, 101, 10, 51, 50, 49, 52, 53, 116, 103, 103, 103, 10, 0};
static const unsigned char output_1[] = {66, 111, 107, 117, 49, 50, 51, 46, 89, 69, 115, 46, 87, 101, 67, 97, 78, 101, 10, 0};
static const unsigned char input_2[] = {50, 10, 95, 95, 89, 69, 83, 73, 77, 72, 69, 82, 69, 10, 116, 10, 101, 77, 112, 116, 89, 10, 110, 111, 116, 104, 105, 110, 103, 10, 122, 101, 82, 48, 48, 10, 78, 117, 76, 108, 95, 95, 10, 49, 50, 51, 78, 111, 111, 111, 110, 101, 66, 51, 50, 49, 10, 0};
static const unsigned char output_2[] = {95, 95, 89, 69, 83, 73, 77, 72, 69, 82, 69, 46, 78, 117, 76, 108, 95, 95, 10, 0};
static const unsigned char input_3[] = {50, 10, 75, 10, 84, 97, 10, 84, 65, 82, 10, 116, 50, 51, 52, 65, 110, 10, 99, 111, 115, 83, 111, 10, 0};
static const unsigned char output_3[] = {75, 46, 84, 65, 82, 10, 0};
static const unsigned char input_4[] = {50, 10, 95, 95, 72, 65, 72, 65, 10, 84, 97, 98, 10, 49, 50, 51, 10, 55, 56, 49, 51, 52, 53, 10, 45, 95, 45, 10, 0};
static const unsigned char output_4[] = {95, 95, 72, 65, 72, 65, 46, 49, 50, 51, 10, 0};
static const unsigned char input_5[] = {50, 10, 89, 97, 109, 101, 82, 111, 114, 101, 10, 72, 104, 65, 97, 115, 10, 111, 107, 73, 87, 73, 76, 76, 49, 50, 51, 10, 87, 111, 114, 107, 79, 117, 116, 10, 70, 97, 105, 108, 115, 10, 45, 95, 45, 10, 0};
static const unsigned char output_5[] = {89, 97, 109, 101, 82, 111, 114, 101, 46, 111, 107, 73, 87, 73, 76, 76, 49, 50, 51, 10, 0};
static const unsigned char input_6[] = {50, 10, 102, 105, 110, 78, 78, 97, 108, 76, 76, 108, 121, 10, 68, 105, 101, 10, 78, 111, 119, 87, 10, 87, 111, 119, 10, 87, 111, 87, 10, 0};
static const unsigned char output_6[] = {102, 105, 110, 78, 78, 97, 108, 76, 76, 108, 121, 46, 87, 111, 87, 10, 0};
static const unsigned char input_7[] = {50, 10, 95, 10, 66, 98, 10, 57, 49, 50, 52, 53, 10, 0};
static const unsigned char output_7[] = {95, 46, 66, 98, 10, 0};
static const unsigned char input_8[] = {50, 10, 83, 112, 10, 54, 55, 49, 50, 51, 53, 10, 66, 98, 10, 0};
static const unsigned char output_8[] = {83, 112, 46, 54, 55, 49, 50, 51, 53, 10, 0};

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
    free(input);
    return 1;
}
