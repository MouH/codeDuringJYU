package ties456_2013_group4_week37.copy;

import java.io.IOException;
import java.net.URISyntaxException;
import java.util.List;

import javax.xml.parsers.ParserConfigurationException;
import javax.xml.xpath.XPathExpressionException;

import org.xml.sax.SAXException;

public class Test {
	public static void main(String [ ] args) throws XPathExpressionException, IOException, AuthenticationException, URISyntaxException, ParserConfigurationException, SAXException
	{
		String applicationID = "38416";
		String apiKey = "m6l7uzmn3n6fmqdl7n60kq900nx8se8odad3b8ox";
		String email = "karkkainen357@hotmail.com";
		String password = "170482DongS";
		
		MediaFire2 mediaFire = new MediaFire2(applicationID,apiKey);
		mediaFire.connect(email, password);
		mediaFire.getAllFolder();
		mediaFire.getAllFile();
		mediaFire.backUpFiles();
	
	}

}
