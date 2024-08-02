#include <stdio.h>

int main(){
int j, i, k;
for (j=1; j<9; j+=3){
for (i=1; i<=9; ++i){
for (k=j; k<=j+2; k++)
printf("%d X %d = %2d\t", k, i, k*i);
printf("\n");
}
printf("\n");
}
printf("\n");
}
