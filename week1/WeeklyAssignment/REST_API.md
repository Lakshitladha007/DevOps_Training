REST API's

- REST stands for "Representational State Transfer". This method is used to send an HTTP or HTTPs request to a RESTful 
web service.

- The Invoke-RestMethod cmdlet sends HTTP and HTTPS requests to Representational State Transfer (REST) web services.

- It is commonly used for interacting with web APIs, sending data to a server, and retrieving data from web services
in various formats such as JSON, XML, or plain text.

- It can send requests like GET, POST, PUT, DELETE, etc., to access or modify web resources.

- It can handle responses in various formats (JSON, XML, etc.) and can convert the response into PowerShell objects 
for easy manipulation.

SYNTAX:

Invoke-RestMethod [-Uri] <String> [-Method <String>] [-Headers <IDictionary>] [-Body <Object>] [-ContentType <String>] 
[-Credential <PSCredential>] [-InFile <String>] [-OutFile <String>] [-Proxy <String>] [-ProxyCredential <PSCredential>] 
[-ProxyUseDefaultCredentials] [-TimeoutSec <Int32>] [-UseBasicP] [-UserAgent <String>] 
[-Authentication <AuthenticationMethod>] 
[-AllowUnencryptedAuthentication] [<CommonParameters>]

KEY PARAMETERS:

1. URI:
    - URI stands for Uniform Resource Identifier.
    - The URI (Uniform Resource Identifier) is the endpoint you want to interact with. This is a required parameter.

2. Method:
    - The method specifies the HTTP method to use for the request. **The default is `GET`**, but you can specify
      methods like `POST`, `PUT`, `DELETE`, etc.
    - Example: `Method "POST"` or `Method "GET"`

3. Body:
    - The content to send with the request. This is typically used for POST or PUT requests, where you need to send 
    data to the server.

4. ContentType:
    - Specifies the content type of the request (e.g., `application/json`, `application/x-www-form-urlencoded`, etc.)

5. Credential:
    - A PSCredential object to specify the credentials (username and password) for basic authentication when required.
    
RETURN VALUE:

`Invoke-RestMethod` typically returns the response from the web service as a PowerShell object. If the response is in 
JSON format, PowerShell automatically converts it into an object.

Different HTTP methods used in REST APi's:

1. GET Method:
The GET method is used to retrieve resources from a server. It is said to be a safe method as it does not change the
state of the resource in any way.

2. POST Method:
POST method is used to create a new resource into the collection of resources on a server.

3. PUT Method:
PUT is used to update the existing resource on the server and it updates the full resource.

4. Delete Method:
DELETE Method is used to delete the resources from a server. It deletes resource identified by the Request-URI.
