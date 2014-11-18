package main.java.group4.week39.soap;

import java.util.concurrent.ExecutionException;

import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.jws.soap.SOAPBinding;
import javax.jws.soap.SOAPBinding.Style;

import main.java.group4.week39.util.GDPUtil;
 
//Service Endpoint Interface
@WebService
@SOAPBinding(style = Style.RPC)
public interface Soap{
 
	
	
	
	@WebMethod String getfromGooglemaps(String lat, String lng) throws ExecutionException;
	
	
 


 
}
	
