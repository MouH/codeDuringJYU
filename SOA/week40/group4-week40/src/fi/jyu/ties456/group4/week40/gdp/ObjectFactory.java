
package fi.jyu.ties456.group4.week40.gdp;

import javax.xml.bind.JAXBElement;
import javax.xml.bind.annotation.XmlElementDecl;
import javax.xml.bind.annotation.XmlRegistry;
import javax.xml.namespace.QName;


/**
 * This object contains factory methods for each 
 * Java content interface and Java element interface 
 * generated in the fi.jyu.ties456.group4.week39.gdp package. 
 * <p>An ObjectFactory allows you to programatically 
 * construct new instances of the Java representation 
 * for XML content. The Java representation of XML 
 * content can consist of schema derived interfaces 
 * and classes representing the binding of schema 
 * type definitions, element declarations and model 
 * groups.  Factory methods for each of these are 
 * provided in this class.
 * 
 */
@XmlRegistry
public class ObjectFactory {

    private final static QName _GetGDP_QNAME = new QName("http://ws.demo1.ties532.jyu.fi/", "getGDP");
    private final static QName _NoSuchCountryException_QNAME = new QName("http://ws.demo1.ties532.jyu.fi/", "NoSuchCountryException");
    private final static QName _GetGDPResponse_QNAME = new QName("http://ws.demo1.ties532.jyu.fi/", "getGDPResponse");

    /**
     * Create a new ObjectFactory that can be used to create new instances of schema derived classes for package: fi.jyu.ties456.group4.week39.gdp
     * 
     */
    public ObjectFactory() {
    }

    /**
     * Create an instance of {@link NoSuchCountryException }
     * 
     */
    public NoSuchCountryException createNoSuchCountryException() {
        return new NoSuchCountryException();
    }

    /**
     * Create an instance of {@link GetGDP }
     * 
     */
    public GetGDP createGetGDP() {
        return new GetGDP();
    }

    /**
     * Create an instance of {@link GetGDPResponse }
     * 
     */
    public GetGDPResponse createGetGDPResponse() {
        return new GetGDPResponse();
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link GetGDP }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "http://ws.demo1.ties532.jyu.fi/", name = "getGDP")
    public JAXBElement<GetGDP> createGetGDP(GetGDP value) {
        return new JAXBElement<GetGDP>(_GetGDP_QNAME, GetGDP.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link NoSuchCountryException }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "http://ws.demo1.ties532.jyu.fi/", name = "NoSuchCountryException")
    public JAXBElement<NoSuchCountryException> createNoSuchCountryException(NoSuchCountryException value) {
        return new JAXBElement<NoSuchCountryException>(_NoSuchCountryException_QNAME, NoSuchCountryException.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link GetGDPResponse }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "http://ws.demo1.ties532.jyu.fi/", name = "getGDPResponse")
    public JAXBElement<GetGDPResponse> createGetGDPResponse(GetGDPResponse value) {
        return new JAXBElement<GetGDPResponse>(_GetGDPResponse_QNAME, GetGDPResponse.class, null, value);
    }

}
