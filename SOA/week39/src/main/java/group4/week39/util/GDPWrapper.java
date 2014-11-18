package main.java.group4.week39.util;

import main.java.group4.week39.gdp.GDP;
import main.java.group4.week39.gdp.GDPService;
import main.java.group4.week39.gdp.NoSuchCountryException_Exception;

public class GDPWrapper {
	
	private GDPService gdpService;
	private GDP gdp;
	
	public GDPWrapper(){
		gdpService = new GDPService();
		gdp = gdpService.getGDPPort();
	}
	
	public Double getGDP(String countryCode) throws NoSuchCountryException_Exception{
		return gdp.getGDP(countryCode);
	}
}
