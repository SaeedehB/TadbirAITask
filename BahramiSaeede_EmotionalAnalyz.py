'''auther : Saeedeh Bahrami'''
'''I set the pathes of csv_file and csv_file2 files
   based on my system path to read the Data files,
   For running the code on your system,
   please change these [ csv_file and csv_file2] '''

#---------------------------------------------------------------------#
import csv
from collections import defaultdict
import re
import nltk
from nltk.corpus import stopwords
from afinn import Afinn
import pandas as pd

stop = stopwords.words('english')
from nltk.corpus import wordnet

'''------------------------------------------------------------------------------------------------------------'''
''' reading the list of entity '''

csv_file = r'C:\Users\bahrami\Desktop\work\Tadbir\TadbirAITask-master\Data\Entities.csv'
columns = defaultdict(list)  # each value in each column is appended to a list

with open(csv_file) as f:
    reader = csv.DictReader(f)  # read rows into a dictionary format
    for row in reader:  # read a row as {column1: value1, column2: value2,...}
        for (k, v) in row.items():  # go over each column name and value
            columns[k].append(v)  # append the value into the appropriate list
            # based on column name k

list_entity = columns['Company']
Category = columns['Sector']

# print(list_entity,' , ',Category)
print('-----------------------------------------------------------------------')
'''------------------------------------------------------------------------------------------------------------'''
''' extracting the list of entity in the News data written by Saeedeh Bahrami'''

def check_entity(String,counter):

    # print('string = ', String)
    Sentences = nltk.sent_tokenize(String)
    Tokens = []
    for Sent in Sentences:
        Tokens.append(nltk.word_tokenize(Sent))
    Words_List = [nltk.pos_tag(Token) for Token in Tokens]
    # print('wordlist = ', Words_List)

    Nouns_List = []

    for List in Words_List:
        for Word in List:
            # print('Word = ', Word)
            if (Word[0] != '[') & (Word[0] !='``'):
                Nouns_List.append(Word[0])
                break

    # print('----------------------------------------------')
    # print('Nouns_List = ', Nouns_List)
    Names = []
    for Nouns in Nouns_List:
        if not wordnet.synsets(Nouns):
            Names.append(Nouns)

    # print (Names)
    # print(len(Names))
    # print (Names)
    Names = Names[0]
    str_name = str([Names])

    s = str_name
    start = str_name.find('') + 0
    end = str_name.find('-', start)
    str_name = str_name[start:end] + "']"

    print('entity name = ', str_name)
    start=String.find('-', start)+1
    end=String.find('-NA', start)
    News_content=String[start:end]
    # print(News_content)
    my_dict = [{'news_headline':str_name, 'news_article':News_content}]

    return str_name,News_content
'''--------------------------------------------------------------------------------------------------------'''
print('This code is written by Saeedeh Bahrami')
print('extract the Entity Names with the emothinal News analysis based on the related Entity')
print('**********************************************************************************************************')
csv_file2 = r'C:\Users\bahrami\Desktop\work\Tadbir\TadbirAITask-master\Data\News.csv'


f = open(csv_file2)
csv_f = csv.reader(f)
News_list = []

af = Afinn()
counter = 0
for row in csv_f:
    News_list.append(row[0])
    if counter < 3000:
        String = str([News_list[counter]])
        # if counter==1:
        [entity,News_content]=check_entity(String,counter)
        score=af.score(News_content)
        if score>0:
            # dic_analyz = [{'News': News_content, ' Overall_Score': 'Positive'}]
            # print(dic_analyz)
            print('News : ', News_content)
            print('Overall_Score is ', ' Positive')
        elif score<0:
            # dic_analyz = [{'News': News_content, ' Overall_Score': 'Negative'}]
            # print(dic_analyz)
            print('News : ', News_content)
            print('Overall_Score is ', ' Negative')
        else:
            # dic_analyz = [{'News': News_content, ' Overall_Score': 'Neutral'}]
            # print(dic_analyz)
            print('News : ', News_content)
            print('Overall_Score is ', ' Neutral')
        print('----------------------------------------------------------------------------------------------------------------------')
    counter = counter + 1







