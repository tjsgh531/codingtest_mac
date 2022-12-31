#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> queue1, vector<int> queue2) {
    long long answer = 0;
    long long sum1 = 0, sum2 = 0;
    int k = queue1.size() * 2;

    for (int i = 0; i < queue1.size(); i++) {
        sum1 += queue1[i];
    }
    for (int i = 0; i < queue2.size(); i++) {
        sum2 += queue2[i];
    }

    while (k--) {
        if (sum1 > sum2) {
            sum1 -= queue1.front();
            sum2 += queue1.front();
            queue2.push_back(queue1.front());
            queue1.erase(queue1.begin());
            answer++;
        }
        else if (sum1 < sum2) {
            sum2 -= queue2.front();
            sum1 += queue2.front();
            queue1.push_back(queue2.front());
            queue2.erase(queue2.begin());
            answer++;
        }
        else
            break;
    }
    if (sum1 != sum2) {
        return -1;
    }
    return answer;
}

int main(void){
    vector<int> v;
    v.push_back(3);
    v.push_back(3);
    v.push_back(3);
    v.push_back(3);

    vector<int> v2;
    v2.push_back(3);
    v2.push_back(3);
    v2.push_back(21);
    v2.push_back(3);
    int answer = solution(v, v2);
    cout << answer;
    return 0;
}