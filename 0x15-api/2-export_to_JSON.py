#!/usr/bin/python3
"""Module that returns information about TODO list progress
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
	arg = int(argv[1])
	url = 'https://jsonplaceholder.typicode.com/'
	user = requests.get(url + 'users/{}'.format(arg)).json()
	todos = requests.get(url + 'todos', params={'userId': arg}).json()
	name = user.get("username")

	with open("{}.json".format(arg), 'w') as jsonfile:
		json.dump({arg: [{
			"task": i.get("title"),
			"completed": i.get("completed"),
			"username": name
			} for i in todos]}, jsonfile)
