class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1

        while i<j:
            if s[i].lower()==s[j].lower():
                print("yes")
                i +=1
                j -= 1
            else:
                if not (48<=ord(s[i])<=57 or 65<=ord(s[i])<=90 or 97<=ord(s[i])<=122): 
                    i += 1
                
                elif not (48<=ord(s[j])<=57 or 65<=ord(s[j])<=90 or 97<=ord(s[j])<=122): 
                    j -= 1
                else:
                    return False
        return True