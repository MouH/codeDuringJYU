Local GDP Service

What is a Local GDP Service?
 - Local GDP service is s service you can get GDP data form a country which represented by geographic 
   coordinates data(like, like latitude 37.423021 and longitude -122.083739).
 - The Local GDP Service provides a direct way to access GDP data via an HTTP request.
 - The service is implemented in RESTFul standard.
 
Usage Limits
 - not implement
 
Http requests
- A Local GDP request must be of the following form:
  http://localhost:8080/group4-week39/rest/localgdpservice?parameters
  
- Required parameters (no optional parameters)
  lat - latitude of the request address
  lon - longitude of the request address
  
Responses
- the response is always in JSON Format.
- the JSON returned by this request is shown below.
- if successfully return the GDP data, the JSON should return
{
	"GDP" : 1234.9457，
	"error" : " "
}
- else
{
	"GDP" : ,
	"error" : "not enough parameters" | "not a country"
}
  