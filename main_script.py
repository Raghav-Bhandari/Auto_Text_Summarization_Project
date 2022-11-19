import spacy

# 'en_core_web_sm' is an English word library that includes vocabulary and syntax
# can be used en_core_web_lg
nlp = spacy.load('en_core_web_sm')

# Pkgs for Normalizing Text
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

# Import Heapq for Finding the Top N Sentences
from heapq import nlargest

# Summarizer function
def text_summarizer(raw_docx,key):
    raw_text = raw_docx
    docx = nlp(raw_text)

    # list of stop words there are in total 40 stop words in python
    stopwords = list(STOP_WORDS)

    # Build Word Frequency # word.text is tokenization in spacy
    word_frequencies = {}  
    for word in docx:  
        if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1

    # Calculate maximum frequency
    maximum_frequncy = max(word_frequencies.values())

    # Perform Normalization to get frequency in range 0-1
    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
        
    # List of sentences in raw_text
    sentence_list = [ sentence for sentence in docx.sents ]

    # Sentence Scores need to be check
    sentence_scores = {}  
    for sent in sentence_list:  
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]

    # Sentence arrange according to ranking
    summarized_sentences = nlargest(key, sentence_scores, key=sentence_scores.get)

    # Extracting main summary and converting it to string format
    final_sentences = [ w.text for w in summarized_sentences ]
    summary = ' '.join(final_sentences)
    return summary

raw_docx="Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think like humans and mimic their actions. The term may also be applied to any machine that exhibits traits associated with a human mind such as learning and problem-solving.The ideal characteristic of artificial intelligence is its ability to rationalize and take actions that have the best chance of achieving a specific goal. A subset of artificial intelligence is machine learning (ML), which refers to the concept that computer programs can automatically learn from and adapt to new data without being assisted by humans. Deep learning techniques enable this automatic learning through the absorption of huge amounts of unstructured data such as text, images, or video.When most people hear the term artificial intelligence, the first thing they usually think of is robots. That's because big-budget films and novels weave stories about human-like machines that wreak havoc on Earth. But nothing could be further from the truth.Artificial intelligence is based on the principle that human intelligence can be defined in a way that a machine can easily mimic it and execute tasks, from the most simple to those that are even more complex. The goals of artificial intelligence include mimicking human cognitive activity. Researchers and developers in the field are making surprisingly rapid strides in mimicking activities such as learning, reasoning, and perception, to the extent that these can be concretely defined. Some believe that innovators may soon be able to develop systems that exceed the capacity of humans to learn or reason out any subject. But others remain skeptical because all cognitive activity is laced with value judgments that are subject to human experience."

def main():
    sum = text_summarizer(raw_docx,7)
    print(sum)


if __name__ == "__main__":
    main()
# print("****************************************")
# sum2 = text_summarizer(sum,3)
# print(sum2)