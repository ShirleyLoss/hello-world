import unicodedata
import random

f = open('/Users/shirleyloss/Downloads/Tofel_word.txt',encoding = 'utf-8')
wordDictionary1 = {}
wordDictionary2 = {}
wordList = f.readlines()
for wordL in wordList[:]:
    word = wordL.split(' ')
    wordEnglish = word[0].split('\t')
    wordChinese = word[1].split('\n')
    wordDictionary1[wordEnglish[0]] = wordChinese[0]
    wordDictionary2[wordChinese[0]] = wordEnglish[0]

score = 0
for i in range(0,3):
    question = random.choice(list(wordDictionary1.keys()))
    print(question)
    answer = input()
    realAnswer = wordDictionary1.get(question)
    if answer == realAnswer:
        print('good!')
        score += 1
    else:
        print('Wrong! It\'s ' + realAnswer)
print(score)