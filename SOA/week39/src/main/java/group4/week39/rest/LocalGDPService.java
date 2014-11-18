package main.java.group4.week39.rest;


import java.util.concurrent.ExecutionException;

import javax.ws.rs.DefaultValue;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;






import main.java.group4.week39.cache.GDPCache;
import main.java.group4.week39.gdp.NoSuchCountryException_Exception;
import main.java.group4.week39.util.GDPUtil;
import main.java.group4.week39.util.ResponseJSON;


// Plain old Java Object it does not extend as class or implements 
// an interface

// The class registers its methods for the HTTP GET request using the @GET annotation. 
// Using the @Produces annotation, it defines that it can deliver several MIME types,
// text, XML and HTML. 

// The browser requests per default the HTML MIME type.

//Sets the path to base URL + /hello
@Path("/localgdpservice")
public class LocalGDPService {

	
	
	// This method is called if XML is request
	@GET
	@Produces(MediaType.APPLICATION_JSON)
	public String getGDP(
			@DefaultValue("") @QueryParam("lat") String lat,
			@DefaultValue("") @QueryParam("lon") String lon) throws ExecutionException {
		if(lat.length() == 0 || lon.length() == 0){
			ResponseJSON responseJSON = new ResponseJSON(0.00, "not enghout parameters");
			return responseJSON.doResponse();
		}
		else{			
			GDPUtil gdpUtil = new GDPUtil();
			gdpUtil.setLatlng(lat, lon);
			System.out.println("1");
			String countryCode = gdpUtil.getCountryCode();
			System.out.println("2");
			if(countryCode == ""){
				ResponseJSON responseJSON = new ResponseJSON(0.00, "no gdp data of this country");
				return responseJSON.doResponse();
			}
			else{

				Double gdpCached =null;
				try {
					gdpCached = GDPCache.getGDP(countryCode);
					
				} catch (NoSuchCountryException_Exception e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}

				ResponseJSON responseJSON;
				responseJSON = new ResponseJSON(gdpCached, "");
				return responseJSON.doResponse();

			}
		}
	}
} 