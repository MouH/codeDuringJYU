package main.java.group4.week39.util;

import java.io.IOException;

import main.java.group4.week39.gdp.NoSuchCountryException_Exception;

import org.apache.http.client.ClientProtocolException;

public class GDPUtil {
	private String lat, lon;
	private String countryCode = "";
	
	
	public GDPUtil(){}
	
	public void setLatlng(String lat, String lon){
		this.lat = lat;
		this.lon = lon;
	}
	
	public String getCountryCode(){
		GeoCodingWrapper geoCodingWrapper = new GeoCodingWrapper(lat,lon);
		try {
			countryCode = geoCodingWrapper.getCountryCode();
		} catch (ClientProtocolException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
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
			return gdp.getGDP(countryCode);
		} catch (NoSuchCountryException_Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return 0.00;
	}
}
