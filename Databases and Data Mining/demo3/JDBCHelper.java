import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;


public class JDBCHelper {

	public static void insertData(String sqlExecute) throws Exception {

		try {
			 
			Class.forName("org.postgresql.Driver");
 
		} catch (ClassNotFoundException e) {
 
			System.out.println("Where is your PostgreSQL JDBC Driver? "
					+ "Include in your library path!");
			e.printStackTrace(); 
		}
 
		System.out.println("PostgreSQL JDBC Driver Registered!");
 
		Connection connection = null; 

		try {
				 
			connection = DriverManager.getConnection("jdbc:postgresql://vdb1.it.jyu.fi:5432/hamou_db", "hamou","3mV88tgw8U");
	 
		} catch (SQLException e) {
	 
			System.out.println("Connection Failed! Check output console");
			e.printStackTrace();
			return;
	 
		}
	 
		if (connection != null) {
			System.out.println("connected successfully!");
			Statement sql;
			try {
				sql = connection.createStatement();
				sql.executeQuery(sqlExecute);

			} catch (SQLException e) {
				System.out.println("Failed");
	            return;
			}
		}
		 else {
				System.out.println("Failed to make connection!");
			}
		}

	}


