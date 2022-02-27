import re

punctuation1 = ['.', '?', '!']
punctuation2 = [',']

'''
(1) some words. -> some words.
[1] some words. -> some words.
source: https://stackoverflow.com/questions/14596884/remove-text-between-and
'''
def delete_parenthesis(sentence) -> str:
    return re.sub("[\(\[].*?[\)\]]", "", sentence)


'''
dots ... word, end. -> ['dots', '...', 'word', ',', 'end', '.']
source: https://www.geeksforgeeks.org/python-split-string-on-all-punctuations/
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


def manage_paragraph():
    # TODO
    pass

'''
format: 0 or 1. 0 is putting each sentence on one line. 1 is regular paragraph format. 

return: list of paragraphs that are recognized
'''
def write_word_to_file(sentence, w_file, format=0):

    paragraphs = []

    without_parenthesis = delete_parenthesis(sentence)

    list_of_words = match(without_parenthesis)

    list_of_words_with_space = add_spaces(list_of_words)

    for word in list_of_words_with_space:

        try:
            w_file.write(word)
        except:
            print("unrecognizable\r")

        if word.isdigit():
            w_file.write('\r')
            w_file.write('\r')
            paragraphs.append(word)
            manage_paragraph()
        

        if format == 0:
            char = '\r'
        elif format == 1:
            char = ' '

        if word in punctuation1:
            w_file.write(char)
    
    return paragraphs
       
def main():
    f = open('longer_test.txt','r', encoding='UTF-8')
    contents = f.read()
    #contents = contents.decode('UTF-8')

    f2 = open('longer_test_result.txt', 'w')
    found_paragraphs = write_word_to_file(contents, f2)

    print(found_paragraphs)

    f.close()
    f2.close()

main()
