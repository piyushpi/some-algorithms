#include <iostream>
#include <conio.h>

// O(N^2)

using namespace std;

int main()
{
    int cost[5] = {1,2,4,5,6};
    int gas[5] = {0,5,5,5,6};
    int tank = 0;

    int l = sizeof(cost)/sizeof(cost[0]);

    int start = 0;

    for (start=0; start<l; start++)
    {
        cout<<"starting at "<<start<<endl;

        int circuit = 0;
        int a = 0;
        
        for (int i=0; i<l; i++)
        {
            circuit += 1;
            if ((i+start) >= l)
            {
                cout<<"warping"<<endl;
                a = (i+start) - l;
                tank += gas[a] - cost[a];
            }
            else
            {
                a = i+start;
                tank += gas[a] - cost[a];
            }

            if (tank < 1)
            {
                cout<<"tank empty at "<<i<<endl;
                break;
            }
            else
            {
                // cout<<tank<<endl;
                cout<<gas[a]<<endl;
            }

            if (circuit+1 == l)
            {
                cout<<"possible from "<<start<<endl;
                break;
            }

            // for (int j=0; j<l; j++)
            // {
            // }
        }
        cout<<"---------"<<endl;
    }

    return 0;
}