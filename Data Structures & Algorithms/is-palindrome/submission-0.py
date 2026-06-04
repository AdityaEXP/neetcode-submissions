class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabets = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
        # numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

        processed_1 = ""

        for x in s:
            if (x.lower() in alphabets):
                processed_1 += x.lower()
            
            if(x.isdigit()):
                # if x in numbers:
                processed_1 += x

        p_2 = ""

        for i in range(len(s) -1, -1, -1):
            x = s[i]

            if (x.lower() in alphabets):
                p_2 += x.lower()
            
            if(x.isdigit()):
                # if x in numbers:
                p_2 += x
        
        print(processed_1)
        print(p_2)
        return processed_1 == p_2



