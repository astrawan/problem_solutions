#include <stdio.h>
int main()
{
    int n,temp;
    scanf("%d",&n);
    for (int i=0;i < n;i++){
        scanf("%d",&temp);
        printf("%d is %s\n",temp,temp%2 ? "odd":"even");
    }
}