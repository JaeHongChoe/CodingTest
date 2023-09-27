#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    vector<string> ans(20);
    
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    
    auto eIter = set_difference(participant.begin(), participant.end(), completion.begin(), completion.end(), ans.begin());
    ans.erase(eIter, ans.end());
    
    return ans[0];
}
