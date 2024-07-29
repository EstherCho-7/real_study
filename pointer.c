#include <stdio.h>
#include <string.h>
void swap(char* str, int len) {
	char v;
	char* fr=str;
	char* ed=str+len-1;
	while (fr<ed) {
		v= *fr;
		*fr= *ed;
		*ed =v;
		fr++;
		ed--;
	}
}
void main(){
	char str[10]="ABCDEFGH";
	int len = strlen(str);
	swap(str, len);
	for (int i=1; i<len; i+=1){
		printf("%c", str[i]);
	}

	printf("\n");

	int a[3][2]={{1,2},{3,4},{5,6}};
       	printf("%d\n", **a);
	printf("%d\n", **a+1);
        printf("%d\n", **a+2);
}
