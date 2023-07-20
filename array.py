# You are given an initial 2-value array (x). You will use this to calculate a score.

# If both values in (x) are numbers, the score is the sum of the two.
# If only one is a number, the score is that number. If neither is a number, return 'Void!'.

# Once you have your score, you must return an array of arrays.
# Each sub array will be the same as (x) and the number of sub arrays should be equal 
# to the score.

# For example:

# if (x) == ['a', 3] you should return [['a', 3], ['a', 3], ['a', 3]].

# def explode(arr):  
    
#     num = [0,1,2,3,4,5,6,7,8,9]
    
#     if arr[0] in num and arr[1] in num:
#         score = sum(arr)
#         return [arr] * score
#     elif arr[0] in num:
#         score = arr[0]
#         return [arr] * score
#     elif arr[1] in num:
#         score = arr[1]
#         return [arr] * score
#     else:
#         return 'Void!'