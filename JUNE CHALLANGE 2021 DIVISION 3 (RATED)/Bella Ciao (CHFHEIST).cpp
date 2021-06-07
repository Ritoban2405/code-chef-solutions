//PROBLEM STATEMENT -https://www.codechef.com/JUNE21C/problems/CHFHEIST

#include <iostream>
using namespace std;
#define ll long int

int main() 
{
    ll tc;
    cin >> tc;
    while (tc--) 
	{
        ll D, d, p, Q, ans = 0;
        cin >> D >> d >> p >> Q;
        ll remain = D % d;
        ll times = (D / d);
        ans = (times*p*d) + d*Q * (times*(times-1)/2) + (p*remain+(remain*Q*times));
        cout << ans << endl;
    }
    return 0;
}
