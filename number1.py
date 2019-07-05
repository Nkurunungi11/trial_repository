from TwitterSearch import *
import csv
import datetime, time
#the start and end of our twitter data
mindate = datetime.date(2010, 1, 1)
maxdate = datetime.date(2016, 1, 1)

try:
    tso = TwitterSearchOrder() # create a tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['Uganda', 'Food']) # let's define all words we would like to have a look for
    #tso.set_count(600) #Maximum and default value is 100 pages
    tso.set_language('en') # we want to see English tweets only
    #tso.set_include_entities(False) # and don't give us all those entity information
    #tso.set_geocode(52.5233,13.4127,10,imperial_metric=False) # latitude,longitude,radius
    #tso.set_until(maxdate)
    #tso.set_result_type('mixed') #(<mixed,recent,popular>)
    #tso.set_locale('ja')
    
    ts = TwitterSearch(
    consumer_key = 'GiOVEQJZtlnattsMrtbl8FZcz',
    consumer_secret = 'H81NrCevKWDvAgRzChUKm8rgJRDnnRqyZLMKrjW1peKOcUqlbq',
    access_token = '726747169189945345-f51OIdFujB2qGrg8Vi3frrsUkWby8sf',
    access_token_secret = 'ECzoRAk6s3vbwtTZkhOEGt28ChYyGaoBXTxk9UAwnWhm5'
    )
    # Open/Create a file to append data
    csvFile = open('tweets.csv', 'ab')
    #Use csv Writer
    csvWriter = csv.writer(csvFile)

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        #print( '@%s tweeted: %s' % (  tweet['user']['screen_name'], tweet['text'] ) )
        print( tweet['created_at'], tweet['user']['screen_name'], tweet['text'] )

  

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)