#!/usr/bin/python3
"""Module that returns information about TODO list progress
"""


import requests
from sys import argv

if __name__ == "__main__":
	arg = int(argv[1])

	url = 'https://jsonplaceholder.typicode.com/'
	users = requests.get(url + 'users')
	todos = requests.get(url + 'todos')

	for item in users.json():
		if arg == item.get("id"):
			total = 0
			count = 0
			name = item.get("name")
			task = []
			for i in todos.json():
				if arg == i.get("userId"):
					total += 1
					if i.get("completed"):
						task.append(i.get("title"))
						count += 1
			print("""Employee {} is done with tasks({}/{}):\
			""".format(name, count, total))
			for val in task:
				print("\t {}".format(val))
