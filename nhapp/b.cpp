#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a=5000;
    int N;
    int T;
    while(true){
        cout<<"nhap so to tien be An nhan: ";
        cin>>N;
        if(N<=200)
            break;
        cout<<"so to tien phai nho hon hoac bang 200"<<endl;
    } 
    T=N*5000;
    cout<<"so tien be An nhan duoc la: "<<T; 
    return 0;
}