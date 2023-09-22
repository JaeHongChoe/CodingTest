#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

int main(){
    deque<int> d; 
    int n, many, which;
    int cnt = 0;
    int where;
    cin >> n >> many;

    for(int i = 1; i<n+1; i++){
        d.push_back(i);
    }

    while(many--){
        cin >> which;
        
        for (int k=0; k<d.size(); k++){
            if (d[k] == which){
                where = k;
            }
        }

        if(d.size()-where > where){
            while(true){
                if (d.front() == which){
                    d.pop_front();
                    break;
                }
                d.push_back(d.front());
                d.pop_front();
                cnt +=1;
            }
        }else{
            while(true){
                if (d.front() == which){
                    d.pop_front();
                    break;
                }
                d.push_front(d.back());
                d.pop_back();
                cnt+=1;
            }
        }
    }
    cout << "cnt: "<<cnt << endl;
    return 0;
}
