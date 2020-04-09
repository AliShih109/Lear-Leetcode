'''
1207. Unique Number of Occurrences

Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.


Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
  
Example 2:
Input: arr = [1,2]
Output: false
  
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
'''


#Solution1
class Solution1():
    def uniqueOccurrences(self, arr):
    
        dict = {} #創建空字典dictionary
    
        for val in arr:
            if val not in dict:
                dict[val] = 0
            dict[val] += 1
                
        return len(dict.values()) == len(set(dict.values())) #set是一種資料型態叫集合

##Python的基本資料型態
##list[]:序列, tuple(): 序對(宣告後就不可修改), set{}: 集合(無序的不重覆序列), dict{key, value}: 字典


#Solution2
from collections import Counter #計數器，可輸入list, string並返回dict

class Solution2():
    def uniqueOccurrences(self, arr):
    
        dict=Counter(arr)         
        return len(dict.values()) == len(set(dict.values()))
