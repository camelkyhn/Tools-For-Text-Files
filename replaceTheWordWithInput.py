import string
punctuation = string.punctuation

def getStringFromFile(filename):
    with open(filename, 'r')as file:
        content = file.read()
    return content

def putSpaceBeforeAndAfterPunctuation(content):
    for i in punctuation:
        index = 0
        while index<len(content):
            if i == content[index]:
                content = content[:(index)] + ' ' + i + ' ' + content[(index+1):]
                index+=2
            else:
                index+=1
    return content

#Returns a list not a string
def splitWords(content):
    words = content.split()
    return words

def replaceWordWithInput(wantToReplaceWith, willBeReplaced,  content):
    wantToReplaceWith = wantToReplaceWith.split()
    for index, value in enumerate(content):
        if willBeReplaced == value:
            content = content[:(index)] + wantToReplaceWith + content[(index+1):]
    return content

def convertListToString(contentList):
    content = ' '.join(contentList)
    return content

def removeSpaceBeforeComma(content):
    comma = ','
    index = 0
    while index<len(content):
        if comma == content[index]:
            content = content[:(index-1)] + content[(index):]
        index +=1
    return content

def removeExtraSpaces(content):
    for i in punctuation:
        index = 0
        while(index<len(content)):
            if i == content[index]:
                content = content[:(index-1)] + i + content[(index+2):]
            index+=1
    return content

if __name__ == '__main__':
    print('Enter the "WORD" you want to replace with!')
    wantToReplaceWith = input()
    print('Now, you must enter the "WORD" that is going to be replaced in the FILE!')
    willBeReplaced = input()
    content = getStringFromFile('Example.txt') #Example.txt is the file that is in the project directory and will be processed
    contentWithPunctuation = putSpaceBeforeAndAfterPunctuation(content)
    contentList = splitWords(contentWithPunctuation)
    newContent = replaceWordWithInput(wantToReplaceWith, willBeReplaced, contentList)
    finalContent = removeExtraSpaces(convertListToString(newContent))
    print(finalContent)
