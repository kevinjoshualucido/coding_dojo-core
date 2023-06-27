package com.kevinlucido.daikichi.controllers;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/daikichi")
public class DaikichiPathVariables {
	@RequestMapping("")
	public String index() {
		return "Welcome!";
	}
	@RequestMapping("/today")
	public String today() {
		return "Today you will find luck in all your endeavors!";
	}
	@RequestMapping("/tomorrow")
	public String tomorrow() {
		return "Tomorrow, an opportunity will arise, so be sure to be open to new ideas!";
	}
	
	
	// PATH VARIABLE MAPPING
	@RequestMapping("/travel/{city}")
	public String showCity(@PathVariable("city") String city) {
		return "Congrats! You'll soon be travelling to " + city;
	}
	@RequestMapping("/lotto/{num}")
	public String fortune(@PathVariable("num") int num) {
		if (num % 2 == 0) {
			String thisOne = new String( "You will take a grand journey in the near future, but be weary of tempting offers" );
			return thisOne;
		}
		else if (num % 2 == 1) {
			String thisTwo = new String ("You have enjoyed the fruits of your labor but now is a great time to spend time with family and friends." );
			return thisTwo;
		}
		return null;
	}
	
}
