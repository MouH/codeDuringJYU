import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class GenerateSQL {
	
	ArrayList<String> femaleFirstName;
	ArrayList<String> maleFirstName;
	ArrayList<String> lastName;
	String[] department = {"1","4","5"};
	
	public GenerateSQL(){
		femaleFirstName = new ArrayList<String>();
		maleFirstName = new ArrayList<String>();
		lastName = new ArrayList<String>();
		try {
			this.readffn();
			this.readln();
			this.readmfn();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	private void readffn() throws IOException{
		File file1 = new File("D:/course/jyu/demo3/src/ffnames.txt");
		FileReader fileReader1 = new FileReader(file1);
		BufferedReader reader1 = new BufferedReader(fileReader1);
		String line = null;
		
		while ((line = reader1.readLine()) != null) {
		    this.femaleFirstName.add(line.trim());
		}
//		System.out.println("successfully read female first name. size: " + this.femaleFirstName.size());
		
		reader1.close();
		fileReader1.close();
	}
	private void readmfn() throws IOException{
		File file = new File("D:/course/jyu/demo3/src/mfnames.txt");
		FileReader fileReader = new FileReader(file);
		BufferedReader reader = new BufferedReader(fileReader);
		String line = null;
		
		while ((line = reader.readLine()) != null) {
		    this.maleFirstName.add(line.trim());
		}
//		System.out.println("successfully read male first name. size: " + this.maleFirstName.size());
		reader.close();
		fileReader.close();
	}
	private void readln() throws IOException{
		File file = new File("D:/course/jyu/demo3/src/lnames.txt");
		FileReader fileReader = new FileReader(file);
		BufferedReader reader = new BufferedReader(fileReader);
		String line = null;
		
		while ((line = reader.readLine()) != null) {
		    this.lastName.add(line.trim());
		}
//		System.out.println("successfully read last name. size: " + this.lastName.size());
		reader.close();
		fileReader.close();
	}
	
	
	public String getSQL(int i){
//		int a = this.getRandomNumber(0, this.lastName.size()-1);
		
		String lastN = this.lastName.get(1);
//		System.out.println(lastN);
		String ssn = "73344" + i;
		String dno = this.department[this.getRandomNumber(0, this.department.length-1)];
		String gender;
		int salary = this.getRandomNumber(10000, 100000);
		String firstName;
		if(this.getRandomNumber(0, 1) == 0 ){
			gender = "M";
			firstName = this.maleFirstName.get(this.getRandomNumber(0, this.maleFirstName.size()-1));
		}
		else{
			gender = "F";
			firstName = this.femaleFirstName.get(this.getRandomNumber(0, this.femaleFirstName.size()-1));
		}
		
		String sql = "INSERT INTO EMPLOYEE (Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno) " 
				+ "VALUES ('" + firstName + "','T','" + lastN + "','" + ssn +"','1955-12-08','---','" + gender
				+ "','" + salary + "','888665555','" + dno + "');";

		return sql;
		
	}
	
	private int getRandomNumber(double start, double end){
		int a = (int) ( Math.random() * ( end - start ) + start + 0.5);
		return (int) Math.floor(a);
	}
}
