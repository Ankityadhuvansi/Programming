// WAP to impleament FCFS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
void main()
{
    int n, i, j, k, temp, temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8, temp9, temp10;
    int at[10], bt[10], ct[10], tat[10], wt[10], p[10];
    float awt = 0, atat = 0;
    printf("Enter the number of processes: ");
    scanf("%d", &n);
    printf("Enter the arrival time and burst time of the processes:\n");
    for (i = 0; i < n; i++)
    {
        printf("Arrival time of process %d: ", i + 1);
        scanf("%d", &at[i]);
        printf("Burst time of process %d: ", i + 1);
        scanf("%d", &bt[i]);
        p[i] = i + 1;
    }
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < (n - i - 1); j++)
        {
            if (at[j] > at[j + 1])
            {
                temp = at[j];
                at[j] = at[j + 1];
                at[j + 1] = temp;
                temp1 = bt[j];
                bt[j] = bt[j + 1];
                bt[j + 1] = temp1;
                temp2 = p[j];
                p[j] = p[j + 1];
                p[j + 1] = temp2;
            }
        }
    }
    for (i = 0; i < n; i++)
    {
        if (i == 0)
        {
            ct[i] = at[i] + bt[i];
        }
        else
        {
            if (at[i] > ct[i - 1])
            {
                ct[i] = at[i] + bt[i];
            }
            else
            {
                ct[i] = ct[i - 1] + bt[i];
            }
        }
        tat[i] = ct[i] - at[i];
        wt[i] = tat[i] - bt[i];
        awt += wt[i];
        atat += tat[i];
    }
    awt = awt / n;
    atat = atat / n;
    printf("\nProcess\tArrival time\tBurst time\tCompletion time\tTurnaround time\tWaiting time\n");
}
