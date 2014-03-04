from twitter import *
import json
from pg8000 import DBAPI

# jdbc:postgresql://vdb1.it.jyu.fi:5432/hamou_db
#  "hamou","3mV88tgw8U"

def execu(execu_sql):
    conn = DBAPI.connect(
        host = "vdb1.it.jyu.fi", 
        user = "hamou", 
        password = "3mV88tgw8U",
        database = "hamou_db")

    cursor = conn.cursor()
    try:
        cursor.execute(execu_sql)
        print "success once"
    except Exception, e:
        print "fails"       
    conn.commit()

auth = OAuth(
    consumer_key = 'MaoPys1yBGIePQ3nPn5Mw',
    consumer_secret = 'xurs56ytLpMmreOFA7tiaCb1pchDqL9RtYky3gzYvU',
    token = '1868897340-QWHiIvzIGvAkurgjSr4bFrDXNY7ZC09uZjSeRBf',
    token_secret = 'liHATGOkxpMfhhkvT1s8n6imm37ZDsSUfCF3jLmr3kg7v'
)

stream = TwitterStream(auth=auth)

for tweet in stream.statuses.sample():
    if tweet.get("text") and tweet['user']['lang'] == 'en' and tweet['place'] != 'null':
        try:
            # print tweet["text"]
            text = tweet["text"]
            city_name = tweet['place']['name']
            country_code = tweet["place"]["country_code"]
            print country_code
            execu_sql = "INSERT INTO TWITTER (text, city, country) VALUES ('" + text +"','" + city_name +"','" + country_code + "');"
            print execu_sql
            execu(execu_sql)

            # print "\n"
        except Exception, e:
            # print "shit"
            continue

            


