#include <string>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

int main(){

    int n, m;

    cin >> n;
    
    vector<int> answer(n), temp(n);

    for(int i =0; i<n; i++){
        cin >> answer[i];
    }

    cin >> m;

    vector<int> real(m), result(m);

    for(int i =0; i<m; i++){
        cin >> real[i];
    }    

    temp = real;

    sort(answer.begin(), answer.end());
    sort(real.begin(), real.end());

    
    auto eIter = set_intersection(real.begin(), real.end(), answer.begin(), answer.end(), result.begin());
    
    result.erase(eIter, result.end());
    
    for (int i=0; i<temp.size(); i++){
        auto it = find(result.begin(), result.end(), temp[i]);
        if ( it != result.end()){
            cout << 1 << '\n';
        }else{
            cout << 0 << '\n';
        }
    }
    return 0;
}
