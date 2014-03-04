package fi.jyu.it.ties456.week38.Main;

import java.io.IOException;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


import fi.jyu.it.ties456.week38.services.people.PeopleRegistryService;
import fi.jyu.it.ties456.week38.services.people.PersonInfoType;

/**
 * Servlet implementation class SearchPeopleServlet
 */
@WebServlet("/SearchPeopleServlet")
public class SearchPeopleServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

    /**
     * Default constructor. 
     */

    public ArrayList<PersonInfoType> searchPeople(String searchValue){
		PeopleRegistryService peopleRegistryService = new PeopleRegistryService();
		ArrayList<PersonInfoType> list = (ArrayList<PersonInfoType>) peopleRegistryService.getPeopleRegistryPort().searchForPerson(searchValue);  

		
		return list;
   
    }
	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doPost(request,response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		String searchValue = request.getParameter("searchValue");
		
		ArrayList<PersonInfoType> people = this.searchPeople(searchValue);
		if (people.size()>0) {
//			String ID = people.get(0).getId();
//			PersonInfoType person = people.get(0);
			request.setAttribute("people", people);
			request.getRequestDispatcher("index.jsp").forward(request,response);
		}
		else{
			request.getRequestDispatcher("index.jsp").forward(request,response);
		}
		
	}

}
