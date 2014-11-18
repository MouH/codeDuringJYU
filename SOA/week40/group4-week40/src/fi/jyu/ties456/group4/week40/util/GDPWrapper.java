package fi.jyu.ties456.group4.week40.util;

import fi.jyu.ties456.group4.week40.gdp.GDP;
import fi.jyu.ties456.group4.week40.gdp.GDPService;
import fi.jyu.ties456.group4.week40.gdp.NoSuchCountryException_Exception;

public class GDPWrapper {
	
	private GDPService gdpService;
	private GDP gdp;
	
	public GDPWrapper(){
		gdpService = new GDPService();
		gdp = gdpService.getGDPPort();
	}
	
	public Double getAGDP(String countryCode) throws NoSuchCountryException_Exception{
		return gdp.getGDP(countryCode);
	}
}
