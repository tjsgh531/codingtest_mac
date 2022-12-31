#include<bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N,height,ans = 0;
    cin >> N;
    stack< pair<int, int> > s;
    for(int i = 0; i < N; i++){
        cin >> height;
        while(!s.empty() && s.top().first < height){
            s.pop();
        }
        s.push( make_pair(height, i));
        if(s.empty()) ans += i;
        else ans += (i- s.top().second);
    }
    cout << ans;

    return 0;
}