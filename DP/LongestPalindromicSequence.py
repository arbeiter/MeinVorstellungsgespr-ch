'''
Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-i.html


def findLongestPalindromic(S):

#first approach
#find all palindromes. sort by size

#second approach
#find all positions of all elements
#abcbaa
#table:
#a->0,4,5
#b->1,3
#c->2
#sort these by diff
#iterate over these bounds and check

#Cache solutions
