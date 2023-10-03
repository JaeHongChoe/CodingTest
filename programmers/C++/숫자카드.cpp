#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m, temp;

    cin >> n;

    vector<int> ans(n);

    for(int i=0; i<n; i++){
        cin >> ans[i];
    }

    sort(ans.begin(), ans.end());

    cin >> m;

    for(int i=0; i<m; i++){
        int cnt =0;
        cin >> temp;
        auto range = equal_range(ans.begin(), ans.end(), temp);
        for (auto iter = range.first; iter != range.second; ++iter)
		    cnt++;
        cout << cnt << " ";
        // cout << count(ans.begin(), ans.end(), temp) << ' '; 시간초과
    }

    return 0;
}
