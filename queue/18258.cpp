#include<bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, temp;
    string order;
    queue<int> q;

    cin >> N;
    for(int i =0; i<N; i++){
        cin >> order;
        if(order =="push"){
            cin >> temp;
            q.push(temp);
        }
        else if(order =="pop"){
            if(q.empty()) cout << -1 <<"\n";
            else {
                cout << q.front() << "\n";
                q.pop();
            }
        }
        else if(order == "size") cout << q.size() << "\n";
        else if(order == "empty"){
            if(q.empty()) cout << 1 << "\n";
            else cout << 0 << "\n";
        }
        else if(order == "front"){
            if(q.empty()) cout << -1 << "\n";
            else cout << q.front() << "\n";
        }
        else{
            if(q.empty()) cout << -1 << "\n";
            else cout << q.back() << "\n";
        }
    }
    return 0;
}