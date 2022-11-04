

# Project Overview

For this project I wanted to analyze texts from Project Gutenberg, specifically books written by Sigmund Freud. Having read criticism of Freud's books, but having never read the books myself, I wanted to analyze a number of Freud's books using sentiment analysis techniques in Python. I mainly used the Natural Language Toolkit library to do the analysis of the text. First, I used the stopword's corpus to remove words that added little information to the text. As well, I used the tokenize tool within the remove_stopwords function to break each word in the book into an individual string. As well, I used the polarity tool to give an idea of the overall sentiment of the text. From this, I hoped to 1. Understand the top terms in the text 2. The overall tone of the text with all terms considered. 

# Implementation

Starting at the top of my system, there is a helper function which imports a text from the project Gutenberg library given a globally declared variable set to the books url. This function returns the entire book as one string. From there, the book needs to be processed for further analysis using tools from the NLTK library. First is to tokenize the entire book, so each word is a string and can be muted based on logic. Next, the tokenized text needs to be looped through and compared to a corpus of stopwords, if any of the tokens match any of the stopwords, they are removed from the tuple. 

For the analysis portion of this system, there are two main components. First is creating a dictionary with with keys equal to a word and value equal to the word's frequency in the text. For this frequency dictionary, I wanted the dictionary to be sorted based on the value, for this I need to pass the word dictionary onto a new function to reorder the dictionary's elements. For this reordering, I decided to use the sorted method for dictionaries instead of nested loops to sort the dictionary. I just felt as if this was the easier route so thats why I took it. Second is sentiment analysis using the NLTK library which outputs a polarity score dictionary for the text. 


# Results


