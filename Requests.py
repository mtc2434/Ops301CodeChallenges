#!/usr/bin/env python3
# Script:  Requests.py                     
# Author:  Marcelo Clark                      
# Date of latest revision:   6/14/2023   
# Purpose:  performing HTTP GET requests using the requests Python library. This library is very useful for a security professional to evaluate how a web server responds to outside requests.





import requests

# User enters URL
url = input("Enter the URL: ")

# User picks which Http method they want
http_method = input("Select HTTP method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")

# Request  Details
print("Request:")
print("URL:", url)
print("HTTP Method:", http_method)

# Defines different requests
http_methods = {
    "GET": requests.get,
    "POST": requests.post,
    "PUT": requests.put,
    "DELETE": requests.delete,
    "HEAD": requests.head,
    "PATCH": requests.patch,
    "OPTIONS": requests.options
}

# Performs request
if http_method in http_methods:
    response = http_methods[http_method](url)
else:
    print("Invalid HTTP method.")
    exit()

# Print response headers
print("\nResponse Header Information:")
for header, value in response.headers.items():
    print(f"{header}: {value}")

#traslate status code
status_code = response.status_code
status_text = requests.status_codes._codes[status_code][0]
print("Status Code:", status_code)
print("Status Text:", status_text)
