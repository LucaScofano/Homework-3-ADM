# -*- coding: utf-8 -*-
"""exercise_4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10_5OThPYfQfXHadIS1_rPaAI2S-7UJk9
"""

#We understood the theory, but for the practice google helped us.
def subsequence(str): 
    n = len(str) 
  
    M = [[0 for x in range(n)] for x in range(n)] # create a matrix to store subsequence --> list comprehension
     
    # Strings of length 1 are palindrome of length 1 
    for i in range(n): 
        M[i][i] = 1
        
    for c in range(2, n + 1): # c is length of substring
        for i in range(n-c+1): 
            j = i+c-1
            if str[i] == str[j] and c == 2: 
                M[i][j] = 2
            elif str[i] == str[j]: 
                M[i][j] = M[i+1][j-1] + 2
            else: 
                M[i][j] = max(M[i][j-1], M[i+1][j]) 

    return M[0][n-1] 

seq = "DATAMININGSAPIENZA"
n = len(seq) 

print(subsequence(seq))

#OUTPUT: 7