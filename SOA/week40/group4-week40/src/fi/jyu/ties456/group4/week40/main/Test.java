package fi.jyu.ties456.group4.week40.main;

import java.net.URISyntaxException;

import fi.jyu.ties456.group4.week40.util.GDPUtil;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		GDPUtil gdpUtil = new GDPUtil();
		gdpUtil.setLatlng("40.714224", "-73.961452");
		String countryCode = null;
		try {
			countryCode = gdpUtil.getCountryCode();
		} catch (URISyntaxException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		System.out.println(countryCode);
	}

}
