'''
Created on 8/30/2019 @author: TBABAIAN
 
Starting code for hw2. Place the rest of the code below the comment line 
'''

def fromFile(file):
    file = open(file, 'r')
    line = file.read()
    return line 

txtfile =   input("Please enter the name of the file containing the text: ")
textOrig = fromFile(txtfile).strip() 
print('Contents of file',txtfile)
print ('*****************\n', textOrig, '*****************\n')

'''Place your code below this line '''

'''
created on Sep 15, 2019 by Joann.
wordcontext project from CS602 Assignment 2: 
given a chunk of text (through a file) and a keyword, locate the first occurrence of the keyword \
in the text, output the sentence in which the keyword appears, along with the sentences before and \
after. Text before and after the displayed portion should be represented with five periods.

input:
1. file name containing the text;
2. a keyword in the text;
output:
(1) the sentence right before the sentence that contains the keyword, followed by
(2) the sentence that contains the keyword, showing the keyword in all capital letters, followed by 
(3) the sentence right after the sentence that contains the keyword.
(4) In addition a set of five periods should be displayed in place of text before (1) and/or after (3).
If the text does not contain the keyword, the program should report that.

about how to locate the keyword:
keyword with spaces before and after could be find in a text containing only words and spaces between them

'''

#prompt the user to enter the file name and the keyword
inputText = textOrig
keyWd = input('Enter the keyword: ').upper()
keyWd = ' ' + keyWd + ' '
#define five period
fivePeriod = '.....'

#formalize the format of the text
inputText = inputText.replace('. ', '.')
inputText = inputText.replace('? ', '?')
inputText = inputText.replace('! ', '!')
inputText = inputText.replace('.', '. ')
inputText = inputText.replace('?', '? ')
inputText = inputText.replace('!', '! ')

#upper case the text
revisedTextUp = inputText.upper()

#replace ?&! with dot and store in a variable
revisedTextDot = revisedTextUp.replace("?", '.')
revisedTextDot = revisedTextDot.replace('!', '.')

#replace the punctuation with space and store in a variable
revisedTextPu = revisedTextDot.replace('.', ' ')
revisedTextPu = revisedTextPu.replace(',', ' ')
revisedTextPu = revisedTextPu.replace('-', ' ')
revisedTextPu = revisedTextPu.replace("’", " ")
revisedTextPu = revisedTextPu.replace("'", " ")
revisedTextPu = revisedTextPu.replace('(', ' ')
revisedTextPu = revisedTextPu.replace(')', ' ')
revisedTextPu = revisedTextPu.replace(';', ' ')

#define the output:

#if keyword is the first word in the text 
if revisedTextPu[:revisedTextPu.find(' ') + 1] == keyWd.lstrip(' '):
    #find the position of keyword
    positionKw = revisedTextPu.find(keyWd.lstrip())
    
    #replace the keyword with upper case
    inputText = keyWd.strip() + inputText[len(keyWd.strip()):]    
    
    #find the first dots after the keyword
    dotAfterKw = revisedTextDot[positionKw + len(keyWd.strip()):].find('.') + positionKw + len(keyWd.strip())
    
    #find the position of second dot after the keyword
    secDotAfterKw = revisedTextDot[dotAfterKw + 1:].find('.') + 1 + dotAfterKw
    
    #find the position of third dot after the keyword
    thirdDotAfterKw = revisedTextDot[secDotAfterKw + 1:].find('.') + 1 + secDotAfterKw
    
    #define the output sentence
    contextKw = inputText[:secDotAfterKw + 1] + fivePeriod
    
    if secDotAfterKw == dotAfterKw:
        secDotAfterKw = -1
        thirdDotAfterKw = -1
        contextKw = inputText
        
    elif thirdDotAfterKw == secDotAfterKw:
        thirdDotAfterKw = -1
        contextKw = inputText
    
    print()
    print(keyWd.strip() + ' appears in the following context:')
    print('-------------------------------------------------------------------------------------------------')
    print(contextKw)
    print('-------------------------------------------------------------------------------------------------')

else:
    #find the position of keyword
    positionKw = revisedTextPu.find(keyWd) + 1
    
    #find the position of first dots before the keyword
    dotBeforeKw = revisedTextDot[:positionKw].rfind('.')

    #find the position of second dots before the keyword
    secDotBeforeKw = revisedTextDot[:dotBeforeKw].rfind('.')
    if dotBeforeKw == -1:
        secDotBeforeKw = -1  
    
    #find the position of first dots after the keyword
    dotAfterKw = revisedTextDot[positionKw + len(keyWd.strip()):].find('.') + positionKw + len(keyWd.strip())
    
    #find the position of second dot after the keyword
    secDotAfterKw = revisedTextDot[dotAfterKw + 1:].find('.') + 1 + dotAfterKw
    
    #find the position of third dot after the keyword
    thirdDotAfterKw = revisedTextDot[secDotAfterKw + 1:].find('.') + 1 + secDotAfterKw
    
    if secDotAfterKw == dotAfterKw:
        secDotAfterKw = -1
        thirdDotAfterKw = -1
        
    elif thirdDotAfterKw == secDotAfterKw:
        thirdDotAfterKw = -1
        
    
    #if the text contains the keyword
    if keyWd in revisedTextPu:
        inputText = inputText[:positionKw] + keyWd.strip() + inputText[positionKw + len(keyWd.strip()):]
        
        #if the text has only one sentence and the keyword is in the sentence
        if dotBeforeKw == -1 and secDotAfterKw == -1:
            contextKw = inputText
        
        #if there's no sentence after the sentence where the keyword locates
        elif dotBeforeKw != -1 and secDotAfterKw == -1:
            #if there's only one sentence before the sentence where the keyword locates
            if secDotBeforeKw == -1:
                contextKw = inputText
            #if there's more than one sentence before the sentence where the keyword locates
            else: 
                contextKw = fivePeriod + inputText[secDotBeforeKw + 2:]
         
        #if there there's no sentence before the sentence where the keyword locates 
        elif dotBeforeKw == -1 and secDotAfterKw != -1:
            #if there's more than one sentence after the sentence where the keyword locates
            if thirdDotAfterKw != -1:
                contextKw = inputText[:secDotAfterKw + 1] + fivePeriod
            #if there's only one sentence after the sentence where the keyword locates
            else: 
                contextKw = inputText
                        
        #if there's sentences before and after the sentence where the keyword locates
        elif dotBeforeKw != -1 and secDotAfterKw != -1:
            if secDotBeforeKw == -1 and thirdDotAfterKw == -1:
                contextKw = inputText
                
            elif secDotBeforeKw != -1 and thirdDotAfterKw == -1:
                contextKw = fivePeriod + inputText[secDotBeforeKw + 2 :]
                
            elif secDotBeforeKw == -1 and thirdDotAfterKw != -1:
                contextKw = inputText[:secDotAfterKw + 1] + fivePeriod
                
            else:
                contextKw = fivePeriod + inputText[secDotBeforeKw + 2 : secDotAfterKw + 1] + fivePeriod
         
        print()   
        print(keyWd.strip() + ' appears in the following context:')
        print('-------------------------------------------------------------------------------------------------')
        print(contextKw)
        print('-------------------------------------------------------------------------------------------------')
        
    #if the text doesn't contain the keyword    
    else: 
        print('The text does not contain', keyWd.strip())
