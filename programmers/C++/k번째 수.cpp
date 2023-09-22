#include <string>
#include <vector>
#include<algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    int a = commands.size();
    vector<int> answer;
    
    for(int i=0; i < a; i++){
        vector<int> v;
        int l = commands[i][0];
        int r = commands[i][1];
        int k = commands[i][2];
        
        for(int j=l-1; j<r; j++){
            v.push_back(array[j]);
        }
        sort(v.begin(), v.end());
        answer.push_back(v[k-1]);
            
    }
    
    return answer;
}
