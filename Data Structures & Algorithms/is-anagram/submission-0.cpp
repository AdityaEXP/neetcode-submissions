#include <unordered_map>
#include <string>

using namespace std;


class Solution {
public:
    bool isAnagram(string s, string t) {

        if (s.length() != t.length()) {
            return false;
        }
        
        unordered_map<char, int> word1;

        for(int i = 0; i < s.size(); i ++) {
            char ele = s[i];
            word1[ele] += 1;
        }

        for (auto i: t) {
            word1[i]--;

            if (word1[i] == 0) {
                word1.erase(i);
            }
        }

        if (word1.empty()) {
            return true;
        } else {
            return false;
        }

    }
};
