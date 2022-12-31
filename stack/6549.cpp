#include<bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    while(1){
        int n;
        cin >> n;
        if(n == 0) break;
        stack<pair<int, int>> s;
        long long ans = 0;
        for(int i =0; i< n; i++){
            int h;
            cin >> h;
            int idx = i;
            while(!s.empty() && s.top().X >= h){
                ans = max(ans, 1LL * (i- s.top().Y) * s.top().X);
                idx = s.top().Y;
                s.pop();
            }
            s.push({h, idx});
        }
        while(!s.empty()){
            ans = max(ans, 1LL * (n - s.top().Y) * s.top().X);
            s.pop();
        }
        cout << ans << '\n';
    }

    return 0;
}

// 1LL => '숫자 1을 LL(long long)형태로 나타내겠습니다'를 의미
// cout << 1000000 * 10000000 * 1LL 
// => error: 연산 우선순서에 따라 int * int 가 먼저 실행 되어 error발생

// cout << 1LL * 1000000 * 1000000
// => correct  