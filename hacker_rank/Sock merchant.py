# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:39:21 2020
    John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock
Input Format

The first line contains an integer , the number of socks represented in .
The second line contains  space-separated integers describing the colors  of the socks in the pile.

Constraints

 where 
Output Format

Return the total number of matching pairs of socks that John can sell.

Sample Input

9
10 20 20 10 10 30 50 10 20
Sample Output

3
@author: Jivitesh Gudekar
"""


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pair = 0
    mylist = list(set(ar))
    for i in range(len(mylist)):
        count = ar.count(mylist[i])
        pair += int(count / 2)
    return pair

if __name__ == '__main__':
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    result = sockMerchant(n, ar)

    print(str(result) + '\n')

