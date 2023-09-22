#include <iostream>
#include <vector>
#include <string>
#include <cstdio>

using namespace std;


int main() {
	vector<string> vec {"abc", "def", "ghi"};

	if (const auto it = find(begin(vec), end(vec), "abc");
		it != end(vec)) {
		*it = "$$$";
	}

	for (const auto& s: vec) {
		cout << s << "\n";
	}

	return 0;
}