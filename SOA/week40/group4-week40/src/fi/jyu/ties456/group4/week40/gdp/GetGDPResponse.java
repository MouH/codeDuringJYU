
package fi.jyu.ties456.group4.week40.gdp;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlType;


/**
 * <p>Java class for getGDPResponse complex type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * 
 * <pre>
 * &lt;complexType name="getGDPResponse">
 *   &lt;complexContent>
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       &lt;sequence>
 *         &lt;element name="GDP" type="{http://www.w3.org/2001/XMLSchema}double" minOccurs="0"/>
 *       &lt;/sequence>
 *     &lt;/restriction>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "getGDPResponse", propOrder = {
    "gdp"
})
public class GetGDPResponse {

    @XmlElement(name = "GDP")
    protected Double gdp;

    /**
     * Gets the value of the gdp property.
     * 
     * @return
     *     possible object is
     *     {@link Double }
     *     
     */
    public Double getGDP() {
        return gdp;
    }

    /**
     * Sets the value of the gdp property.
     * 
     * @param value
     *     allowed object is
     *     {@link Double }
     *     
     */
    public void setGDP(Double value) {
        this.gdp = value;
    }

}
