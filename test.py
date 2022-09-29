import requests

BASE = "http://127.0.0.1:8000/"

# data =[{"likes":10,"name":"janm","views": 1500},
# 		{"likes":15,"name":"tim","views": 1100},
# 		{"likes":222,"name":"edw","views": 2500}]

# for i in range(len(data)):
# 	response = requests.put(BASE +"video/"+str(i),data[i])
# 	print(response.json())


# input()
# response = requests.get(BASE +"video/6")
# print(response.json())

response = requests.get(BASE +"video/2")
print(response.json())