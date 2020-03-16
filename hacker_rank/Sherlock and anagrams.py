# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 13:25:19 2020

Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

For example , the list of all anagrammatic pairs is  at positions  respectively.

Function Description

Complete the function sherlockAndAnagrams in the editor below. It must return an integer that represents the number of anagrammatic pairs of substrings in .

sherlockAndAnagrams has the following parameter(s):

s: a string .
Input Format

The first line contains an integer , the number of queries.
Each of the next  lines contains a string  to analyze.

Constraints



String  contains only lowercase letters  ascii[a-z].

Output Format

For each query, return the number of unordered anagrammatic pairs.

Sample Input 0

2
abba
abcd
Sample Output 0

4
0
Explanation 0

The list of all anagrammatic pairs is  and  at positions  and  respectively.

No anagrammatic pairs exist in the second query as no character repeats.

Sample Input 1

2
ifailuhkqq
kkkk
Sample Output 1

3
10
Explanation 1

For the first query, we have anagram pairs  and  at positions  and  respectively.

For the second query:
There are 6 anagrams of the form  at positions  and .
There are 3 anagrams of the form  at positions  and .
There is 1 anagram of the form  at position .

Sample Input 2

1
cdcd
Sample Output 2

5
Explanation 2

There are two anagrammatic pairs of length :  and .
There are three anagrammatic pairs of length :  at positions  respectively.

@author: gudek
"""

#!/bin/python3

from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count = 0
    for i in range(1,len(s)+1):
        a = ["".join(sorted(s[j : j+i])) for j in range(len(s)-i+1)]
        b = Counter(a)
        for j in b:
            count+=b[j]*(b[j]-1)/2  # Using the formula n*(n-1)/2
    return int(count)
if __name__ == '__main__':

        s ="abba"

        result = sherlockAndAnagrams(s)

        print(str(result) + '\n')
