#include <stdio.h>
#include <string.h>

int get_beat_value(char* note) {
    if (strcmp(note, "o") == 0) return 4;
    if (strcmp(note, "o|") == 0) return 2;
    if (strcmp(note, ".|") == 0) return 1;
    return 0;
}

int main(void) {
    char line[10000];
    fgets(line, sizeof(line), stdin);
    char* token = strtok(line, " \n");
    int first = 1;
    while (token) {
        if (!first) printf(" ");
        printf("%d", get_beat_value(token));
        first = 0;
        token = strtok(NULL, " \n");
    }
    printf("\n");
    return 0;
}
