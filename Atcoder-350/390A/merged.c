#include <stdio.h>

void read_input(int *a) {
for(int i=0;i<5;i++) scanf("%d", &a[i]);
}

int check_swap(int *a) {
int b[5]; for(int i=0;i<5;i++) b[i]=a[i];
for(int i=0;i<4;i++){
  int tmp=b[i]; b[i]=b[i+1]; b[i+1]=tmp;
  int ok=1; for(int j=0;j<5;j++) if(b[j]!=j+1) ok=0; if(ok) return 1;
  tmp=b[i]; b[i]=b[i+1]; b[i+1]=tmp;
}
return 0;
}

void print_yesno(int x) {
printf("%s\n", x?"Yes":"No");
}

int main(void){ int a[5]; read_input(a); int ok=check_swap(a); print_yesno(ok); return 0;}
