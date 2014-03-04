package fi.jyu.ties456.group4.week40.cache;

import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeUnit;

import fi.jyu.ties456.group4.week40.gdp.NoSuchCountryException_Exception;
import fi.jyu.ties456.group4.week40.util.GDPWrapper;

import com.google.common.cache.CacheBuilder;
import com.google.common.cache.CacheLoader;
import com.google.common.cache.LoadingCache;

public class GDPCache {
	
	private static LoadingCache<String, Double> gdpCache;

	static {
		gdpCache = CacheBuilder.newBuilder()
			       .maximumSize(10)
			       .expireAfterWrite(2, TimeUnit.MINUTES)
			       .build(
			           new CacheLoader<String, Double>() {
			             public Double load(String countryCode) throws NoSuchCountryException_Exception{
				         		GDPWrapper gdp = new GDPWrapper();
				         		return gdp.getAGDP(countryCode);
			             }
			           });	
	}
	public static Double getGDP(String countryCode) throws NoSuchCountryException_Exception, ExecutionException{
		return gdpCache.get(countryCode);
	
	}

}
