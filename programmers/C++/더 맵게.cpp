#include <string>
#include <vector>
#include <functional>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer, l, r;
    int cnt = 0;
    
    priority_queue<int> sco;
    
    for(int n : scoville){
        sco.push(n*-1);
    }
    
    while(sco.empty() == 0){

        l = sco.top(); 
        sco.pop();
        
        if (l <= -1*K){
            return cnt;
        }else if(sco.size() == 0){ // -1 상황에서 오류 방지
            return -1;
        }
        r = sco.top();
        sco.pop();
        sco.push((l + (r*2)));
        cnt++;
    }
    
    return -1;
}
