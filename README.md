# Handyman Tools
A web app project for Georgia Tech's Advanced Databases course.  Working in a team of four people, the purpose of the project was to take a series of use-cases to design the database schema, queries, documentation, and finally implement a web-app for handling the inventory of a hardware store.

## Technology Stack
- Bottle framework
- Python
- SQL
- Bootstrap
- jQuery

## Getting started

Recommend using virtualenv:
```
$ git checkout -b <your-private-branch-name>
$ pyvenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python app.py
```

## Contributing

Make sure you are on your development branch and rebase all changes from master.
```
$ git checkout <your-private-branch-name>
$ git rebase master
```

Push your branch to github
`$ git push origin <your-branch-name>`

Initiate a pull request on github. [Instructions](https://help.github.com/articles/using-pull-requests/) can be found on github

After the pull request is accepted, remove your feature/development branch.
`$ git push <remotename> :<branchname>`

## CI

Staging site is located at http://handyman-tools.cfapps.io

All changes to this github repo are push to the staging site
