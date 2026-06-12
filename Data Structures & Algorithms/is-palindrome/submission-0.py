class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1
        while i<j:
            if s[i].lower()==s[j].lower():
                print("yes")
                i +=1
                j -= 1
            else:
                if not s[i].isalnum():
                    i += 1
                elif not s[j].isalnum():
                    j -= 1
                else:
                    return False
        return True