package fi.jyu.ties456.group4.week40.util;

import java.net.URISyntaxException;
import fi.jyu.ties456.group4.week40.gdp.NoSuchCountryException_Exception;

public class GDPUtil {
	private String lat, lon;
	String countryCode = "";
	
	
	public GDPUtil(){}
	
	public void setLatlng(String lat, String lon){
		this.lat = lat;
		this.lon = lon;
	}
	
	public String getCountryCode() throws URISyntaxException{
		GeoCodingWrapper geoCodingWrapper = new GeoCodingWrapper(lat,lon);

		countryCode = geoCodingWrapper.getCountryCode();

		if(countryCode.length() == 0){
			return "";
		}
		else{
			return countryCode;
		}

	}
	
	public Double getGDP(){

		GDPWrapper gdp = new GDPWrapper();
		try {
			return gdp.getAGDP(countryCode);
		} catch (NoSuchCountryException_Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return 0.00;
	}
}
