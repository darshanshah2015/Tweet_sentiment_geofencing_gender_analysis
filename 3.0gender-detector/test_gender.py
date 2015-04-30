from gender_detector import GenderDetector
from wordsegment import segment
import csv,string
import re,math
import re
import itertools
#import names from the spreadshet
test_file = 'overall_1430382666.tsv'
csv_file = csv.DictReader(open(test_file, 'rb'), delimiter='\t', quotechar='"')
names= []
for line in csv_file:
    names.append((line['Author']))
word_final= []
rec=open("Names.txt", "w")

for item in names:
    rec.write("%s\n" % item)
rec.close()

with open("Names.txt", 'r') as word:
    for i in word:
        word_final.append(re.findall("[a-zA-Z]+", i.strip()))
        #word_final.append(word_processed)
#to correct the format we receive the words and take as a chain in list
word_final =list(itertools.chain(*word_final))
#print word_final
rec=open("Names_processed.txt", "w")

for item in word_final:
    rec.write("%s\n" % item)
rec.close()


for item in word_final:
    c= segment(item)
    d= max(c, key=len)
    #print d
    detector = GenderDetector('us') # It can also be uk.
    e= detector.guess(d) # => 'male'
    print d,e
   
    

"""
rec=open("Names_processed.txt", "w")

for item in word_final:
    rec.write("%s\n" % item)
rec.close()

 

with open("Names_processed.txt", 'r') as word:
    for i in word:
        word= re.findall("[a-zA-Z]+", i)
        c= segment(word)
        print c        
"""







detector = GenderDetector('us') # It can also be ar, uk, uy.

c= detector.guess('harry1234') # => 'male'

print c
