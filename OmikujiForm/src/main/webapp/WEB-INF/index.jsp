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
		<h1>Send an Omikuji!</h1>
		
		<div>
			<form action="/post" method="post">
				<label>Pick any number between 5 to 25.</label>
				<input type="number" name="number"/>
				<label>Enter the name of any city.</label>
				<input type="text" name="city"/>
				<label>Enter the name of any real person!</label>
				<input type="text" name="person"/>
				<label>Enter professional endeavor or hobby.</label>
				<input type="text" name="hobby"/>
				<label>Enter any type of living thing.</label>
				<input type="text" name="thing"/>
				<label>Say something nice to someone.</label>
				<input type="text" name="message"/>
				<p>Send and show a friend</p>
				<input type="submit" value="Send"/>
			</form>
		</div>
	</div>

</body>
</html>