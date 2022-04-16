#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from os import system, path, listdir
import argparse
import requests

def main():

	parser = argparse.ArgumentParser(description="""\
	Replace Name, username and email for all projects on Github

	Replace in commit: $ python3 transgited.py --user username --name \"Your Name\" --oldemail old@email.com --email new@email.com
	Replace in files: $ python3 transgited.py --replace --user username --name \"Your Name\" --oldname \"Old Name\" --email new@email.com
	Help: $ python3 transgited.py --help""", formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('-u', '--user', type=str, help='Your username', required=True)
	parser.add_argument('-n', '--name', type=str, help='Your name', required=True)
	parser.add_argument('-e', '--email', type=str, help='Your new E-mail', required=True)
	parser.add_argument('-on', '--oldname', type=str, help='Your old name')
	parser.add_argument('-oe', '--oldemail', type=str, help='Your old E-mail')
	parser.add_argument('-a', '--all', type=bool, help='Replace for source and fork projects', action=argparse.BooleanOptionalAction)
	parser.add_argument('-r', '--replace', type=bool, help='Replace name in all projects', action=argparse.BooleanOptionalAction)
	parser.add_argument('-o', '--onlyfork', type=bool, help='Replace for source and fork projects', action=argparse.BooleanOptionalAction)
	args = parser.parse_args()

	password = input("Type your GitHub Access Token: https://github.com/settings/tokens/\n")

	if args.replace == True:
		if args.oldname == None:
			print("Missing old name")
			return
		if len(args.oldname.split()) != len(args.name.split()):
			print("Names must be same length")
			return
		x=0
		repos = [a for a in listdir() if path.isdir(a)]
		for name in args.name.split():
			print(f"changing {name}...")
			system(f"sudo find . \\( -type d -name .git -prune \\) -o -type f -print0 | xargs -0 sed -i 's/{args.oldname.split()[x]}/{name}/I'")
			x+=1
		for repo in repos:
			system(f"cd {repo}/ ; sudo rm bash_script.sh ; sudo git add . ; sudo git commit -m \"Replace old name\" ;\
					 sudo git push https://{args.user}:{password}@github.com/{args.user}/{repo}.git -u master")
		return
		
	if args.oldemail == None:
		print("missing oldemail")
		return

	url = f"https://api.github.com/users/{args.user}/repos?per_page=1000"

	resp = requests.get(url=url)
	json_data = resp.json()
	repos=[]
	for repo in json_data:
		if args.all == True:
			repos.append(repo["name"])
		elif args.onlyfork == True:
			if repo["fork"] == True:
				repos.append(repo["name"])
		else:
			if repo["fork"] == False:
				repos.append(repo["name"])
	
	print("Your repos: "+ ", ".join(repos))
	for repo in repos:
		if path.exists(repo):
			print(f"Repo {repo} already exists")
		else:
			system(f"git clone https://github.com/{args.user}/{repo}")

		system(f"cp bash_script.sh {repo}")
		system(f"cd {repo}/ ; chmod +x bash_script.sh ;\
				 sudo ./bash_script.sh {args.oldemail} \"{args.name}\" {args.email} ;\
				 git push https://{args.user}:{password}@github.com/{args.user}/{repo}.git --force --all")

if __name__ == '__main__':
	main()