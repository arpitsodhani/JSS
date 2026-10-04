#include <stdio.h>
#include <string.h>

int validate_filename(char* file_name) {
    int len = strlen(file_name);
    if (len < 5) return 0;
    
    // Check first char is letter
    if (!((file_name[0] >= 'a' && file_name[0] <= 'z') || (file_name[0] >= 'A' && file_name[0] <= 'Z'))) {
        return 0;
    }
    
    // Count digits
    int digit_count = 0;
    int dot_pos = -1;
    for (int i = 0; i < len; i++) {
        if (file_name[i] >= '0' && file_name[i] <= '9') {
            digit_count++;
        }
        if (file_name[i] == '.') {
            dot_pos = i;
        }
    }
    
    if (digit_count > 3) return 0;
    if (dot_pos == -1) return 0;
    
    // Check extension
    char* ext = file_name + dot_pos + 1;
    if (strcmp(ext, "txt") == 0 || strcmp(ext, "exe") == 0 || strcmp(ext, "dll") == 0) {
        return 1;
    }
    
    return 0;
}

int main() {
    char file_name[1000];
    scanf("%s", file_name);
    
    if (validate_filename(file_name)) {
        printf("Yes\n");
    } else {
        printf("No\n");
    }
    
    return 0;
}
