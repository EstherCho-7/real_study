#include <stdio.h>
int main(){
	int a[3][2]={{1,2},{3,4},{5,6}};
	printf("%d\n", **a);
	printf("%d\n", **a+1);
	printf("%d\n", **a+2);
}
