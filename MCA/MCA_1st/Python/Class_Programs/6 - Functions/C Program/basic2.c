#include <stdio.h>
 
 
int main () {

   int i = 20;
   int *p, *q;
   
   p=&i;
   q=p;
   
   
   
   printf("Value of i : %d\n", i );
   printf("Value of *p : %d\n", *p );
   printf("Value of *q : %d\n", *q );
   *q = 40;
    printf("Value of i : %d\n", i );
   printf("Value of *p : %d\n", *p );
   printf("Value of *q : %d\n", *q );
   
  
   
}

