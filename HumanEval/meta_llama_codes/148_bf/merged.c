#include <stdio.h>
#include <string.h>

void get_planets_between(char* planet1, char* planet2, char result[][20], int* result_len) {
    char* planets[] = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    int p1_idx = -1, p2_idx = -1;
    
    for (int i = 0; i < 8; i++) {
        if (strcmp(planets[i], planet1) == 0) p1_idx = i;
        if (strcmp(planets[i], planet2) == 0) p2_idx = i;
    }
    
    *result_len = 0;
    if (p1_idx == -1 || p2_idx == -1) return;
    
    int start = (p1_idx < p2_idx) ? p1_idx : p2_idx;
    int end = (p1_idx > p2_idx) ? p1_idx : p2_idx;
    
    for (int i = start + 1; i < end; i++) {
        strcpy(result[*result_len], planets[i]);
        (*result_len)++;
    }
}

int main() {
    char planet1[20], planet2[20];
    scanf("%s %s", planet1, planet2);
    
    char result[10][20];
    int result_len;
    get_planets_between(planet1, planet2, result, &result_len);
    
    printf("(");
    for (int i = 0; i < result_len; i++) {
        if (i > 0) printf(", ");
        printf("\"%s\"", result[i]);
    }
    printf(")\n");
    
    return 0;
}
