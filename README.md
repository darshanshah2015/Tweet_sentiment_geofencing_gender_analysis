# Tweet_sentiment_geofencing_gender_analysis
1.0 Collect tweets is the folder containing files that collect streaming data from twitter. It makes use of twitter streaming API , <a href="https://github.com/tweepy/tweepy">tweepy</a> and a few other libraries to work. However, these libraries were not perfect. They needed quite a bit working on to get the inflow of tweets going. Geofencing can be acheived by tweaking the code inside streaming.py. I have provided comments in the file for reference. For extensive details, read the README file in the respective folders.

2.0 Sentiment analysis contains the part where the actual Sentiment analysis is performed. Again, read the README file in folder for more details.

3.0 gender detector detects the gender to the user based on their user name.

3.1 Word segment is required for gender detection, it segments the username into feedable 'human' names.

