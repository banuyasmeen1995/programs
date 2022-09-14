import numpy as np
def binarySearch(arr, x):
    low = 0

    high = len(arr)
    while (low <= high):
       m = (low + high) // 2

       item = arr[m]

       if (item == x):
           return m 

       if (item < x):
           low = m + 1

       else:
           high = m - 1

    return -1

  
dic = open("dict.txt")
dictionary = dic.read().split()
spellsfile = open("spells.txt")
spells = spellsfile.read().split()
dictionary.sort()

incorrect_words = 0
for spell in spells:
    result = binarySearch(dictionary, spell)

if (result == -1):
    incorrect_words+=1
  
if (incorrect_words != 0):
    print("Number of incorrect word found is: ",incorrect_words)
else:
    print("All words are present in the dictionary.")