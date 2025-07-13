# Function	Use it when you want to...
# get()	Ask for data (read only)
# post()	Send new data (create)
# put()	Replace something completely
# patch()	Update a part of something
# delete()	Remove something

import requests

# response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
# print(response.status_code)  #If return 200 fine 404 means error
# print(response.json())  #GIve data from APIs in dic
# # print(response.text)  #Give Code in text form

# -------------------------------------------------------------------------------

# GET
# response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
# if response.status_code == 200:
#     data = response.json()
#     print("Title of the task is: ", data['title'])
# else:
#     print("Something went wrong!")

# -------------------------------------------------------------------------------

# requests.post(url, data={"name": "Alice"})    #It send data to add into the list
# new_task = {
#     "userId": 1,
#     "title": "Learn POST request",
#     "completed": False
# }

# response = requests.post("https://jsonplaceholder.typicode.com/todos", json=new_task)

# print("Status code:", response.status_code)
# print("Response JSON:", response.json())

# --------------------------------------------------------------------------------

# To jab tu delete ke button pe click karta jese hum insta ki koi post delete Karen to delete request jaati
# requests.delete(url)  # It delete some stuff It is for your on web
# response = requests.delete("https://jsonplaceholder.typicode.com/todos/1")
# print("Delete status : ",response.status_code)

#=================================================================================

# requests.put(url, data={"title": "New Title"})     #It replace all list
# new = {
#     "userId": 1,
#     "title": "Learn POST request",
# }
# response = requests.put("https://jsonplaceholder.typicode.com/todos/1", json=new)

# print(response.status_code)
# print(response.json())

# requests.patch(url, data={"title": "Just changing this"})   #It replace a part of list
dataa = {
    "title": "Partially Updated Title"
}
response = requests.patch("https://jsonplaceholder.typicode.com/todos/1",json=dataa)
print(response.status_code)
print(response.json())