import shortuuid
import http.client
import urllib.parse

def shorten_url(original_url):
    # Generate a unique short ID
    short_id = shortuuid.uuid()[:6]
    
    # Create a connection to the URL shortening service (in this case, bit.ly)
    conn = http.client.HTTPConnection("api.bitly.com")
    
    # Set the headers and data for the request
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    data = urllib.parse.urlencode({'longUrl': original_url, 'domain': 'bit.ly', 'login': 'your_email', 'apiKey': 'your_api_key'})
    
    # Send the request
    conn.request("POST", "/v3/shorten", data, headers)
    
    # Get the response
    response = conn.getresponse()
    
    # Check if the request was successful
    if response.status == 200:
        # Parse the JSON response
        response_data = response.read().decode()
        shortened_url = urllib.parse.urlparse(response_data).path[1:]
        
        # Return the shortened URL
        return "http://bit.ly/" + shortened_url
    else:
        return "Error shortening URL"

# Test the function
original_url = "http://www.example.com"
shortened_url = shorten_url(original_url)
print("Original URL:", original_url)
print("Shortened URL:", shortened_url)
