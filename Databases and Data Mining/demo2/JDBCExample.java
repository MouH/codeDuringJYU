import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.SQLException;
import java.sql.*;


public class JDBCExample {
 
	public static void main(String[] argv) {
 
		System.out.println("-------- PostgreSQL "+ "JDBC Connection Testing ------------");
 
		try {
 
			Class.forName("org.postgresql.Driver");
 
		} catch (ClassNotFoundException e) {
 
			System.out.println("Where is your PostgreSQL JDBC Driver? "
					+ "Include in your library path!");
			e.printStackTrace();
			return;
 
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
			ResultSet results = sql.executeQuery(" SELECT Fname, Lname FROM EMPLOYEE INNER JOIN DEPARTMENT ON EMPLOYEE.Dno=DEPARTMENT.Dnumber and DEPARTMENT.Dname = 'Research'; ");
    			if (results != null)
    			{
      				while (results.next())
      				{
        				System.out.println("Name = "+results.getString(1)+"\n");
      				}
    			}
			
	    			results.close();
			} catch (SQLException e) {
                System.out.println("Failed");
                return;
                }
		} else {
			System.out.println("Failed to make connection!");
		}
	}
 
}
