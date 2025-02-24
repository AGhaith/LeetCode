# Time Complexity

Time complexity is O(n).

## My Approach

First, I will "cure" the string, meaning I will remove all the non-alphanumeric characters from the string.

**Note:** An alphanumeric character is a character that is either a letter or a number, so non-alphanumeric characters are like " " or "," or "." etc.

Then I will convert the string to lowercase to make sure when comparing the characters it is case **INSENSITIVE**.

Then first we need to figure out if it will be different for odd-length and even-length strings. If it is different, then we will try to take an approach that works for both.

Let's test that out.

### Example 1:

**Input:** "OAAO"

What should happen here is we first compare the contents in index 0 with index 3 and then index 1 with index 2.

### Example 2:

**Input:** "POP"

What should happen here is we first compare the contents in index 0 with index 2, but notice something: the index in the middle is mutual. That means it won't matter if we compare it or not.

Luckily, there is a condition that can work fine in both cases, which is moving from left to right at the same time, but we only need to move `(String_Length // 2)` times.

Note that we use integer division because in the case of odd numbers like our example "POP" we only need to check once, that is, `3 // 2 = 1`.

So we will move from left to right and right to left and compare the characters at the same time.

If we find a mismatch, we return **False**; else we return **True**.

That's it; we are done.

## Author

### Ahmed Ghaith

### A.wesam2300@nu.edu.eg
