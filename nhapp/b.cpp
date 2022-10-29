#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef double db;
//by KMA dil and man
void exam(int i, int* p, int& r){
    cout<<i<<" "<<*p<<" "<<r<<endl;
    p = &r;
    r++;
    *p = i;
}
int main()
{
    int arr[4] {20,22};
    // int *q {arr};
    // exam(arr[2], q, arr[1]);
    // cout<<endl;
    // cout<<*q<<" "<<arr[0]<<" "<<arr[1]<<" "<<arr[2];
    cout<<arr[0]<<" "<<arr[1]<<" "<<arr[2]<<" "<<arr[3];
    return 0;
}