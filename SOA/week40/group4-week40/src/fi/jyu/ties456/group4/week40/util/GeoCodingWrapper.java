package fi.jyu.ties456.group4.week40.util;

import java.net.URISyntaxException;
import net.sf.json.JSONArray;
import net.sf.json.JSONObject;
import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.WebResource;

public class GeoCodingWrapper {
	private String lon;
	private String lat;
	
	public GeoCodingWrapper(String lat, String lon){
		this.lat = lat;
		this.lon = lon;
	}
	
	private String phraseCountryCode(String string){
		JSONArray respones = JSONObject.fromObject(string).getJSONArray("results");
		if(respones.size()==0){
			return "";
		}
		JSONArray address = respones.getJSONObject(respones.size()-1).getJSONArray("address_components");

		JSONObject country = address.getJSONObject(0);
		String countryCode = country.getString("short_name");

		return countryCode;
		
	}
	
	public String getCountryCode() throws URISyntaxException{
		return doHTTPRequest();
	}
	
	private String doHTTPRequest() throws URISyntaxException{

			 
			Client c = Client.create();
			
			WebResource baseResource;
			
			String geocodingURI = null;

            	geocodingURI = "http://maps.googleapis.com/maps/api/geocode/json";

	 
            baseResource = c.resource(geocodingURI);

            WebResource r = baseResource.queryParam("latlng", this.lat + "," + this.lon)
            		.queryParam("sensor", "false");
            return phraseCountryCode(r.get(String.class));

	}
}
