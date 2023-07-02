<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Omikuji</title>
</head>
<body>
	<div>
		<div>
			<h3>
				In <span><c:out 
						value="${ number }" /></span> years, you will be living in <span><c:out 
						value="${ city }" /></span> with <span><c:out
						value="${ person }" /></span> as your roommate, <span><c:out
						value="${ hobby }" /></span> for a living. The next time you see a <span><c:out
						value="${ thing }" /></span>, you will have good luck. Also, <span><c:out
						value="${ message }" /></span>.
			</h3>
		</div>
		<a href="/">Go Back</a>
	</div>
</body>
</html>