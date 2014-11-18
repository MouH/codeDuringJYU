package main.java.group4.week39.soap;
import java.util.concurrent.ExecutionException;

import javax.jws.WebService;

import main.java.group4.week39.util.GDPUtil;


//Service Implementation
@WebService(endpointInterface = "fi.jyu.ties456.group4.week39.soap.Soap")

public class SoapImpl implements Soap {
	

	@Override
	public String getfromGooglemaps(String lat, String lng) throws ExecutionException {
		GDPUtil gdpUtil = new GDPUtil();
		gdpUtil.setLatlng(lat,lng);
		return(gdpUtil.getGDP()).toString();
		
	}

}
