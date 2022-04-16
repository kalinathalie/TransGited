 # TransGited 🏳️‍⚧️

> This tool can replace every commit author+email and every name in all files for all projects of a Github user.

```
usage: transgited.py [-h] -u USER -n NAME -e EMAIL [-on OLDNAME] [-oe OLDEMAIL] [-a | --all | --no-all] [-r | --replace | --no-replace]
                     [-o | --onlyfork | --no-onlyfork]
    
    Replace in commit : $ python3 transgited.py --user username --name "Your Name" --oldemail old@email.com --email new@email.com
    Replace in files  : $ python3 transgited.py --replace --user username --name "Your Name" --oldname "Old Name" --email new@email.com
    Help              : $ python3 transgited.py --help

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER  Your username
  -n NAME, --name NAME  Your name
  -e EMAIL, --email EMAIL
                        Your new E-mail
  -on OLDNAME, --oldname OLDNAME
                        Your old name
  -oe OLDEMAIL, --oldemail OLDEMAIL
                        Your old E-mail
  -a, --all, --no-all   Replace for source and fork projects
  -r, --replace, --no-replace
                        Replace name in all projects
  -o, --onlyfork, --no-onlyfork
                        Replace for source and fork projects

```

By: Kali Nathalie
