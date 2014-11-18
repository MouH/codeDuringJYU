package main.java.group4.week39.soap;

import javax.xml.ws.Endpoint;


public class SoapEndpintPuplisher {
	
	 
		public static void main(String[] args) {
		   Endpoint.publish("http://localhost:9999/soap", new SoapImpl());
	    }

}
