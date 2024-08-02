#include <stdio.h>

int main(){
	int num;
	printf("choose number(1~4):");

	if (scanf("%d", &num) != 1) {
        while (getchar() != '\n');
        printf("Invalid input\n");
        return 0;
	}

	if (num>4 || num<1) {
		printf("Wrong Number"); 
		return 0;
	}
	else
		switch(num) {
			case 1:
				printf("You chose 1");
				break;
			case 2:
				printf("You chose 2");
                                break;
			case 3:
				printf("You chose 3");
                                break;
			case 4:
				printf("You chose 4");
                                break;
		}
	return 0;
}
