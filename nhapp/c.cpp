#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a;
    int x;
    cout<<"nhap a: ";
    cin>>a;
    cout<<"nhap x: ";
    cin>>x;
    float Kq = a*x*x + sqrt(x);
    float kQ = a*pow(x, 2) +sqrt(x);
    cout<<"Ket qua la: ";
    cout<<Kq<<" "<<kQ; 
    
    return 0;
}