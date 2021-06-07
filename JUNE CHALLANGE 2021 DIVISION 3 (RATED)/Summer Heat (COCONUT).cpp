//problem statement - https://www.codechef.com/JUNE21C/problems/COCONUT


#include <iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int a,b,c,d,res=0;
        cin>>a>>b>>c>>d;
        res=(c/a+d/b);
        cout<<res<<endl;
    }
}
