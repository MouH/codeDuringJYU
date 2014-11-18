package main.java.group4.week39.main;

import main.java.group4.week39.util.GDPUtil;

public class Test {
	public static void main(String[] args) {
		GDPUtil gdpUtil = new GDPUtil();
		gdpUtil.setLatlng("40.714224", "73.961452");
		System.out.println(gdpUtil.getCountryCode());
	}
}
