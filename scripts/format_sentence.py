import re

def delete_parenthesis(sentence) -> str:
    return re.sub("[\(\[].*?[\)\]]", "", sentence)

def format_sentence(sentence, file):

    #without_parenthesis = delete_parenthesis(sentence)

    sentenceSplit = filter(None, sentence.split(". "))
    for s in sentenceSplit :
        line = s.strip() + "."
        print(line)
        #line = line.decode('UTF-8')
        try:
            file.write(line + '\r')
        except:
            pass




f = open('testing.txt','r', encoding='UTF-8')
contents = f.read()
#contents = contents.decode('UTF-8')

f2 = open('testing_result.txt', 'w')
format_sentence(contents, f2)

f.close()
f2.close()
