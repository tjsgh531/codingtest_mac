#include<bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, temp;
    queue<int> q;

    cin >> N;
    for(int i =1; i <=N; i++) q.push(i);

    while(q.size() >1){
        q.pop();
        temp = q.front();
        q.push(temp);
        q.pop();
    }
    cout << q.front();

    return 0;
}