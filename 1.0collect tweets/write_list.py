import csv,string
import re,math

test_file = 'Sentiment_Analysis_Subset.csv'
#test_file = 'Dataset/Dataset.csv'
csv_file = csv.DictReader(open(test_file, 'rb'), delimiter=',', quotechar='"')

pos_tweets = []
neg_tweets = []

for line in csv_file:
    if line['Sentiment']=='1':
        pos_tweets.append((line['SentimentText']))
    else:
        neg_tweets.append((line['SentimentText']))

pos=open("positive.txt", "w")

for item in pos_tweets:
    pos.write("%s\n" % item)
pos.close()

neg=open("negative.txt", "w")

for item in neg_tweets:
    neg.write("%s\n" % item)
neg.close()
