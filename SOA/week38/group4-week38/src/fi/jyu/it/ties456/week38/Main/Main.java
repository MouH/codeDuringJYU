package fi.jyu.it.ties456.week38.Main;

import fi.jyu.it.ties456.week38.services.courses.StudentISService;
import fi.jyu.it.ties456.week38.services.people.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
//import java.io.InputStreamReader;
import java.util.ArrayList;

import org.omg.CORBA.SystemException;

/**
 * @author Jussi
 * 
 */
public class Main {

	/**
	 * @param args
	 * @throws IOException
	 */
	public static void main(String[] args) throws IOException {
//		SearchForPerson somebody = new SearchForPerson();
		System.out.print("Enter: search,create or quit \n");
		
		String courseName;
		String tID;
		int credit=-1;
		String shortDesc;


		// open up standard input
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
		String word = br.readLine();
		while (!(word.equals("quit"))){
			if (word.equals("search")){
				System.out.print("Please give a name: \n");
				word = br.readLine();
				
				PeopleRegistryService peopleRegistryService = new PeopleRegistryService();
				ArrayList<PersonInfoType> list = (ArrayList<PersonInfoType>) peopleRegistryService.getPeopleRegistryPort().searchForPerson(word);  
				for(int i = 0; i < list.size(); i++ ) {
					System.out.println(list.get(i).getEmailAddress());
					System.out.println(list.get(i).getFirstname());
					System.out.println(list.get(i).getId());
				}
			}
				// do something

			if (word.equals("create")){
				
				System.out.print("Please give a course name: \n");
				courseName = br.readLine();
				
				System.out.print("Please give a teacher's ID: \n");
				tID = br.readLine();
				System.out.print("Please give number of credits: \n");

				while(credit<0){
					try {
						credit = Integer.parseInt(br.readLine());
					}  catch(NumberFormatException e){
						System.out.print("Please input a number: \n");
					}
				}

				System.out.print("Please give a short description: \n");
				shortDesc = br.readLine();
				
				StudentISService studentISService = new StudentISService();
				String courseID = studentISService.getStudentISPort().createCourse(courseName, tID, credit, shortDesc);
				System.out.print(courseID);
			}
				
			else	 	
				System.out.print("Enter: search,create or quit \n");
				
			try {
				word = br.readLine();

			} catch (IOException ioe) {
						System.out.println("IO error to read!");
						System.exit(1);
				}
		}

	}

}
