/*
    Hollow Square Pattern : 
    For n=6,

    * * * * * * 
    *         *
    *         *
    *         *
    *         *
    * * * * * *
*/
#include <iostream>
using namespace std;

int main() {
    int n;

    cout<<"Enter the value of n : ";
    cin>>n;

    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(j==0 || i==0 || j==(n-1) || i==(n-1))
            cout<<"* ";
            else
            cout<<"  ";
        }
        cout<<endl;
    }
    return 0;
}