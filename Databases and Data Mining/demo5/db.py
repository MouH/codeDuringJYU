from pg8000 import DBAPI
import cPickle as p




def count_number(number_of_count):
    # store the count data in  [ time  ,   count  ]
    # time and count are also []


    ocuur_time = []
    count_time = []

    execu_sql = "SELECT to_char(times, 'MI') FROM TWITTER ORDER BY times ASC;" 
    cursor = dbhelper()
    try:
        cursor.execute(execu_sql)
        stick = '61'
        count = 0
        for row in cursor.fetchmany(number_of_count):
            if stick == '61':
                stick = row[0]
                count += 1

            if row[0] == stick:
                count += 1
            else:
                ocuur_time.append(stick)
                stick = row[0]
                count_time.append(count)
                count = 1
            stick = row[0]
        
    except Exception, e:
        pass
    
    a = [ocuur_time, count_time]
    f = file('./count', 'w')
    p.dump(a, f)
    f.close()
    cursor.close() 

def store_text(number_of_count):
    # store text in a []

    stored_text = []   
    execu_sql = "SELECT text FROM TWITTER;" 
    cursor = dbhelper()
    try:
        cursor.execute(execu_sql)
        for row in cursor.fetchmany(number_of_count):
            stored_text.append(row[0])
        
    except Exception, e:
        pass

    f = file('./text', 'w')
    p.dump(stored_text, f)
    f.close()
    cursor.close() 

def dbhelper():

    conn = DBAPI.connect(
        host = "vdb1.it.jyu.fi", 
        user = "hamou", 
        password = "3mV88tgw8U",
        database = "hamou_db")

    cursor = conn.cursor()
    return cursor
  
def main():
    count_number(2000)
    store_text(2000)

if __name__ == "__main__":
    main()