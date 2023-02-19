#!/usr/bin/python3
"""Module that returns information about TODO list progress
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
	arg = int(argv[1])
	url = 'https://jsonplaceholder.typicode.com/'
	user = requests.get(url + 'users/{}'.format(arg)).json()
	todos = requests.get(url + 'todos', params={'userId': arg}).json()
	name = user.get("username")

	with open("{}.csv".format(arg), 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
		[writer.writerow(
			[arg, name, i.get("completed"), i.get("title")]
		) for i in todos]

