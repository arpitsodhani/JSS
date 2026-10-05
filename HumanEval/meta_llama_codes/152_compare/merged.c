

#include <stdio.h>
#include <stdlib.h>
int main() {
    int n; scanf("%d", &n);
    int game[100], guess[100];
    for(int i=0; i<n; i++) scanf("%d", &game[i]);
    for(int i=0; i<n; i++) scanf("%d", &guess[i]);
    for(int i=0; i<n; i++) printf("%d%c", abs(game[i]-guess[i]), i<n-1?' ':'\\n');
    return 0;
}
