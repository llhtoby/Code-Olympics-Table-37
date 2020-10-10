"""

Write a program that takes a dictionary word list (example below) and two words 
then determines the smallest number of steps possible to get from the first word to the second one.  
Each step can only change 1 letter and the words on each step need to be present in the dictionary.  
The output should be an integer.

Example dictionary:
""hot"",""dot"",""dog"",""lot"",""log"",""arm"",""cat"",""man""
 
Word 1:
hit
Word 2:
cog
 
Output:
5

"""


"""
check if word1 has len(word2)-1 letters that are the same, e.g. cat and mat, not cat and sit
"""
def checkWords(word1, word2):
    word1_list = list(word1)
    word2_list = list(word2)

    same_letters = 0
    can_change = False

    for i in range(len(word2)):
        if word1_list[i] == word2_list[i]:
            same_letters += 1
    
    if same_letters == (len(word2) - 1):
        can_change = True

    return can_change

