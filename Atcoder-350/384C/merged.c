#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_input(int *a,int *b,int *c,int *d,int *e){ scanf("%d%d%d%d%d", a,b,c,d,e); }

void list_participants(int a,int b,int c,int d,int e){
    const char *names = "ABCDE";
    int score[32];
    char label[32][6];
    int cnt=0;
    int vals[5]={a,b,c,d,e};
    for(int mask=1; mask<32; mask++){
        int sum=0, len=0;
        for(int i=0;i<5;i++){
            if(mask>>i & 1){ sum+=vals[i]; label[cnt][len++]=names[i]; }
        }
        label[cnt][len]='\0';
        score[cnt]=sum;
        cnt++;
    }
    for(int i=0;i<cnt;i++){
        for(int j=i+1;j<cnt;j++){
            if(score[j]>score[i] || (score[j]==score[i] && strcmp(label[j],label[i])<0)){
                int ts=score[i]; score[i]=score[j]; score[j]=ts;
                char tmp[6]; strcpy(tmp,label[i]); strcpy(label[i],label[j]); strcpy(label[j],tmp);
            }
        }
    }
    for(int i=0;i<cnt;i++) printf("%s\n", label[i]);
}

void print_answer(void){ }

int main(void){ int a,b,c,d,e; read_input(&a,&b,&c,&d,&e); list_participants(a,b,c,d,e); return 0; }
