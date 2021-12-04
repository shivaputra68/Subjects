#include<stdio.h>
int Fact(int a)
{
	if (a==0 || a ==1)
	{
		return 1;
	}
	else
	{		
	
		return (a*Fact(a-1));
	}
}
int main()
{
	
	int a, fa;
	printf("Enter yhe Value \n");
	scanf("%d",&a);
	printf("Factorial Program\n");
	fa = Fact(a);
	printf("The Factorial of %d ===> %d\n", a, fa);

	
}

