
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		GenerateSQL gs = new GenerateSQL();
		for(int i=1000;i<3000;i++){
			try {
				JDBCHelper.insertData(gs.getSQL(i));
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}

}
