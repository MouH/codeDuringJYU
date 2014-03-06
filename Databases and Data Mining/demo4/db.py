from pg8000 import DBAPI

# jdbc:postgresql://vdb1.it.jyu.fi:5432/hamou_db
#  "hamou","3mV88tgw8U"
Class DB_Helper{
	def execu(self, execu_sql){
        conn = DBAPI.connect(
	        host = "jdbc:postgresql://vdb1.it.jyu.fi:5432", 
	        user = "", 
	        password = "",
	        database = "hamou_db")

        cursor = conn.cursor()
        try:
        	cursor.execute(execu_sql)
        except Exception, e:
        	pass
        
        conn.commit()	
	}	
}
