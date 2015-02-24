<%@taglib uri="http://www.springframework.org/tags/form" prefix="form"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="s" uri="http://www.springframework.org/tags"%>

<html>
    <head>
        <title> <s:message code="title" /> </title>
    </head>
    <body>

     <c:if test="${not empty customerList}">


                <table border="1px">
                      <tr>
                        <th> <s:message code="firstName" /> </th>
                        <th> <s:message code="lastName" /> </th>
                      </tr>
                  <c:forEach var="customer" items="${customerList}">
                      <tr>

                       <td>${customer.firstName}</td>
                       <td>${customer.lastName}</td>
                     </tr>
                   </c:forEach>
                 </table>
        </c:if>




    </body>
</html>
