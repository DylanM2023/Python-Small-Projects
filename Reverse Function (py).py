NewPhrase = ""
Answer = ""
count = 0
Phrase = "The cat sat on the mat, with another cat!"
Phrase = Phrase.split()
count = len(Phrase) - 1
for i in Phrase:
    NewPhrase = Phrase[count]
    Answer = Answer + NewPhrase + (" ")
    count = count - 1
print(Answer)


