#include <stdio.h>
#include <string.h>

int validate_date(char* date) {
    if (strlen(date) != 10) return 0;
    if (date[2] != '-' || date[5] != '-') return 0;
    
    int month = (date[0] - '0') * 10 + (date[1] - '0');
    int day = (date[3] - '0') * 10 + (date[4] - '0');
    int year = (date[6] - '0') * 1000 + (date[7] - '0') * 100 + (date[8] - '0') * 10 + (date[9] - '0');
    
    if (month < 1 || month > 12) return 0;
    if (day < 1) return 0;
    
    int days_in_month[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    if (day > days_in_month[month - 1]) return 0;
    
    return 1;
}

int main() {
    char date[100];
    scanf("%s", date);
    
    if (validate_date(date)) {
        printf("True\n");
    } else {
        printf("False\n");
    }
    
    return 0;
}
