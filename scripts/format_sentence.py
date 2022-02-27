import re

punctuation1 = ['.', '?', '!']
punctuation2 = [',']

'''
(1) some words. -> some words.
[1] some words. -> some words.
'''
def delete_parenthesis(sentence) -> str:
    return re.sub("[\(\[].*?[\)\]]", "", sentence)


'''
dots ... word, end. -> ['dots', '...', 'word', ',', 'end', '.']
'''
def match(sentence) -> list:
    return re.findall( r'\w+|[^\s\w]+', sentence)


'''
['dots', '...', 'word', ',', 'end', '.'] -> ['dots', ' ', '...', ' ', 'word', ',', ' ', 'end', '.']
'''
def add_spaces(list_of_words) -> list:
    result = []

    for word in list_of_words:
        if word not in punctuation1 and word not in punctuation2:
            result.append(word)
            result.append(' ')
        elif word in punctuation2:
            result.pop()
            result.append(word)
            result.append(' ')
        else:
            result.pop()
            result.append(word)

    return result



def write_word_to_file(sentence, w_file):

    without_parenthesis = delete_parenthesis(sentence)

    list_of_words = match(without_parenthesis)

    list_of_words_with_space = add_spaces(list_of_words)

    for word in list_of_words_with_space:

        w_file.write(word)
        
        if word in punctuation1:
            w_file.write('\r')
       

f = open('testing.txt','r', encoding='UTF-8')
contents = f.read()
#contents = contents.decode('UTF-8')

f2 = open('testing_result.txt', 'w')
write_word_to_file(contents, f2)

f.close()
f2.close()
