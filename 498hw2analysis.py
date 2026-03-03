import time
import requests

urls = [
    ('http://35.188.222.116:8080/register', 'POST'),
    ('http://35.195.182.100:8080/register', 'POST'),
    ('http://35.188.222.116:8080/list', 'GET'),
    ('http://35.195.182.100:8080/list', 'GET')
]

for url, method in urls:
    total_time = 0
    
    for i in range(10):
        start = time.time()
        
        if method == 'POST':
            payload = {"username": f"LatencyUser_{int(time.time() * 1000)}_{i}"}
            requests.post(url, json=payload)
        else:
            requests.get(url)
            
        total_time += (time.time() - start) * 1000 
        
    print(url)
    print(total_time / 10)
    
    

not_found_count = 0

for i in range(100):
    unique_username = f"ConsistencyUser_{int(time.time() * 1000)}_{i}"
    
    requests.post("http://35.188.222.116:8080/register", json={"username": unique_username})
    
    response = requests.get("http://35.195.182.100:8080/list")
    data = response.json()
    
    if unique_username not in data.get("users", []):
        not_found_count += 1

print(f"not found #:{not_found_count}")