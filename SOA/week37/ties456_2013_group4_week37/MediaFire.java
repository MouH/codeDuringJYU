package ties456_2013_group4_week37;

import java.io.*;
import java.net.URI;
import java.net.URISyntaxException;

import javax.xml.parsers.ParserConfigurationException;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;

import org.apache.commons.codec.digest.DigestUtils;
import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.utils.URIBuilder;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.xml.sax.InputSource;

public class MediaFire {
	public String applicationID;
	public String apiKey;
	public String sessionToken = "";
	public UserInfo userInfo;
	
	public MediaFire(String applicationID, String apikey){
		this.applicationID = applicationID;
		this.apiKey = apikey;
	}
	
	public void connect(String email, String password) throws IOException, AuthenticationException, URISyntaxException, ParserConfigurationException, XPathExpressionException{
		//get the sessionToken
		
		//get signature
		String original = email+password+applicationID+apiKey;
		String signature = DigestUtils.shaHex(original);
		
		URIBuilder builder = new URIBuilder("https://www.mediafire.com/api/user/get_session_token.php");
		builder.addParameter("email", email);
		builder.addParameter("password", password);
		builder.addParameter("application_id", this.applicationID);
		builder.addParameter("signature", signature);
		
		URI uri = null;
		try {
			uri = builder.build();
		} catch (URISyntaxException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		//get_session_token
		CloseableHttpClient httpclient = HttpClients.createDefault();
		HttpGet httpGet = new HttpGet(uri);
		CloseableHttpResponse response1 = httpclient.execute(httpGet);
		// The underlying HTTP connection is still held by the response object
		// to allow the response content to be streamed directly from the network socket.
		// In order to ensure correct deallocation of system resources
		// the user MUST either fully consume the response content  or abort request
		// execution by calling CloseableHttpResponse#close().

		try {
		    System.out.println(response1.getStatusLine());
		    HttpEntity entity1 = response1.getEntity();
		    // do something useful with the response body
		    
		    //get the session_tokem
		    String xmlString = EntityUtils.toString(entity1);
	        //DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
	        //DocumentBuilder db = factory.newDocumentBuilder();
	        InputSource inStream = new InputSource();
	        inStream.setCharacterStream(new StringReader(xmlString));
		    XPathFactory factory1 = XPathFactory.newInstance();
		    XPath path = factory1.newXPath();
		    sessionToken = path.evaluate("/response/session_token", inStream);
		    System.out.print(sessionToken);
		    
		    // and ensure it is fully consumed
		    EntityUtils.consume(entity1);
		} finally {
		    response1.close();
		}
	}
	
	public UserInfo getInfo() throws IOException, AuthenticationException, URISyntaxException, XPathExpressionException, ParserConfigurationException{
		userInfo = new UserInfo();
		URIBuilder uri = new URIBuilder("http://www.mediafire.com/api/user/get_info.php");
		uri.addParameter("session_token", sessionToken);
		
		//get_info
		
		//send user get_info
		CloseableHttpClient httpclient = HttpClients.createDefault();
		HttpGet httpGet = new HttpGet(uri.toString());
		CloseableHttpResponse response1 = httpclient.execute(httpGet);
		// The underlying HTTP connection is still held by the response object
		// to allow the response content to be streamed directly from the network socket.
		// In order to ensure correct deallocation of system resources
		// the user MUST either fully consume the response content  or abort request
		// execution by calling CloseableHttpResponse#close().

		try {
		    System.out.println(response1.getStatusLine());
		    HttpEntity entity2 = response1.getEntity();
		    // do something useful with the response body
		    
		    //get the session_tokem
		    String xmlString = EntityUtils.toString(entity2);
	        //DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
	        //DocumentBuilder db = factory.newDocumentBuilder();
	        InputSource inStream = new InputSource();
	        inStream.setCharacterStream(new StringReader(xmlString));
	        
		    XPathFactory factory1 = XPathFactory.newInstance();
		    XPath path = factory1.newXPath();
		    
		    
		    //save to userInfo
		    userInfo.setEmail(path.evaluate("/response/user_info/email", inStream));
		    inStream.setCharacterStream(new StringReader(xmlString));
		    
		    userInfo.setFirstName(path.evaluate("/response/user_info/first_name", inStream));
		    inStream.setCharacterStream(new StringReader(xmlString));
		    
		    userInfo.setLastName(path.evaluate("/response/user_info/first_name", inStream));
		    inStream.setCharacterStream(new StringReader(xmlString));
		    
		    userInfo.setDisplayName(path.evaluate("/response/user_info/displayName", inStream));
		    inStream.setCharacterStream(new StringReader(xmlString));
		    
		    userInfo.setGender(path.evaluate("/response/user_info/gender", inStream));
		    inStream.setCharacterStream(new StringReader(xmlString));
		    
		    userInfo.setBirthDate(path.evaluate("/response/user_info/birthDate", inStream));
		    inStream.setCharacterStream(new StringReader(xmlString));
		    
		    userInfo.setLocation(path.evaluate("/response/user_info/location", inStream));
		    inStream.setCharacterStream(new StringReader(xmlString));
		    
		    userInfo.setWebsite(path.evaluate("/response/user_info/website", inStream));
		    inStream.setCharacterStream(new StringReader(xmlString));
		    
		    userInfo.setPremium(path.evaluate("/response/user_info/premium", inStream));
		    inStream.setCharacterStream(new StringReader(xmlString));
		    
		    userInfo.setBandwidth(path.evaluate("/response/user_info/bandwidth", inStream));
		    inStream.setCharacterStream(new StringReader(xmlString));
		    
		    userInfo.setCreated(path.evaluate("/response/user_info/created", inStream));
		    inStream.setCharacterStream(new StringReader(xmlString));
		    
		    boolean a = ( path.evaluate("/response/user_info/first_name", inStream)  == "yes" );
		    userInfo.setValidated(a);

		    
		    // and ensure it is fully consumed
		    EntityUtils.consume(entity2);
		} finally {
		    response1.close();
		}
		
		return userInfo;
	}
}
