#include<bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N,height;
    long long ans = 0;
    cin >> N;
    stack<pair<int,int>> s;
    int dp[N];
    
    for(int i = 0; i < N; i++ ){
        cin >> height;
        int temp = 0;
        if(!s.empty()) temp++;
        while(!s.empty() && s.top().first <= height){
            if(s.top().first == height){
                temp += dp[s.top().second];
                break;
            }
            s.pop();
            if(!s.empty()) temp++;
        }
        s.push({height,i});
        dp[i] = temp;
        ans += temp;
    }
    cout << ans;
}