# Dhruvin Bhayani
# 105170206

dictionaryFile = open('dictionary.txt', 'rt')
dictionaryString = dictionaryFile.read()
dictionaryWord = dictionaryString.split()
dictionaryFile.close()


storyFile = open('story.txt', 'rt')
storyString = storyFile.read()
storyWord = storyString.split()
storyFile.close()

uncommonWords = []
temp = 0


for i in range(len(storyWord)):
    temp = 0
    for j in range(len(dictionaryWord)):
        if storyWord[i] == dictionaryWord[j]:      
            temp = temp + 1
    if temp == 0:
        uncommonWords.append(storyWord[i])


print(len(uncommonWords))