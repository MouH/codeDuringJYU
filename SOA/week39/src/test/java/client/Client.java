package test.java.client;

import java.net.URL;

import javax.xml.namespace.QName;
import javax.xml.ws.Service;

import main.java.group4.week39.soap.Soap;


 
public class Client{
 
	public static void main(String[] args) throws Exception {
 
	URL url = new URL("http://localhost:9999/soap?wsdl");
 
        //1st argument service URI, refer to wsdl document above
	//2nd argument is service name, refer to wsdl document above
        QName qname = new QName("http://soap.week39.group4.ties456.jyu.fi/", "SoapImplService");
 
        Service service = Service.create(url, qname);
 
        Soap soap = service.getPort(Soap.class);
        
        
 
        System.out.println(soap.getfromGooglemaps("40.714224","-73.961452"));
 
    }
 
}