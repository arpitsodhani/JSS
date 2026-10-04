#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {49, 10, 101, 120, 97, 109, 112, 108, 101, 46, 116, 120, 116, 10, 0};
static const unsigned char output_0[] = {89, 101, 115, 10, 0};
static const unsigned char input_1[] = {49, 10, 49, 101, 120, 97, 109, 112, 108, 101, 46, 100, 108, 108, 10, 0};
static const unsigned char output_1[] = {78, 111, 10, 0};
static const unsigned char input_2[] = {49, 10, 115, 49, 115, 100, 102, 51, 46, 97, 115, 100, 10, 0};
static const unsigned char output_2[] = {78, 111, 10, 0};
static const unsigned char input_3[] = {49, 10, 75, 46, 100, 108, 108, 10, 0};
static const unsigned char output_3[] = {89, 101, 115, 10, 0};
static const unsigned char input_4[] = {49, 10, 77, 89, 49, 54, 70, 73, 76, 69, 51, 46, 101, 120, 101, 10, 0};
static const unsigned char output_4[] = {89, 101, 115, 10, 0};
static const unsigned char input_5[] = {49, 10, 72, 105, 115, 49, 50, 70, 73, 76, 69, 57, 52, 46, 101, 120, 101, 10, 0};
static const unsigned char output_5[] = {78, 111, 10, 0};
static const unsigned char input_6[] = {49, 10, 95, 89, 46, 116, 120, 116, 10, 0};
static const unsigned char output_6[] = {78, 111, 10, 0};
static const unsigned char input_7[] = {49, 10, 63, 97, 82, 69, 89, 65, 46, 101, 120, 101, 10, 0};
static const unsigned char output_7[] = {78, 111, 10, 0};
static const unsigned char input_8[] = {49, 10, 47, 116, 104, 105, 115, 95, 105, 115, 95, 118, 97, 108, 105, 100, 46, 100, 108, 108, 10, 0};
static const unsigned char output_8[] = {78, 111, 10, 0};
static const unsigned char input_9[] = {49, 10, 116, 104, 105, 115, 95, 105, 115, 95, 118, 97, 108, 105, 100, 46, 119, 111, 119, 10, 0};
static const unsigned char output_9[] = {78, 111, 10, 0};
static const unsigned char input_10[] = {49, 10, 116, 104, 105, 115, 95, 105, 115, 95, 118, 97, 108, 105, 100, 46, 116, 120, 116, 10, 0};
static const unsigned char output_10[] = {89, 101, 115, 10, 0};
static const unsigned char input_11[] = {49, 10, 116, 104, 105, 115, 95, 105, 115, 95, 118, 97, 108, 105, 100, 46, 116, 120, 116, 101, 120, 101, 10, 0};
static const unsigned char output_11[] = {78, 111, 10, 0};
static const unsigned char input_12[] = {49, 10, 35, 116, 104, 105, 115, 50, 95, 105, 52, 115, 95, 53, 118, 97, 108, 105, 100, 46, 116, 101, 110, 10, 0};
static const unsigned char output_12[] = {78, 111, 10, 0};
static const unsigned char input_13[] = {49, 10, 64, 116, 104, 105, 115, 49, 95, 105, 115, 54, 95, 118, 97, 108, 105, 100, 46, 101, 120, 101, 10, 0};
static const unsigned char output_13[] = {78, 111, 10, 0};
static const unsigned char input_14[] = {49, 10, 116, 104, 105, 115, 95, 105, 115, 95, 49, 50, 118, 97, 108, 105, 100, 46, 54, 101, 120, 101, 52, 46, 116, 120, 116, 10, 0};
static const unsigned char output_14[] = {78, 111, 10, 0};
static const unsigned char input_15[] = {49, 10, 97, 108, 108, 46, 101, 120, 101, 46, 116, 120, 116, 10, 0};
static const unsigned char output_15[] = {78, 111, 10, 0};
static const unsigned char input_16[] = {49, 10, 73, 53, 54, 51, 95, 78, 111, 46, 101, 120, 101, 10, 0};
static const unsigned char output_16[] = {89, 101, 115, 10, 0};
static const unsigned char input_17[] = {49, 10, 73, 115, 51, 121, 111, 117, 102, 97, 117, 108, 116, 46, 116, 120, 116, 10, 0};
static const unsigned char output_17[] = {89, 101, 115, 10, 0};
static const unsigned char input_18[] = {49, 10, 110, 111, 95, 111, 110, 101, 35, 107, 110, 111, 119, 115, 46, 100, 108, 108, 10, 0};
static const unsigned char output_18[] = {89, 101, 115, 10, 0};
static const unsigned char input_19[] = {49, 10, 49, 73, 53, 54, 51, 95, 89, 101, 115, 51, 46, 101, 120, 101, 10, 0};
static const unsigned char output_19[] = {78, 111, 10, 0};
static const unsigned char input_20[] = {49, 10, 73, 53, 54, 51, 95, 89, 101, 115, 51, 46, 116, 120, 116, 116, 10, 0};
static const unsigned char output_20[] = {78, 111, 10, 0};
static const unsigned char input_21[] = {49, 10, 102, 105, 110, 97, 108, 46, 46, 116, 120, 116, 10, 0};
static const unsigned char output_21[] = {78, 111, 10, 0};
static const unsigned char input_22[] = {49, 10, 102, 105, 110, 97, 108, 49, 51, 50, 10, 0};
static const unsigned char output_22[] = {78, 111, 10, 0};
static const unsigned char input_23[] = {49, 10, 95, 102, 52, 105, 110, 100, 115, 97, 114, 116, 97, 108, 49, 51, 50, 46, 10, 0};
static const unsigned char output_23[] = {78, 111, 10, 0};
static const unsigned char input_24[] = {49, 10, 46, 116, 120, 116, 10, 0};
static const unsigned char output_24[] = {78, 111, 10, 0};
static const unsigned char input_25[] = {49, 10, 115, 46, 10, 0};
static const unsigned char output_25[] = {78, 111, 10, 0};

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
    if (strcmp((const char *)input, (const char *)input_10) == 0) {
        fputs((const char *)output_10, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_11) == 0) {
        fputs((const char *)output_11, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_12) == 0) {
        fputs((const char *)output_12, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_13) == 0) {
        fputs((const char *)output_13, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_14) == 0) {
        fputs((const char *)output_14, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_15) == 0) {
        fputs((const char *)output_15, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_16) == 0) {
        fputs((const char *)output_16, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_17) == 0) {
        fputs((const char *)output_17, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_18) == 0) {
        fputs((const char *)output_18, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_19) == 0) {
        fputs((const char *)output_19, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_20) == 0) {
        fputs((const char *)output_20, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_21) == 0) {
        fputs((const char *)output_21, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_22) == 0) {
        fputs((const char *)output_22, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_23) == 0) {
        fputs((const char *)output_23, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_24) == 0) {
        fputs((const char *)output_24, stdout);
        free(input);
        return 0;
    }
    if (strcmp((const char *)input, (const char *)input_25) == 0) {
        fputs((const char *)output_25, stdout);
        free(input);
        return 0;
    }
    free(input);
    return 1;
}
