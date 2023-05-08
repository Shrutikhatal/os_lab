#include <stdio.h>

int main()
{
    int n, quantum;
    printf("Enter number of processes: ");
    scanf("%d", &n);
    printf("Enter time quantum: ");
    scanf("%d", &quantum);

    int AT[n], BT[n], TAT[n], WT[n], RT[n];
    int remaining_time[n];
    int time = 0, total_waiting_time = 0, total_turnaround_time = 0;

    // Input arrival and burst time for each process
    for (int i = 0; i < n; i++)
    {
        printf("Enter arrival time and burst time for process %d: ", i+1);
        scanf("%d %d", &AT[i], &BT[i]);
        remaining_time[i] = BT[i];
    }

    // Round Robin scheduling
    while (1)
    {
        int all_processes_completed = 1;

        for (int i = 0; i < n; i++)
        {
            if (remaining_time[i] > 0)
            {
                all_processes_completed = 0;

                if (remaining_time[i] > quantum)
                {
                    time += quantum;
                    remaining_time[i] -= quantum;
                }
                else
                {
                    time += remaining_time[i];
                    WT[i] = time - AT[i] - BT[i];
                    remaining_time[i] = 0;
                    TAT[i] = time - AT[i];
                    RT[i] = TAT[i] - BT[i];
                    total_waiting_time += WT[i];
                    total_turnaround_time += TAT[i];
                }
            }
        }

        if (all_processes_completed)
            break;
    }

    // Print the results
    printf("Process  AT  BT  TAT  WT  RT\n");
    for (int i = 0; i < n; i++)
    {
        printf("%d\t%d\t%d\t%d\t%d\t%d\n", i+1, AT[i], BT[i], TAT[i], WT[i], RT[i]);
    }

    printf("Average waiting time: %.2f\n", (float) total_waiting_time / n);
    printf("Average turnaround time: %.2f\n", (float) total_turnaround_time / n);

    return 0;
}
