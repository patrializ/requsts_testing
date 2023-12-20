import requests

# Example GET request
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("GET Request:")
print("Status Code:", response.status_code)
print("Response Content:")
print(response.json())
print()

# Example of a POST request with data transfer
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print("POST Request:")
print("Status Code:", response.status_code)
print("Response Content:")
print(response.json())
print()

# Example PUT request to update a resource
update_data = {
    'title': 'foo updated',
    'body': 'bar updated'
}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=update_data)
print("PUT Request:")
print("Status Code:", response.status_code)
print("Response Content:")
print(response.json())
print()

# Example DELETE request to delete a resource
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print("DELETE Request:")
print("Status Code:", response.status_code)
print("Response Content:")
print(response.text)
