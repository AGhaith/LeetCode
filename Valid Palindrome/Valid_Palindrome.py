class Solution(object):
    def isPalindrome(self, Input_String):
        """
        :type s: str
        :rtype: bool
        """
        for Curr_Char in Input_String:
            if Curr_Char.isalnum()==False:
                Input_String=Input_String.replace(Curr_Char,"")
        Input_String=Input_String.lower()
        String_Length = len(Input_String)
        Left=0
        Right=(String_Length)-1
        Half_Length=(String_Length//2)
        while(Left<Half_Length):
            if Input_String[Left]==Input_String[Right]:
                Left+=1
                Right-=1
            else:
                return False
        return True
    
    # Time Complexity is O(n)
    # My Approach :
    # First I will "Cure" the string meaning i will remove all the non-alphanumeric characters from the string
    # Note : an alphanumeric character is a character that is either a letter or a number so non-alphanumeric characters are like " " or "," or "." etc
    # Then I will convert the string to lowercase to make sure when comparing the characters it is case INsensitive
    # Then first we need to figure out will it be different for odd length and even length strings if it is different then we will try to take an approach that works for both
    # Let's test that out
    # Example 1 :
    # Input "OAAO" what should happen here is we first compare the contents in index 0 with index 3 and then index 1 with index 2
    # Example 2 :
    # Input "POP" what should happen here is we first compare the contents in index 0 with index 2 but notice something that the index in the middle is mutual that means it wont matter if we compare it or not
    # Luckily there is a condition that can work fine in both cases that is moving from left and right at the same time but we only need to move (String_Length//2) times
    # Note that we use integer division because in the case of odd numbers like out example "POP" we only need to check once that is 3//2 = 1
    # So we will move from left to right and right to left and compare the characters at the same time
    # If we find a mismatch we return False else we return True
    # That's it we are done
    
    # Ahmed Ghaith