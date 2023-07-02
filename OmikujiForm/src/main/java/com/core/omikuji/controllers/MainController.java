package com.core.omikuji.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import jakarta.servlet.http.HttpSession;

@Controller
public class MainController {
	@GetMapping("/")
	public String index() {
		return"redirect:/omikuji";
	}
	
	@GetMapping("/omikuji")
	public String home() {
		return "index.jsp";
	}
	
	@PostMapping("/post")
	public String submit(
			@RequestParam(value="number") int number,
			@RequestParam(value="city") String city,
			@RequestParam(value="person") String person,
			@RequestParam(value="hobby") String hobby,
			@RequestParam(value="thing") String thing,
			@RequestParam(value="message") String message,
			HttpSession session
			) {
		session.setAttribute("number", number);
		session.setAttribute("city", city);
		session.setAttribute("person", person);
		session.setAttribute("hobby", hobby);
		session.setAttribute("thing", thing);
		session.setAttribute("message", message);
		return "redirect:/omikuji/show";
	}
	
	@GetMapping("/omikuji/show")
	public String show() {
		return "show.jsp";
	}
}
