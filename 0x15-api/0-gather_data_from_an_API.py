#!/usr/bin/python3
"""Module that returns information about TODO list progress
"""


import requests
from sys import argv

if __name__ == "__main__":
  arg = int(argv[1])
# print(arg)
  url = 'https://jsonplaceholder.typicode.com/'
  users = requests.get(url + 'users')
  todos = requests.get(url + 'todos')
# print(users.json())

  for item in users.json():
# print(item)
    if arg == item.get("id"):
#   print(item)
      total = 0
      count = 0
      name = item.get("name")
      task = []
      for i in todos.json():
#     print(i)
        if arg == i.get("userId"):
          total += 1
          if i.get("completed"):
            task.append(i.get("title"))
            count += 1
      print("Employee {} is done with tasks({}/{}):".format(name, count, total))
      for val in task:
        print("\t {}".format(val))
