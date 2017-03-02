import string,csv
import itertools
from nltk.corpus import stopwords
from collections import Counter
import re
from itertools import islice, izip

fin = open("item.csv",'r') # to remove utf character
raw_data = fin.read().lower()
ascii_data=raw_data.decode('unicode_escape').encode('ascii','ignore')
fout= open("Final.csv", "w+")
fout.write(ascii_data)
fout.close()
fin.close()

word=[]



data = open("Final.csv").read()
data_list = data.split('\n')


pos_sent = open("keyword.txt").read()
positive_words=pos_sent.split('\n')
positive_counts=[]

result = []

for data in data_list:
    positive_counter=0
    
    
    data_processed=data.lower()
    
    
    

    words=data_processed.split(' ')
    word_count=len(words)
    for word in words:
        if word in positive_words:
            #print word+ 'positive'
            positive_counter=positive_counter+1
        
   
    positive_counts.append(positive_counter/word_count)
    

    if positive_counter > 0 :
        result.append("True")
    else :
        result.append("False");
    


data1 = open("item1.csv").read()
data_list1 = data1.split('\n')


output=zip(data_list1,result) 

with open('Final.csv', 'w+') as f:
    writer = csv.writer(f)
    writer.writerows(output)
	
