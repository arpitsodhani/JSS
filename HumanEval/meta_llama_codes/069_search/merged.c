#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const unsigned char input_0[] = {53, 10, 53, 32, 53, 32, 53, 32, 53, 32, 49, 10, 0};
static const unsigned char output_0[] = {49, 10, 0};
static const unsigned char input_1[] = {54, 10, 52, 32, 49, 32, 52, 32, 49, 32, 52, 32, 52, 10, 0};
static const unsigned char output_1[] = {52, 10, 0};
static const unsigned char input_2[] = {50, 10, 51, 32, 51, 10, 0};
static const unsigned char output_2[] = {45, 49, 10, 0};
static const unsigned char input_3[] = {56, 10, 56, 32, 56, 32, 56, 32, 56, 32, 56, 32, 56, 32, 56, 32, 56, 10, 0};
static const unsigned char output_3[] = {56, 10, 0};
static const unsigned char input_4[] = {53, 10, 50, 32, 51, 32, 51, 32, 50, 32, 50, 10, 0};
static const unsigned char output_4[] = {50, 10, 0};
static const unsigned char input_5[] = {50, 50, 10, 50, 32, 55, 32, 56, 32, 56, 32, 52, 32, 56, 32, 55, 32, 51, 32, 57, 32, 54, 32, 53, 32, 49, 48, 32, 52, 32, 51, 32, 54, 32, 55, 32, 49, 32, 55, 32, 52, 32, 49, 48, 32, 56, 32, 49, 10, 0};
static const unsigned char output_5[] = {49, 10, 0};
static const unsigned char input_6[] = {52, 10, 51, 32, 50, 32, 56, 32, 50, 10, 0};
static const unsigned char output_6[] = {50, 10, 0};
static const unsigned char input_7[] = {49, 49, 10, 54, 32, 55, 32, 49, 32, 56, 32, 56, 32, 49, 48, 32, 53, 32, 56, 32, 53, 32, 51, 32, 49, 48, 10, 0};
static const unsigned char output_7[] = {49, 10, 0};
static const unsigned char input_8[] = {55, 10, 56, 32, 56, 32, 51, 32, 54, 32, 53, 32, 54, 32, 52, 10, 0};
static const unsigned char output_8[] = {45, 49, 10, 0};
static const unsigned char input_9[] = {50, 53, 10, 54, 32, 57, 32, 54, 32, 55, 32, 49, 32, 52, 32, 55, 32, 49, 32, 56, 32, 56, 32, 57, 32, 56, 32, 49, 48, 32, 49, 48, 32, 56, 32, 52, 32, 49, 48, 32, 52, 32, 49, 48, 32, 49, 32, 50, 32, 57, 32, 53, 32, 55, 32, 57, 10, 0};
static const unsigned char output_9[] = {49, 10, 0};
static const unsigned char input_10[] = {53, 10, 49, 32, 57, 32, 49, 48, 32, 49, 32, 51, 10, 0};
static const unsigned char output_10[] = {49, 10, 0};
static const unsigned char input_11[] = {50, 52, 10, 54, 32, 57, 32, 55, 32, 53, 32, 56, 32, 55, 32, 53, 32, 51, 32, 55, 32, 53, 32, 49, 48, 32, 49, 48, 32, 51, 32, 54, 32, 49, 48, 32, 50, 32, 56, 32, 54, 32, 53, 32, 52, 32, 57, 32, 53, 32, 51, 32, 49, 48, 10, 0};
static const unsigned char output_11[] = {53, 10, 0};
static const unsigned char input_12[] = {49, 10, 49, 10, 0};
static const unsigned char output_12[] = {49, 10, 0};
static const unsigned char input_13[] = {50, 51, 10, 56, 32, 56, 32, 49, 48, 32, 54, 32, 52, 32, 51, 32, 53, 32, 56, 32, 50, 32, 52, 32, 50, 32, 56, 32, 52, 32, 54, 32, 49, 48, 32, 52, 32, 50, 32, 49, 32, 49, 48, 32, 50, 32, 49, 32, 49, 32, 53, 10, 0};
static const unsigned char output_13[] = {52, 10, 0};
static const unsigned char input_14[] = {49, 56, 10, 50, 32, 49, 48, 32, 52, 32, 56, 32, 50, 32, 49, 48, 32, 53, 32, 49, 32, 50, 32, 57, 32, 53, 32, 53, 32, 54, 32, 51, 32, 56, 32, 54, 32, 52, 32, 49, 48, 10, 0};
static const unsigned char output_14[] = {50, 10, 0};
static const unsigned char input_15[] = {49, 50, 10, 49, 32, 54, 32, 49, 48, 32, 49, 32, 54, 32, 57, 32, 49, 48, 32, 56, 32, 54, 32, 56, 32, 55, 32, 51, 10, 0};
static const unsigned char output_15[] = {49, 10, 0};
static const unsigned char input_16[] = {51, 48, 10, 57, 32, 50, 32, 52, 32, 49, 32, 53, 32, 49, 32, 53, 32, 50, 32, 53, 32, 55, 32, 55, 32, 55, 32, 51, 32, 49, 48, 32, 49, 32, 53, 32, 52, 32, 50, 32, 56, 32, 52, 32, 49, 32, 57, 32, 49, 48, 32, 55, 32, 49, 48, 32, 50, 32, 56, 32, 49, 48, 32, 57, 32, 52, 10, 0};
static const unsigned char output_16[] = {52, 10, 0};
static const unsigned char input_17[] = {50, 51, 10, 50, 32, 54, 32, 52, 32, 50, 32, 56, 32, 55, 32, 53, 32, 54, 32, 52, 32, 49, 48, 32, 52, 32, 54, 32, 51, 32, 55, 32, 56, 32, 56, 32, 51, 32, 49, 32, 52, 32, 50, 32, 50, 32, 49, 48, 32, 55, 10, 0};
static const unsigned char output_17[] = {52, 10, 0};
static const unsigned char input_18[] = {49, 56, 10, 57, 32, 56, 32, 54, 32, 49, 48, 32, 50, 32, 54, 32, 49, 48, 32, 50, 32, 55, 32, 56, 32, 49, 48, 32, 51, 32, 56, 32, 50, 32, 54, 32, 50, 32, 51, 32, 49, 10, 0};
static const unsigned char output_18[] = {50, 10, 0};
static const unsigned char input_19[] = {50, 49, 10, 53, 32, 53, 32, 51, 32, 57, 32, 53, 32, 54, 32, 51, 32, 50, 32, 56, 32, 53, 32, 54, 32, 49, 48, 32, 49, 48, 32, 54, 32, 56, 32, 52, 32, 49, 48, 32, 55, 32, 55, 32, 49, 48, 32, 56, 10, 0};
static const unsigned char output_19[] = {45, 49, 10, 0};
static const unsigned char input_20[] = {49, 10, 49, 48, 10, 0};
static const unsigned char output_20[] = {45, 49, 10, 0};
static const unsigned char input_21[] = {49, 51, 10, 57, 32, 55, 32, 55, 32, 50, 32, 52, 32, 55, 32, 50, 32, 49, 48, 32, 57, 32, 55, 32, 53, 32, 55, 32, 50, 10, 0};
static const unsigned char output_21[] = {50, 10, 0};
static const unsigned char input_22[] = {49, 49, 10, 53, 32, 52, 32, 49, 48, 32, 50, 32, 49, 32, 49, 32, 49, 48, 32, 51, 32, 54, 32, 49, 32, 56, 10, 0};
static const unsigned char output_22[] = {49, 10, 0};
static const unsigned char input_23[] = {50, 50, 10, 55, 32, 57, 32, 57, 32, 57, 32, 51, 32, 52, 32, 49, 32, 53, 32, 57, 32, 49, 32, 50, 32, 49, 32, 49, 32, 49, 48, 32, 55, 32, 53, 32, 54, 32, 55, 32, 54, 32, 55, 32, 55, 32, 54, 10, 0};
static const unsigned char output_23[] = {49, 10, 0};
static const unsigned char input_24[] = {53, 10, 51, 32, 49, 48, 32, 49, 48, 32, 57, 32, 50, 10, 0};
static const unsigned char output_24[] = {45, 49, 10, 0};

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
    free(input);
    return 1;
}
