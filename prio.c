#include<stdio.h>

void bubblesort(int bt[],int n,int pid[],int pr[]){
    for (int i = 0; i < n-1; i++)
    {
        int temp,p,x;
        for (int j = 0; j < n-i-1; j++)
        {
            if (pr[j]>pr[j+1])
            {
               x=pr[j+1];
               pr[j+1]=pr[j];
               pr[j]=x;

               temp =bt[j+1];
               bt[j+1]=bt[j];
               bt[j]=temp;

               p=pid[j+1];
               pid[j+1]=pid[j];
               pid[j]=p;
            }
            
        }
        
    }
    
}

int main()
{
int pid[10],bt[10],pr[10];
int n;
printf("Enter the no of processes\n");
scanf("%d",&n);
printf("Enter the process id\n");
for (int i = 0; i < n; i++)
{
scanf("%d",&pid[i]);
}
printf("Enter the burst time and priority\n");
for (int i = 0; i < n; i++)
{
   scanf("%d %d",&bt[i],&pr[i]);
}
bubblesort(bt,n,pid,pr);
int i,wt[n];
wt[0]=0;
for (int i = 1; i < n; i++)
{
    wt[i]=wt[i-1]+bt[i-1];
}
float twt=0.0;
float tat=0.0;
printf("process id      burst time    priority     waiting time      turn around time\n");
for (int i = 0; i < n; i++)
{
   printf("%d\t\t",pid[i]);
   printf("%d\t\t",bt[i]);
   printf("%d\t\t",pr[i]);
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