import pandas as pd

baseExFile = pd.read_excel('./Datasets/CurrasAnnotations_Full.xlsx')
freqExFile = pd.read_excel('./Datasets/Curras_wordsFrequencies.xlsx')

# print(baseExFile)

paWords = {}
wordFreq = {}

# translation logic (lookup values)


def translate(engWord):
    transList = []
    comparisonHash = {}
    maxWord = {}

    for paWord in paWords:
        if engWord in paWords[paWord]:
            transList.append(paWord)

    # compare values to select most used word
    for word in transList:
        maxWord[word] = wordFreq[word]

    return max(maxWord)


# step 0: clean data and add to dictionary
for i, word in enumerate(baseExFile['Word_Ar']):
    if word != '?':
        engTransList = []
        cleanDef = str(baseExFile['Gloss'][i]).replace(
            ';', ' ').replace('/', ' ')
        if (str(baseExFile['Gloss'][i]) == cleanDef):
            engTransList.append(cleanDef.strip())
        else:
            engTransList.extend(cleanDef.split(' '))
        if word not in paWords:
            paWords[word] = engTransList
        else:
            paWords[word].append(engTransList)

for word in freqExFile['Word_Ar']:
    if word not in wordFreq:
        wordFreq[word] = freqExFile['Frequency']
    else:
        wordFreq[word] += freqExFile['Frequency']


# test func

# translate('the')

# step 1: function of translator -> give one word translations to english keywords; first item to appear with english word

# step 2: give sentences and parse word by word

testSentence = 'when is the store open'

out = ''

for word in testSentence.split():
    if type(translate(word)) is str:
        out += translate(word) + ' '
print(out)

# step 3 -> update translation with word freq to adopt most used
