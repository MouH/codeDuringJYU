package ties456_2013_group4_week37;

import java.io.IOException;
import java.net.URISyntaxException;

import javax.xml.parsers.ParserConfigurationException;
import javax.xml.xpath.XPathExpressionException;

public class Test {
	public static void main(String [ ] args) throws XPathExpressionException, IOException, AuthenticationException, URISyntaxException, ParserConfigurationException
	{
		String applicationID = "11094";
		String apiKey = "4wigjg799kzoc6wettp8i7c947qmvv25u68c6pux";
		String email = "muhaocd@gmail.com";
		String password = "qwerty";
		
		MediaFire mediaFire = new MediaFire(applicationID,apiKey);
		mediaFire.connect(email, password);
		mediaFire.getInfo();
		System.out.print(mediaFire.userInfo);
	}

}
