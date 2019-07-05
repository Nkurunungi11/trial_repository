import json
import urllib2

'''  aboutn the api and the key, see the links above'''

''' step 1: input query information'''

apiUrl='thhp://api.nytimes.com/svc/search/v1/article?format=json'

query = 'query=occupy+wall+street' # set the query word here

apiDate='begin_date=20110901&end_date=20120214' #set teh date here

fields='fields=body%2Curl%2Ctitle%2Cdate%2Cdes_facet%2Cdesk_facet%2Cbyline'

offset='offset=0'

key='api-key=c2c5b91680.......2811165' #input your key here


'''
step 2:get the numberof offset/pages'''

link=[apiUrl,query,apiDate, fields,offset,key]
ReqUrl='&'.join(link)
jstr=urllib2.urlopen(ReqUrl).read() #t=jstr.strip('()')

ts =json.loads( jstr )
number = ts['total'] #the number of queries #query = ts['tokens'] #result = ts['results']

print number
seq =range(number/9) # this is not a good way

print seq

''' step 3:crawl the data and dump into csv'''

import csv

addressForSavingData ="D:/Research/Dropbox/tweets/wapor_assessing online opinion/News coverage of ows/nyt.csv"

file = open(addressForSavingData, 'wb') #save to csv file

for i in seq:

	nums =str(i)

	offsets =".join(['offset=', nums]")

	links=[apiUrl, query,apiDate,Fields, offsets,key]

	ReqUrls ='&'.join(links)

	print"*____________*", ReqUrls

	jstrs =urllib2.urlopen(ReqUrls).read()

	t =jstrs.strip('()')

	tss =json.loads(t) # error no joson object

	result =tss['results']

	for ob in result:
		title=ob['title'] #body = ob['body'] #body,url,title,date,des_facet,desk_facet,byline

		print title

		url=ob['url']

		date=ob['date'] # desk_facet=ob['desk_facet'] #byline=ob['byline'] #some author names dont exist

		w=csv.writer(file,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		w.writerow((date,title,url)) # write it out

	file.close()
	
	pass	
