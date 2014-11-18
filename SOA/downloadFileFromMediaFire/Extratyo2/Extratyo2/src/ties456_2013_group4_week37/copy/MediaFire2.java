package ties456_2013_group4_week37.copy;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.StringReader;
import java.net.MalformedURLException;
import java.net.URISyntaxException;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;

import org.apache.commons.codec.digest.DigestUtils;
import org.apache.http.HttpEntity;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.utils.URIBuilder;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;

public class MediaFire2 {
	public String applicationID;
	public String apiKey;
	private String sessionToken = "";

	private Map<String, String> allFolder = new HashMap<String, String>();
	private ArrayList<String> folderToDetect = new ArrayList<String>();
	
	//< folder key,   name,   download link >
	private Map<String, ArrayList<String>> files = new HashMap<String, ArrayList<String>>();
	
	public MediaFire2(String applicationID, String apikey){
		//initiate
		
		this.applicationID = applicationID;
		this.apiKey = apikey;
	}
	 	
	public void connect(String email, String password) throws IOException, AuthenticationException, URISyntaxException, ParserConfigurationException, XPathExpressionException{
		//get the sessionToken
		
		//get signature
		String original = email+password+applicationID+apiKey;
		String signature = DigestUtils.shaHex(original);
		
		URIBuilder uri = new URIBuilder("http://www.mediafire.com/api/user/get_session_token.php");
		uri.addParameter("email", email);
		uri.addParameter("password", password);
		uri.addParameter("application_id", this.applicationID);
		uri.addParameter("signature", signature);
		
		//get_session_token
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
		    System.out.print("success to get sessionToken ---- "+this.sessionToken+"\n");
		    
		    // and ensure it is fully consumed
		    EntityUtils.consume(entity1);
		} finally {
		    response1.close();
		}
	}
	
	private void phraseSubFolders (String folderKey) throws ClientProtocolException, IOException, URISyntaxException, XPathExpressionException, SAXException, ParserConfigurationException{
		//This method is called to phrase all the sub-folder under a certein folder represented by a folderKey
		
		URIBuilder uri = null;
		try {
			uri = new URIBuilder("http://www.mediafire.com/api/folder/get_content.php");
		} catch (URISyntaxException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 
		uri.addParameter("folder_key", folderKey);
		uri.addParameter("content_type","folders");
		uri.addParameter("session_token", this.sessionToken);
		
		//get all sub-folders
		CloseableHttpClient httpclient = HttpClients.createDefault();
		HttpGet httpGet = new HttpGet(uri.toString());
		CloseableHttpResponse response1 = httpclient.execute(httpGet);
		// The underlying HTTP connection is still held by the response object
		// to allow the response content to be streamed directly from the network socket.
		// In order to ensure correct deallocation of system resources
		// the user MUST either fully consume the response content  or abort request
		// execution by calling CloseableHttpResponse#close().	
		
		try {
	        HttpEntity r_entity = response1.getEntity();
	        String xmlString = EntityUtils.toString(r_entity);
	        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
	        DocumentBuilder db = factory.newDocumentBuilder();
	        InputSource inStream = new InputSource();
	        inStream.setCharacterStream(new StringReader(xmlString));
	        Document doc = db.parse(inStream);  

	        String subFolderKey = null;
	        ArrayList<String> subFolders = new ArrayList<String>();
	        
	        NodeList nl = doc.getElementsByTagName("folderkey");
	        for(int i = 0; i < nl.getLength(); i++) {
	            if (nl.item(i).getNodeType() == org.w3c.dom.Node.ELEMENT_NODE) {
	                 org.w3c.dom.Element nameElement = (org.w3c.dom.Element) nl.item(i);
	                 subFolderKey = nameElement.getFirstChild().getNodeValue().trim();
	                 subFolders.add(subFolderKey);
	                 this.folderToDetect.add(subFolderKey);
	             }
	        }
	        
	        NodeList nl1 = doc.getElementsByTagName("name");
	        ArrayList<String> names = new ArrayList<String>();
	        for(int i = 0; i < nl1.getLength(); i++) {
	            if (nl1.item(i).getNodeType() == org.w3c.dom.Node.ELEMENT_NODE) {
	                 org.w3c.dom.Element nameElement = (org.w3c.dom.Element) nl1.item(i);
	                 String name = nameElement.getFirstChild().getNodeValue().trim();
	                 names.add(name);
	             }
	        }
	        
	        for(int i=0;i<names.size();i++){
	        	this.allFolder.put(subFolders.get(i), this.allFolder.get(folderKey)+"/"+names.get(i));
	        }
	        
		} finally {
		    response1.close();
		}
	}
	
	public void getAllFolder(){
		this.allFolder.put("myfiles","MediaFire");
		this.folderToDetect.add("myfiles");
		
		while(!this.folderToDetect.isEmpty()){
			try {
				this.phraseSubFolders(this.folderToDetect.remove(0));
			} catch (ClientProtocolException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (XPathExpressionException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (URISyntaxException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (SAXException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (ParserConfigurationException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		System.out.println(this.allFolder.toString());
	}
	
	public void getAllFile() throws ClientProtocolException, IOException, ParserConfigurationException, SAXException, XPathExpressionException{
		Iterator it = this.allFolder.entrySet().iterator();
		while(it.hasNext()){
			Map.Entry entry = (Map.Entry) it.next();
			String key = (String) entry.getKey();
			this.phraseFiles(key);
		}
		System.out.println(this.files);
	}
	
	private void phraseFiles (String folderKey) throws ClientProtocolException, IOException, ParserConfigurationException, SAXException, XPathExpressionException{
		URIBuilder uri = null;
		try {
			uri = new URIBuilder("http://www.mediafire.com/api/folder/get_content.php");
		} catch (URISyntaxException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 
		uri.addParameter("folder_key", folderKey);
		uri.addParameter("content_type","files");
		uri.addParameter("session_token", this.sessionToken);
		
		//get all sub-folders
		CloseableHttpClient httpclient = HttpClients.createDefault();
		HttpGet httpGet = new HttpGet(uri.toString());
		CloseableHttpResponse response1 = httpclient.execute(httpGet);
		// The underlying HTTP connection is still held by the response object
		// to allow the response content to be streamed directly from the network socket.
		// In order to ensure correct deallocation of system resources
		// the user MUST either fully consume the response content  or abort request
		// execution by calling CloseableHttpResponse#close().	
		
		try {
	        HttpEntity r_entity = response1.getEntity();
	        String xmlString = EntityUtils.toString(r_entity);
	        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
	        DocumentBuilder db = factory.newDocumentBuilder();
	        InputSource inStream = new InputSource();
	        inStream.setCharacterStream(new StringReader(xmlString));
	        Document doc = db.parse(inStream);  

	        String fileQuickKey = null;
	        ArrayList<String> filesQuickKeys = new ArrayList<String>();
	        NodeList nl = doc.getElementsByTagName("quickkey");
	        for(int i = 0; i < nl.getLength(); i++) {
	            if (nl.item(i).getNodeType() == org.w3c.dom.Node.ELEMENT_NODE) {
	                 org.w3c.dom.Element nameElement = (org.w3c.dom.Element) nl.item(i);
	                 fileQuickKey = nameElement.getFirstChild().getNodeValue().trim();
	                 filesQuickKeys.add(fileQuickKey);
	             }
	        }
	        ArrayList<String> filesNames = new ArrayList<String>();
	        NodeList nl1 = doc.getElementsByTagName("filename");
	        String fileName = null;
	        for(int i = 0; i < nl1.getLength(); i++) {
	            if (nl1.item(i).getNodeType() == org.w3c.dom.Node.ELEMENT_NODE) {
	                 org.w3c.dom.Element nameElement = (org.w3c.dom.Element) nl1.item(i);
	                 fileName = nameElement.getFirstChild().getNodeValue().trim();
	                 filesNames.add(fileName);
	             }
	        }
	        for(int i=0;i<filesNames.size();i++){
	        	ArrayList<String> aa = new ArrayList<String>();
	        	aa.add(0, this.allFolder.get(folderKey));
	        	aa.add(1, filesNames.get(i));
	        	aa.add(2, this.phraseFileLink(filesQuickKeys.get(i)));
	        	this.files.put(filesQuickKeys.get(i), aa);
	        	
	        }
	        
		} finally {
		    response1.close();
		}
	}
	
	private String phraseFileLink (String quickKey) throws ClientProtocolException, IOException, ParserConfigurationException, SAXException, XPathExpressionException{
		String fileLink = "";
		URIBuilder uri = null;
		try {
			uri = new URIBuilder("http://www.mediafire.com/api/file/get_links.php");
		} catch (URISyntaxException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 
		uri.addParameter("quick_key", quickKey);
		uri.addParameter("session_token", this.sessionToken);

		CloseableHttpClient httpclient = HttpClients.createDefault();
		HttpGet httpGet = new HttpGet(uri.toString());
		CloseableHttpResponse response1 = httpclient.execute(httpGet);
		// The underlying HTTP connection is still held by the response object
		// to allow the response content to be streamed directly from the network socket.
		// In order to ensure correct deallocation of system resources
		// the user MUST either fully consume the response content  or abort request
		// execution by calling CloseableHttpResponse#close().
		
		
		try {
//		    System.out.println(response1.getStatusLine());
	        HttpEntity r_entity = response1.getEntity();
	        String xmlString = EntityUtils.toString(r_entity);
	        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
	        DocumentBuilder db = factory.newDocumentBuilder();
	        InputSource inStream = new InputSource();
	        inStream.setCharacterStream(new StringReader(xmlString));
	        Document doc = db.parse(inStream);  

	        String fileQuickKey = null;
	        ArrayList<String> filesQuickKeys = new ArrayList<String>();
	        NodeList nl = doc.getElementsByTagName("direct_download");
	        for(int i = 0; i < nl.getLength(); i++) {
	            if (nl.item(i).getNodeType() == org.w3c.dom.Node.ELEMENT_NODE) {
	                 org.w3c.dom.Element nameElement = (org.w3c.dom.Element) nl.item(i);
	                 fileLink = nameElement.getFirstChild().getNodeValue().trim();

	             }
	        }
		    
		    // and ensure it is fully consumed
		    EntityUtils.consume(r_entity);
		} finally {
		    response1.close();
		}
		return fileLink;
	}
	
	public void backUpFiles() throws MalformedURLException{
		System.out.println("Start to back up");
		Iterator it = this.files.entrySet().iterator();
		String folder = null;
		String name = null;
		String link = null;
		
		while(it.hasNext()){
			Map.Entry entry = (Map.Entry) it.next();
			ArrayList<String> haha = (ArrayList<String>)entry.getValue();
			folder = haha.get(0);
			name = haha.get(1);
			link = haha.get(2);
			
			int bytesum = 0;
			int byteread = 0;
			URL url = new URL(link);
			try {
				URLConnection conn = url.openConnection();
				InputStream inStream = conn.getInputStream();
	            File myFilePath = new File("D:/BackUp/"+folder+"/");    
	            if  (!myFilePath.exists())  {    
	            	if(myFilePath.mkdirs()){
	            		System.out.println("hhahaha");
	            	}
	            } 
				FileOutputStream fs = new FileOutputStream("D:/BackUp/"+folder+"/"+name);
				byte[] buffer = new byte[1204];
				int length;
				while ((byteread = inStream.read(buffer)) != -1) {
					bytesum += byteread;
					System.out.println(bytesum);
					fs.write(buffer, 0, byteread);
				}
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}

}


