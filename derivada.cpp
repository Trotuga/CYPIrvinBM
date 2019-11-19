#include <stdio.h>
#include <stdlib.h>
#include <locale.h> 

int ConfiguraIdioma()
{  
	struct lconv *lcPtr;
	setlocale(LC_ALL, "spanish");
	lcPtr = localeconv();

	lcPtr->decimal_point = ".";
	lcPtr->thousands_sep = ",";
	lcPtr->grouping = "3";
		
}

int portada()
{
	ConfiguraIdioma();
	printf("\t\t Programa que obtenga la derivada de un polinomio de grado n  \n\n");
	printf("\tIntegrantes del equipo\n");
		printf("\n\t1.-Baez Mendez Irvin\n\n");
		printf("\t2.-Sagrero Granados Alonso\n\n");
		printf("\t3.-Torres Martinez Ramon Jair\n\n");
		printf("\t4.-Felix Diaz Amaury\n\n");
		printf("\t5.-Lulis NOvia de alonso \n\n");
}
int main()
{
	portada();
	
    int i, e[20], num[20], n;
    char var[20], sr[20], p;
    system("Color F0");
    printf("Derivada de polinomios\n\n");
    printf("Cuantos terminos tendra?: ");
    scanf("%d",&n);
    printf("Escriba una variable elevada a alguna potencia.\n");
    printf("(numero)(literal)(potencia)(numero). \n\nEj.: -5x^4\n");

    for(i=0;i<n;i++)
    {
        printf("Dato %i: ", i+1);
        scanf("%d%c%c%d",&num[i],&var[i],&p,&e[i]);
    }

    printf("La derivada es: ");
    num[0]*=e[0];
    e[0]-=1;
    printf("%d%c%c%d",num[0],var[0],p,e[0]);
    for(i=1;i<n;i++)
    {
        if(num[i]>=0)
            printf("+");
        num[i]*=e[i];
        e[i]-=1;
        printf("%d%c%c%d",num[i],var[i],p,e[i]);
    }
    printf("\n\n");
    system("Pause");
}
