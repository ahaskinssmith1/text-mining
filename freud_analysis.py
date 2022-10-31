# Import Pyschology of Dreams by Freud from Project Gutenberg as dreams
dreams = 'https://www.gutenberg.org/files/66048/66048-0.txt'



# Import Analysis of the Ego by Freud from Project Gutenberg as ego 

ego = 'https://www.gutenberg.org/files/35877/35877-0.txt'



def load_book(url):
    """
    This is a helper function to load a book given the book's URL from projectgutenerg.org 
    """
    import urllib.request
    with urllib.request.urlopen(url) as f:
        response = urllib.request.urlopen(url)
        data = response.read()
        book = data.decode('utf-8')
    return book


load_book(ego)


# remove stopwords

def remove_stopwords():
    """
    This a function to remove stopwords from a string 
    Uses the helper function load_book to get the string from which to remove stopwords 
    """
    # Used code from https://stackabuse.com/removing-stop-words-from-strings-in-python/
    # Mostly used article to learn how to use the tokenize package from nltk

    import nltk
    from nltk.corpus import stopwords
    # nltk.download('stopwords')
    from nltk.tokenize import word_tokenize
    from nltk.tokenize import wordpunct_tokenize
    # nltk.download('punkt')

    url = 'https://www.gutenberg.org/files/35877/35877-0.txt'

    text = load_book(ego) 

    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(text)

    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    return filtered_sentence 


remove_stopwords()


# count frequencies of each word 

def word_dict():
    """
    This is a function to count the frequency of each word in a string and store in a dictionary with word as key and frequency as value 
    """
    import string
    book = remove_stopwords()
    counts = {}
    for word in book:
        counts[word] = counts.get(word, 0) + 1 
    return counts 


word_dict()


#sort word_list
def word_list_sorted(): 
    hist = word_dict() 
    print(type(hist))
    sorted_hist = {}
    sorted_keys = sorted(hist, key = hist.get)

    for w in sorted_keys: 
        sorted_hist[w] = hist[w]

    print(sorted_hist)

word_list_sorted()






#Compare polarity outputs of the texts


def get_polarity():
    import nltk
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    book = remove_stopwords()
    book_string = ' '.join(book)
    score = SentimentIntensityAnalyzer().polarity_scores(book_string)

    print(score)


get_polarity()

# criticism of Freud's theories centers on their hyper-sexual nature https://literariness.org/2016/04/16/freudian-psychoanalysis/



