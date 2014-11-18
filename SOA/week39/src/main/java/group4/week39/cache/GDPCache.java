package main.java.group4.week39.cache;

import java.util.concurrent.ExecutionException;

import main.java.group4.week39.gdp.NoSuchCountryException_Exception;
import main.java.group4.week39.util.GDPWrapper;

import com.google.common.cache.CacheBuilder;
import com.google.common.cache.CacheLoader;
import com.google.common.cache.LoadingCache;

public class GDPCache {
	
	private static LoadingCache<String, Double> gdpCache;

	static {
		gdpCache = CacheBuilder.newBuilder()
			       .maximumSize(1000)
//			       .expireAfterWrite(10, TimeUnit.MINUTES)
			       .build(
			           new CacheLoader<String, Double>() {
			             public Double load(String countryCode) throws NoSuchCountryException_Exception{
				         		GDPWrapper gdp = new GDPWrapper();
				         		return gdp.getGDP(countryCode);
			             }
			           });	
	}
	public static Double getGDP(String countryCode) throws NoSuchCountryException_Exception{
		try {
			return gdpCache.get(countryCode);
		} catch (ExecutionException e) {
			Throwable[] ex = e.getSuppressed();
			if ( ex[0] instanceof NoSuchCountryException_Exception){
				throw (NoSuchCountryException_Exception)ex[0];
			}
			throw new RuntimeException(e);
		}		
	}

}
