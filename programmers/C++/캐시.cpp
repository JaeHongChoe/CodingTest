#include <string>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;

int solution(int cacheSize, vector<string> cities) {
    int answer = 0;
    list<string> cache;
    int cnt = 0;
    
    if (cacheSize == 0)
        return cities.size() *5;
    
    for(int i =0; i < cities.size(); i++){
        for_each(cities[i].begin(), cities[i].end(), [](auto& c){c = tolower(c);});
        
        auto ptr = find(cache.begin(), cache.end(), cities[i]);
        
        if(ptr != cache.end()){ //hit
            cnt++;
            cache.erase(ptr);
            cache.push_back(cities[i]);
        }else{
            cnt+=5;
            if(cache.size() > cacheSize-1){
                cache.pop_front();
            }
            cache.push_back(cities[i]);
        }
        
    }
    return cnt;
}
