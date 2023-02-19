#!/usr/bin/python3
"""Module that returns information about TODO list progress
"""


import requests
from sys import argv

if __name__ == "__main__":
	arg = int(argv[1])

	file = "USER_ID.csv"
	url = 'https://jsonplaceholder.typicode.com/'
	users = requests.get(url + 'users')
	todos = requests.get(url + 'todos')

	for item in users.json():
		if arg == item.get("id"):
			name = item.get("name")
			for i in todos.json():
				if arg == i.get("userId"):
					with open(file, mode='a', encoding="utf-8") as f:
						f.write('''"{}","{}","{}","{}"\n'''\
					   		.format(arg,
						   		name,
						   		i.get("completed"),
						   		i.get("title")))
