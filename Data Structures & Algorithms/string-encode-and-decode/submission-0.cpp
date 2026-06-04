#include <vector>
#include <unordered_map>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:

    string encode(vector<string>& strs) {
        string final_coded = "";
        for (auto s: strs) {
            final_coded+=to_string(s.length()) + "#" + s;
        }

        return final_coded;
    }

    vector<string> decode(string s) {
        vector<string> result;
        // string s = "5#hello9#word"

        for(int i = 0; i < s.size(); ++i) {

            int j = i;
            string lennum = "";
            while (s[j] != '#') {
                lennum+=s[j];
                ++j;
            }
            
            char ele = s[i];
            int ls = stoi(lennum);
            result.push_back(s.substr(j + 1, ls));

            lennum = "";
            i = j + ls;
        }

        return result;
    }
};
