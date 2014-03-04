package fi.jyu.it.ties456.week38.Main;


import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import fi.jyu.it.ties456.week38.services.courses.StudentISService;

/**
 * Servlet implementation class CreateCourseServlet
 */
@WebServlet("/CreateCourseServlet")
public class CreateCourseServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

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
		String name = request.getParameter("name");
		String tID = request.getParameter("tID");
		int credit = Integer.parseInt(request.getParameter("credit"));
		String shortDesc = request.getParameter("des");
		
		StudentISService studentISService = new StudentISService();
		String courseID = studentISService.getStudentISPort().createCourse(name, tID, credit, shortDesc);
		
		request.setAttribute("courseID", courseID);
		request.getRequestDispatcher("index.jsp").forward(request,response);
		
		
	}

}
