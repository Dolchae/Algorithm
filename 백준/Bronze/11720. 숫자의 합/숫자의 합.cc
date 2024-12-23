#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int n;
    int sum = 0;
    cin >> n;
    string a;
    cin >> a;


    for(int i=0; i<n; i++){
        sum += (a[i]-48);
    }

    cout << sum;

    return 0;
}
