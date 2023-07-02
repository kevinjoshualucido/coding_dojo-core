<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<!-- YOUR own local CSS -->
<link rel="stylesheet" href="/css/main.css" />
<!-- YOUR own local JS -->
<script type="text/javascript" src="/js/app.js"></script>
<!-- For Bootstrap CSS -->
<link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css" />
<title>Fruity Loop</title>
</head>
<body>
	<h1 class="container mt-3 text-danger">Fruity Loop</h1>

	<div class="container mt-3">
		<table class="table border-danger">
			<thead>
				<tr>
					<th>Fruit</th>
					<th>Price</th>
				</tr>
			</thead>
			<tbody>
				<c:forEach var="oneFruit" items="${ fruitsList }">
					<tr>
						<td><c:out value="${ oneFruit.name }"/></td>
						<td><c:out value="${ oneFruit.price }"/></td>
					</tr>
				</c:forEach>
			</tbody>
		</table>
	</div>

</body>
</html>