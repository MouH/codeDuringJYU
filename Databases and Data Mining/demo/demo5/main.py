from twitter import *
import json
from pg8000 import DBAPI

# jdbc:postgresql://vdb1.it.jyu.fi:5432/hamou_db
#  "hamou","3mV88tgw8U"
Month = {
    'Jan' : '01',
    'Feb' : '02',
    'Mar' : '03',
    'Apr' : '04',
    'May' : '05',
    'Jun' : '06',
    'Jul' : '07',
    'Aug' : '08',
    'Sep' : '09',
    'Oct' : '10',
    'Nov' : '11',
    'Dec' : '12'
}

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
    try:
        text = tweet["text"]

        coordinates = tweet['coordinates']['coordinates']
        geo = str(coordinates[0]) + ',' + str(coordinates[1])

        city_name = tweet['place']['name']
        country_code = tweet["place"]["country_code"]

        created_at = tweet['created_at'].split()
        times = created_at[-1]+'-'+Month[created_at[1]]+'-'+created_at[2]
        times = times+' '+created_at[3]
        
        execu_sql = "INSERT INTO TWITTER (text, city, country, geo, times) VALUES ('" + text +"','" + city_name +"','" + country_code + "','" + geo + "','" + times + "');"

        execu(execu_sql)
        print "insert success" + str(text)

    except Exception, e:
        continue