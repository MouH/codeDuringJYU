package main.java.group4.week39.util;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import net.sf.json.JSONArray;
import net.sf.json.JSONObject;
import org.apache.http.HttpEntity;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.utils.URIBuilder;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

public class GeoCodingWrapper {
	private URIBuilder uriBuilder;
	private URI uri = null;
	private final String scheme = "https";
	private String lon;
	private String lat;
	private final String path = "/maps/api/geocode/json";
	private final String host = "maps.googleapis.com";
	
	public GeoCodingWrapper(String lat, String lon){
		this.lat = lat;
		this.lon = lon;
	}

	private String doHTTPRequest() throws ClientProtocolException, IOException{
		
		uriBuilder = new URIBuilder();
		uriBuilder.setHost(host).setPath(path);
		String latlng = lat + "," + lon;

		uriBuilder.addParameter("latlng", latlng);
		uriBuilder.addParameter("sensor", "false");
		uriBuilder.setScheme(scheme);
		try {
			uri = uriBuilder.build();
		} catch (URISyntaxException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		CloseableHttpClient httpclient = HttpClients.createDefault();
		HttpGet httpGet = new HttpGet(uri);
		CloseableHttpResponse response = httpclient.execute(httpGet);
		HttpEntity entity = response.getEntity();
		
		return EntityUtils.toString(entity);
	}
	
	private String phraseCountryCode(String json){
		if(json.length()<1){
			return "";
		}
		JSONArray respones = JSONObject.fromObject(json).getJSONArray("results");
		
		if(respones.size()==0){
			return "";
		}
		JSONArray address = respones.getJSONObject(respones.size()-1).getJSONArray("address_components");
		JSONObject country = address.getJSONObject(0);
		
		String countryCode = country.getString("short_name");
		return countryCode;
		
	}
	
	public String getCountryCode() throws ClientProtocolException, IOException{
		return phraseCountryCode(doHTTPRequest());
	}
}
