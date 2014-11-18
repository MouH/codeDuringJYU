<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jstl/core_rt"%>
    
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<script language="javascript" type="text/javascript">
function clearText(field){

    if (field.defaultValue == field.value) field.value = '';
    else if (field.value == '') field.value = field.defaultValue;

}
</script>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
<form method="post" action="SearchPeopleServlet">
	Please input the value to search <input name="searchValue" value="" type="text"><br>

	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" value="Search">
</form>
<hr />


<c:forEach var="p" items="${people}">
<tr>
	<td  align="center" ><c:out value="${p.getId()}"/> </td>
	<td  align="center" ><c:out value="${p.getEmailAddress()}"/> </td>
	<td  align="center" ><c:out value="${p.getFirstname()}"/> </td>
	<td  align="center" ><c:out value="${p.getSurname()}"/> </td>

</tr>
<br />
</c:forEach>

<hr />

<form method="post" action="CreateCourseServlet">
	Please input the course name <input name="name" value="" type="text"><br>
	Please input the teacher's ID<input name="tID" value="" type="text"><br>
	Please input the course credit<input name="credit" value="" type="text"><br>
	Please input a short description<input name="des" value="" type="text"><br>	

	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" value="Submit">	
</form>
<hr />

${courseID}


</body>
</html>