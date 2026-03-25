#You are given an array arr[] of strings. Your have  to sort the array in ascending order based on the lengths of the strings. If two strings have the same length, maintain their original relative order.
class Solution:
    def sortByLength(self, arr):
        arr.sort(key=len)
        return arr
