#include <stdio.h>
int main()
{	int yn;
	scanf("%d", &yn);
	if (yn % 4 == 0 && yn % 100 != 0 || yn % 400 == 0)
		printf("1\n");
	else
		printf("0\n");
	return 0;}
