#include<stdio.h>
int main()
{
   
int pid[10],bt[10];
int n;

printf("Enter the no of processes\n");
scanf("%d",&n);

printf("Enter the process id\n");
for (int i = 0; i < n; i++)
{
scanf("%d",&pid[i]);
}

printf("Enter the burst time\n");
for (int i = 0; i < n; i++)
{
   scanf("%d",&bt[i]);
}

int i,wt[n];
wt[0]=0;
for (int i = 1; i < n; i++)
{
    wt[i]=wt[i-1]+bt[i-1];
}

float twt=0.0;
float tat=0.0;

printf("process id      burst time      waiting time      turn around time\n");
for (int i = 0; i < n; i++)
{
   printf("%d\t\t",pid[i]);
   printf("%d\t\t",bt[i]);
   printf("%d\t\t",wt[i]);
   printf("%d\t\t",wt[i]+bt[i]);
printf("\n");

   twt+=wt[i];
   tat+=wt[i]+bt[i];

}

float att,awt;

att=tat/n;
awt=twt/n;

printf("average waiting time is %.2f\n",awt);
printf("average turn around time is %.2f\n",att);

return 0;
}