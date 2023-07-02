package com.core.fruityloops.models;

public class ItemClass {
	// Member Variables
	private String fruitName;
	private double price;
	
	// Constructor
	public ItemClass(String fruitName, double price) {
		this.fruitName = fruitName;
		this.price = price;
	}
	
	// Getters
	public String getName() {
		return fruitName;
	}
	public double getPrice() {
		return price;
	}
	
	// Setters
	public void setName(String name) {
		this.fruitName = name;
	}
	public void setPrice(double price) {
		this.price = price;
	}
	
}
