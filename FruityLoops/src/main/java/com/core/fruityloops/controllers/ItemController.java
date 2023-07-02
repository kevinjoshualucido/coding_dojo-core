package com.core.fruityloops.controllers;

import java.util.ArrayList;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import com.core.fruityloops.models.ItemClass;

@Controller
public class ItemController {
	
	@RequestMapping("/")
	public String index(Model model) {
		
		// Access constructor method in models package
		ArrayList<ItemClass> fruits = new ArrayList<ItemClass>();
		fruits.add(new ItemClass("pineapple", 4.99));
		fruits.add(new ItemClass("watermelon", 4.99));
		fruits.add(new ItemClass("papaya", 5.39));
		fruits.add(new ItemClass("raspberries", 3.99));
		fruits.add(new ItemClass("blueberries", 3.99));
		
		model.addAttribute("fruitsList", fruits);
		
		return "index.jsp";
	}
}