The criticism I've read on Freud's texts center on his gravitation towards sexuality as an explanation for everything (https://literariness.org/2016/04/16/freudian-psychoanalysis/). With this program, I wanted to break down the contents of two Freudian texts 1. For their top terms to examine for sexual themes and 2. For their overall tone or sentiment. 

Starting with the sentiment of the two books, I found these to be nearly identical (see polarity outputs below). Considering as these are two books from the same author, this is not suprising, but interesting nontheless. This could be an identication that Freud wrote in a uniform tone but uses different topics for his books. 

Next is the top terms. There are far too many words from each book to go over each term but there are many terms that stood out. For example, the word sexual appeared in the Pyschology of Dreams 156 times and appeared in Analysis of the Ego 100 times (the most frequent word for this book). As well, in Pyschology of Dreams some seemingly unrelated words such as wife appear a large number of times. The same thing is true of Analysis of the Ego with words like hypnosis appearing many times. 



## Pyschology of Dreams by Sigmund Freud 
### Words or terms that appeared 50 or more times 

{'enough': 50, 'They': 50, 'actual': 50, 'assume': 50, 'doubt': 50, 'motive': 50, 'intensity': 50, 'symptoms': 50, 'fulfilment': 50, 'patients': 51, 'position': 51, 'either': 51, 'entirely': 51, 'Maury': 51, 'situation': 51, 'feeling': 51, 'pain': 51, 'comes': 51, 'At': 51, 'away': 52, 'important': 52, '1': 52, 'occurs': 52, 'immediately': 52, 'explained': 52, 'actually': 52, 'necessary': 52, 'feelings': 52, 'capable': 52, 'suppressed': 52, 'discussion': 53, 'explain': 53, 'solution': 53, 'presentations': 53, 'associations': 53, 'parts': 54, 'least': 54, 'conception': 54, 'individual': 54, 'less': 54, 'power': 54, 'judgment': 54, 'expressed': 54, 'call': 54, 'And': 54, 'occur': 54, 'remains': 54, 'M.': 54, 'yet': 55, 'normal': 55, 'complete': 55, 'opposite': 55, 'known': 55, 'heard': 55, '!': 55, 'reference': 55, 'Gutenberg-tm': 55, 'difficult': 56, 'apparently': 56, 'There': 56, 'c.': 56, 'et': 56, 'came': 56, 'days': 56, 'sleeping': 56, 'und': 56, 'condition': 56, 'believe': 57, 'problem': 57, 'need': 57, 'general': 57, 'full': 57, 'object': 57, 'series': 57, 'real': 57, 'kind': 57, 'brother': 57, 'usually': 57, 'boy': 57, 'presentation': 57, 'almost': 58, 'hysterical': 58, 'year': 58, 'conditions': 58, 'common': 58, 'correct': 58, 'longer': 58, 'sensation': 58, 'together': 58, 'world': 59, 'shown': 59, 'awakening': 59, 'behind': 59, 'thing': 59, 'wife': 59, 'interest': 60, 'book': 60, 'says': 60, 'told': 60, 'next': 60, 'value': 61, 'since': 61, 'true': 61, 'easily': 61, 'What': 61, 'element': 61, 'represented': 61, 'use': 62, 'recognised': 62, 'sensations': 62, 'sense': 62, 'girl': 62, 'sure': 63, 'recent': 63, 'sources': 63, 'things': 64, 'Here': 64, 'makes': 64, 'Otto': 64, 'reality': 64, '&': 64, 'effect': 64, 'recollection': 64, 'appears': 64, 'seem': 64, 'soon': 64, 'called': 64, 'fear': 64, 'indeed': 65, 'de': 65, 'three': 65, 'authors': 66, 'dreaming': 66, 'experiences': 66, 'indifferent': 66, 'towards': 67, 'word': 67, 'foreconscious': 67, 'appear': 68, 'matter': 68, 'shows': 68, 'phantasy': 68, 'psychological': 69, 'knowledge': 69, 'dreamed': 69, 'scene': 69, 'infantile': 70, 'result': 70, 'Now': 70, 'follows': 70, 'end': 71, 'influence': 71, 'woman': 71, 'latter': 72, 'reason': 72, 'several': 72, 'house': 72, 'examples': 73, 'able': 73, 'left': 73, 'perception': 73, 'purpose': 74, 'processes': 74, 'To': 74, 'among': 74, 'probably': 74, 'used': 75, 'get': 75, 'excitement': 76, 'death': 77, 'said': 77, 'seen': 77, 'lady': 77, 'occasion': 78, 'think': 78, 'conscious': 78, 'stimulus': 78, 'anxiety': 78, 'Irma': 78, 'wish-fulfilment': 78, 'treatment': 79, 'connected': 79, 'My': 79, 'go': 79, 'character': 79, 'similar': 79, 'mental': 80, 'number': 80, 'according': 80, 'put': 81, 'old': 81, 'sensory': 81, 'origin': 82, 'That': 82, 'One': 82, 'cases': 82, 'Project': 84, 'takes': 84, 'system': 84, 'show': 85, 'brought': 85, 'last': 85, 'source': 86, 'She': 86, 'On': 87, 'nature': 87, 'back': 87, 'others': 89, 'words': 90, 'impressions': 90, 'young': 90, 'hand': 92, 'perhaps': 93, 'meaning': 94, 'nothing': 94, 'becomes': 94, 'whole': 94, 'example': 95, 'given': 95, 'representation': 96, 'pictures': 97, 'apparatus': 97, 'relations': 98, 'account': 99, 'Thus': 99, 'impression': 99, 'significance': 100, 'whether': 100, 'never': 101, 'question': 101, 'different': 101, 'censor': 101, 'really': 102, 'quite': 102, 'ideas': 103, 'subject': 103, 'always': 103, 'give': 104, 'present': 104, 'mother': 104, 'name': 105, 'childhood': 106, 'come': 106, 'process': 106, 'children': 106, 'whose': 108, 'As': 108, 'form': 108, 'experience': 109, 'point': 110, 'manner': 110, 'possible': 111, 'idea': 112, 'later': 113, 'far': 113, 'wishes': 113, 'well': 115, 'much': 116, 'might': 116, 'expression': 119, 'attention': 119, 'explanation': 120, 'could': 123, 'say': 123, 'relation': 124, 'consciousness': 125, 'night': 125, 'stimuli': 127, 'make': 128, 'order': 129, 'new': 129, 'long': 129, 'though': 129, 'therefore': 130, 'certain': 130, 'every': 130, 'taken': 130, 'persons': 134, 'following': 134, 'seems': 135, 'great': 135, 'For': 138, 'take': 138, 'something': 138, 'elements': 138, 'become': 138, 'find': 140, 'patient': 140, 'formation': 146, 'know': 146, 'mind': 146, 'connection': 149, 'many': 150, 'theory': 150, 'second': 151, 'course': 154, 'already': 154, 'sexual': 156, 'see': 158, 'child': 160, 'dreamer': 163, 'memory': 163, 'thus': 163, 'years': 165, 'unconscious': 166, 'means': 166, 'person': 167, 'He': 168, 'friend': 170, 'man': 171, 'still': 172, 'without': 173, 'way': 173, 'little': 174, 'work': 175, 'often': 175, 'father': 184, 'found': 186, 'shall': 187, 'however': 188, 'analysis': 192, 'even': 196, 'If': 200, 'place': 204, 'made': 205, 'case': 205, 'p.': 212, 'state': 213, '?': 213, 'sleep': 216, 'A': 218, 'like': 223, 'activity': 224, 'waking': 229, 'fact': 233, 'part': 248, 'We': 252, 'This': 261, 'material': 263, 'day': 277, 'interpretation': 280, 'thought': 282, 'another': 291, 'time': 297, 'life': 302, 'Footnote': 304, 'would': 307, 'two': 311, 'wish': 316, 'first': 320, 'But': 322, 'upon': 330, 'also': 332, 'us': 361, 'content': 363, 'must': 370, 'In': 383, 'It': 408, '[': 412, ']': 412, 'thoughts': 429, , 'psychic': 490, 'may': 585, '’': 622, 'dreams': 822,  'one': 879, ':': 914, ';': 1160, '”': 1176, 'The': 1231, 'I': 2489, 'dream': 3500}

### Polarity output
{'neg': 0.119, 'neu': 0.641, 'pos': 0.241, 'compound': 1.0} 


## Analysis of the Ego by Sigmund Freud

### Words or terms that appeared 10 or more times 

'almost': 10, 'License': 10, 'English': 10, 'http': 10, 'AND': 10, '23': 10, '41': 10, 'within': 10, 'small': 10, 'produced': 10, 'Let': 10, 'sort': 10, 'act': 10, 'ideas': 10, 'fundamental': 10, 'greater': 10, 'shows': 10, 'alone': 10, 'contagion': 10, 'personal': 10, 'longer': 10, 'level': 10, 'never': 10, 'whose': 10, '56': 10, 'features': 10, 'By': 10, 'neuroses': 10, 'leaders': 10, 'could': 10, 'As': 10, 'share': 10, 'end': 10, 'emotions': 10, '25': 10, 'mutual': 10, '39': 10, 'general': 10, 'hand': 10, 'present': 10, 'keep': 10, 'nothing': 10, '26': 10, 'possibility': 10, 'repression': 10, 'narcissism': 10, 'object-choice': 10, 'Psychoanalyse_': 10, 'tender': 10, '58': 10, '74': 10, '82': 10, '93': 10, 'United': 10, 'States': 10, 'access': 10, 'paragraph': 10, 'Identification': 11, 'seem': 11, 'true': 11, 'brothers': 11, 'particular': 11, 'special': 11, 'seems': 11, 'brought': 11, 'family': 11, 'able': 11, 'completely': 11, 'change': 11, 'view': 11, 'circumstances': 11, 'last': 11, 'lost': 11, 'remains': 11, 'becomes': 11, 'exist': 11, 'arise': 11, 'artificial': 11, 'said': 11, 'observed': 11, 'origin': 11, '19': 11, 'organisation': 11, 'structure': 11, '20': 11, 'old': 11, 'To': 11, 'distinction': 11, 'used': 11, 'process': 11, 'Thus': 11, '1920': 11, 'You': 12, 'copy': 12, 'original': 12, 'concerned': 12, 'something': 12, 'clear': 12, 'say': 12, 'For': 12, 'second': 12, 'degree': 12, 'effect': 12, '34': 12, 'put': 12, 'yet': 12, 'especially': 12, 'symptom': 12, 'shown': 12, 'situation': 12, 'gives': 12, 'takes': 12, 'taken': 12, 'objects': 12, 'world': 12, 'account': 12, 'women': 12, '44': 12, 'sensual': 12, 'copyright': 12, 'donations': 12, 'give': 13, 'No': 13, '33': 13, 'Church': 13, '90': 13, 'full': 13, 'social': 13, 'perhaps': 13, 'easy': 13, 'capable': 13, 'among': 13, 'conscious': 13, 'similar': 13, 'consideration': 13, 'equal': 13, 'outside': 13, 'Trotter': 13, 'complete': 13, 'danger': 13, 'repressed': 13, '57': 13, '94': 13, 'Literary': 13, 'Archive': 13, 'German': 14, 'parents': 14, 'acts': 14, 'different': 14, 'psycho-analysis': 14, 'des': 14, 'condition': 14, '3': 14, 'makes': 14, 'importance': 14, 'see': 14, 'hypnotist': 14, '10': 14, 'free': 14, 'reality': 14, 'doubt': 14, 'force': 14, 'feeling': 14, 'easily': 14, 'rather': 14, 'instance': 14, 'panic': 14, '84': 14, 'use': 15, 'away': 15, 'conditions': 15, 'number': 15, 'important': 15, 'little': 15, 'p': 15, 'might': 15, 'less': 15, 'result': 15, 'power': 15, 'always': 15, 'later': 15, 'things': 15, 'found': 15, 'based': 15, 'back': 15, '18': 15, "''": 15, 'hero': 15, 'set': 16, 'show': 16, 'described': 16, 'therefore': 16, '?': 16, 'character': 16, 'question': 16, 'intellectual': 16, 'p.': 16, 'idea': 16, 'McDougall': 16, 'word': 16, 'men': 16, 'thus': 16, 'entirely': 17, 'whole': 17, 'psychological': 17, 'There': 17, 'feelings': 17, 'long': 17, 'interest': 17, 'expression': 17, 'mother': 17, 'OF': 18, 'already': 18, 'explanation': 18, 'characteristics': 18, 'know': 18, 'agreement': 18, 'army': 18, 'loved': 18, 'See': 18, 'zur': 18, 'phenomena': 19, 'factor': 19, 'quite': 19, 'need': 19, 'human': 19, 'children': 19, 'emotion': 19, 'child': 19, 'cases': 19, 'und': 20, 'find': 20, 'satisfaction': 20, 'And': 20, 'point': 20, 'together': 20, 'whether': 20, 'terms': 21, 'man': 21, 'many': 21, 'primitive': 21, 'possible': 21, 'development': 21, 'form': 21, 'take': 21, 'common': 21, 'aim': 21, 'libidinal': 21, 'dread': 21, 'inhibited': 21, 'though': 22, 'given': 22, 'nature': 22, 'still': 22, 'far': 22, 'often': 22, 'relations': 23, 'others': 23, 'make': 23, 'He': 23, 'much': 23, 'Christ': 23, 'great': 24, 'come': 24, 'psychology': 24, 'members': 24, 'herd': 24, 'libido': 24, 'Foundation': 24, 'Group': 25, 'well': 25, 'horde': 25, 'THE': 26, 'certain': 26, 'subject': 26, 'new': 26, 'place': 26, 'directly': 26, 'Gutenberg': 27, 'time': 27, 'become': 27, 'every': 27, 'state': 27, 'suggestion': 27, 'hypnosis': 27, 'primal': 27, 'electronic': 27, '*': 28, 'mind': 28, 'formation': 28, 'without': 28, 'relation': 28, 'aims': 29, 'shall': 29, 'made': 29, 'Psychology': 30, 'influence': 30, 'instinct': 30, 'unconscious': 31, 'tendencies': 31, 'sense': 32, 'leader': 32, 'kind': 32, 'This': 34, 'Bon': 34, 'If': 34, 'case': 34, 'works': 34, 'tie': 34, 'Le': 35, 'like': 35, 'part': 36, 'means': 36, 'emotional': 36, 'A': 37, 'life': 37, 'person': 38, 'towards': 38, 'another': 38, 'first': 39, 'mental': 39, 'fact': 40, 'individuals': 41, 'ties': 42, 'instincts': 43, 'two': 43, 'even': 43, 'identification': 47, 'I': 48, 'would': 48, 'ideal': 49, 'father': 49, 'also': 51, 'must': 52, 'people': 54, 'In': 55, 'work': 55, 'Gutenberg-tm': 55, 'way': 57, 'But': 65, 'us': 70, 'We': 70, 'groups': 74, 'Project': 83, 'It': 84, ':': 91, 'object': 94, '--': 94, 'upon': 95, 'sexual': 100} 


### Polarity output
{'neg': 0.108, 'neu': 0.677, 'pos': 0.215, 'compound': 1.0} 




# Reflection

For the coding of this program, the hardest part was properly using the NLTK tools. This required a multitude of google searches on what packages to download and how to do so. I found that using these libraries was not as simple as importing a package in vscode. I think my scope may have been too large for this assignment, as my analysis did not yield much insight. My analysis for these texts was a little light, if I had more time I would like to run the the two books side by side and compare their similarities in a vectorspace. As well, I would like to modify this program to run multiple texts at the same time. As it stands right now, you need to run one book at a time. While this implimentation works, it is not the most elegant solution. 


