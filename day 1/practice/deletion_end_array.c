#include<stdio.h>

int main()

{

int n,array[10];

printf("enter the size of an array");

scanf("%d" ,&n);

printf("enter elements in an array");

for(int i=0;i<n;i++)

scanf("%d", &array[i]);

printf("\nafter deletion array elements are");

for(int i=0;i<n-1;i++)

printf("\n%d" , array[i]);

}


