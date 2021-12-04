#include <stdio.h>
 
 
int main () {

   int i = 20;
   int *p;
   
   p=&i;
   
   
   printf("Value of i : %d\n", i );
   printf("Value of *p : %d\n", *p );
   printf("Value of i : %d\n", &i );
   printf("Value of p : %d\n", p );
   printf("Value of &p : %d\n", &p );
   
  
   
}

