#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	int x;
	x = 10;
	int y = 20;
	
	printf("Introduce un numero entero: ");
	scanf("%d",&y);
	
	printf("\n X vale: %d , Y vale: %d", x,y);
	
	if(y>10){
		printf("\nEl numero mayor es %d",y);
	}
	if(y<10){
		printf("\nEl numero mayor es %d",x);
	}
	if(y>10){
		printf("\nEl numero %d es mayor que 10. ",y);
	}
	else{
		printf("\nEl numero %d es menor que 10. ",y);	
	}
	 
}

