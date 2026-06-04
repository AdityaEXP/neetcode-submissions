#include <vector>
#include <unordered_map>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
    
    unordered_map < string, vector<string> > allwords;

    for (auto word: strs) {
        string key = word;
        sort(key.begin(), key.end());

        allwords[key].push_back(word);
    }

    vector <vector<string>> result;

    for (auto n: allwords) {
        vector<string> temp;

        for(auto a: n.second){ temp.push_back(a);}
        result.push_back(temp);

    }

    return result;
    }        
};
