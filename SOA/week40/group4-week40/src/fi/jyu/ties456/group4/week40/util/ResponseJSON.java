package fi.jyu.ties456.group4.week40.util;

import java.util.HashMap;
import java.util.Map;

import net.sf.json.JSONObject;

public class ResponseJSON {
	private Double GDP;
	private String error;
	
	public ResponseJSON(Double GDP, String error){
		this.GDP = GDP;
		this.error = error;
	}
	
	public String doResponse(){
		Map map = new HashMap();  
		map.put( "error", this.error ); 
		map.put( "GDP", this.GDP ); 
		JSONObject jsonObject = JSONObject.fromObject( map ); 
		return jsonObject.toString();
	}
	

}
