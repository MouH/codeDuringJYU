 package fi.jyu.ties456.group4.week40.rest;


import java.net.URISyntaxException;
import java.util.concurrent.ExecutionException;

import javax.ws.rs.DefaultValue;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;

import javax.ws.rs.core.MediaType;


import fi.jyu.ties456.group4.week40.cache.GDPCache;
import fi.jyu.ties456.group4.week40.gdp.NoSuchCountryException_Exception;
import fi.jyu.ties456.group4.week40.util.GDPUtil;

import fi.jyu.ties456.group4.week40.util.ResponseJSON;


// Plain old Java Object it does not extend as class or implements 
// an interface

// The class registers its methods for the HTTP GET request using the @GET annotation. 
// Using the @Produces annotation, it defines that it can deliver several MIME types,
// text, XML and HTML. 

// The browser requests per default the HTML MIME type.

//Sets the path to base URL + /hello
//Plain old Java Object it does not extend as class or implements 
//an interface

//The class registers its methods for the HTTP GET request using the @GET annotation. 
//Using the @Produces annotation, it defines that it can deliver several MIME types,
//text, XML and HTML. 

//The browser requests per default the HTML MIME type.

//Sets the path to base URL + /hello
@Path("/localgdpservice")
public class LocalGDPService {

	
	
	// This method is called if XML is request
	@GET
	@Produces(MediaType.TEXT_PLAIN )
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
			
			String countryCode = null;
			try {
				countryCode = gdpUtil.getCountryCode();
			} catch (URISyntaxException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
			
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