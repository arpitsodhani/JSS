#include <stdio.h>
#include <string.h>

int word_to_number(char* word) {
    if (strcmp(word, "zero") == 0) return 0;
    if (strcmp(word, "one") == 0) return 1;
    if (strcmp(word, "two") == 0) return 2;
    if (strcmp(word, "three") == 0) return 3;
    if (strcmp(word, "four") == 0) return 4;
    if (strcmp(word, "five") == 0) return 5;
    if (strcmp(word, "six") == 0) return 6;
    if (strcmp(word, "seven") == 0) return 7;
    if (strcmp(word, "eight") == 0) return 8;
    if (strcmp(word, "nine") == 0) return 9;
    return -1;
}

int main(void) {
    char line[10000];
    fgets(line, sizeof(line), stdin);
    int nums[100], count = 0;
    char* token = strtok(line, " \n");
    while (token) {
        nums[count++] = word_to_number(token);
        token = strtok(NULL, " \n");
    }
    for (int i = 0; i < count - 1; i++) {
        for (int j = i + 1; j < count; j++) {
            if (nums[i] > nums[j]) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
    }
    char* words[] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    for (int i = 0; i < count; i++) {
        if (i > 0) printf(" ");
        printf("%s", words[nums[i]]);
    }
    printf("\n");
    return 0;
}
