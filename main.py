import re

def analyze(file):
    alltext=  ""
    text_opened = open(file)

    for line in text_opened:
        alltext = alltext + line
    allwords = alltext.split()
  
    fixedwords = []
    for word in allwords:
        stripped_word = word.strip("!?.,;:")
        fixedwords.append(stripped_word)

    for w in range(len(fixedwords)):
        for character in fixedwords[w]:
            if character == "'":
                fixedwords[w] = fixedwords[w].replace("'", "")
            else:
              pass
    word_count = len(fixedwords)
  
    print("The total word count is:", word_count)
    word_lengths = []
    for word in fixedwords:
        single_wordlen = 0
        for i in range(len(word)):
          single_wordlen = len(word)
        word_lengths.append(single_wordlen)
    avg_wordlen = sum(word_lengths) / word_count
    print("The average word length within this text is:", avg_wordlen)

    pattern = r"([^.!?]+[.!?])"
    sentences = re.findall(pattern, alltext)
    sentence_count = len(sentences)
    print("The amount of sentences in this text is:", sentence_count)

    nested_sentences = []
    for sentence in sentences:
        nested_sentences.append(sentence.split())

    wps_count = []

    for listset in nested_sentences:
      wps_count.append(len(listset))
      wps_count.sort()
    q1 = wps_count[int((len(wps_count) + 1) * 0.25)]
    q2 = wps_count[int((len(wps_count) + 1) * 0.5)]
    q3 = wps_count[int((len(wps_count) + 1) * 0.75)]
    print(f"WORDS IN SENTENCE VARIATION \n Q1:{q1} \n Q2:{q2} \n Q3:{q3}")
    avg_sentlen = word_count / sentence_count
    print("The average sentence length of this text is:", avg_sentlen)
    
textfile = input("text file here:")
analyze(textfile)
