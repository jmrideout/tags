# Tags - A silly little Python webapp for CodePlatoon git classes ***Edited for ANDREW branch

The tags webapp lists tags and stores more tags.

It displays an image based on info in a config file.

It knows about development, uat, and production environments.

It uses a SQLite database.

It uses a primitive (and rather obsolete) ORM called [Flask-Orator](https://github.com/sdispater/flask-orator).

This app is so barebones and unfinished that it begs for changes.  Using git, you will collaborate with your team to make it better.

## Environment assumptions *edited again for ANDREW branch

- You have a Python3 installed that is recent enough to have the "-m" option for configuring virtual environments.

- You have a [GitHub](https://github.com) account.

## Set up and run the webapp

Fork the Tags repo from https://github.com/walquis/tags.

Run these commands in a Terminal session:
```bash
$ cd # Start from your home directory
$ mkdir src; cd src  # Or cd to wherever you keep code projects
$ git clone https://github.com/<yourlogin>/tags # Clone your fork
# Or use ssh protocol...  $ git clone git@github.com:<yourlogin>/tags
$ cd tags
$ mkdir ../shared  # In case you want to share config across releases
$ cp config.yml.sample ../shared/config.yml
$ python3 -m venv venv  # Make a virtual env in the "venv" directory
$ source venv/bin/activate  # Enter your virtual env
$ pip install -r requirements.txt  # Populate current virtual env with packages
$ python bin/load_schema.py   # Init your DB structure. Assumes FLASK_ENV=development
$ python bin/seed.py   # Add data to your DB.  Assumes FLASK_ENV=development
$ bin/run-flask-webserver.sh  # Assumes FLASK_ENV=development
```
Now visit http://localhost:5555 in your browser.

## A Simulated Project for Collaborating

*Goal*: Your team will exercise your new-found knowledge of git by making changes to this code base.  Below are some suggested tasks.  By divvying them up among your team and implementing them, you will experience the typical challenges associated with working in parallel on a code base.  Your team is free to come up with your own tasks, but keep it simple!  The idea is not to learn new code, but to practice using git for team collaboration.

The ```master``` branch has a working version of the app, runnable as described above.

*Objective*: Keep the app working as you deliver changes to ```master```.

For each task below, a possible solution (aka "reference implementation") lives on a corresponding branch.  Feel free to take a look at the solution branch for ideas/insight into accomplishing the task.  For instance, you can peek at the "Add a config parameter ..." solution by git-diff'ing its ```more_config``` solution branch against master:
```
$ git checkout more_config
$ git diff master
```
Hints for diff'ing the sample solutions:
1. Because (a) all the sample solutions branch from the same point on master, and (b) master will be moving as changes come in, you may want to create a branch to use as a label purely for diff'ing purposes:
```
$ git checkout master
$ git branch master-mark
$ git checkout view_template
$ git diff master-mark
```
2. For some branch comparisons, you may desire to exclude one or more files from the ```git diff``` output. For instance, there's no point in viewing the entire jquery file when looking at ```better_delete_route```...)
```
$ git checkout better_delete_route
$ git diff master -- . ':(exclude)*jquery*.js'
```

Both *Round One* and *Round Two* solutions are branched from the initial ```master``` branch.  However, you may want to tackle the more-complex *Round Two* tasks after you've completed *Round One*.

### Getting Started on the Project

1. *Someone on your team* - Fork this repo and grant read/write access to the rest of the team, who will each clone to their local machine.  NOTE: Just to keep things simple and focused on git (as opposed to github), we will not be using any Github workflow operations apart from the one fork operation.
1. *Whole Team* - Take a look at the Round One tasks below, and decide who will tackle each task.  It will be useful to ```git diff``` the branches with sample solutions, as demonstrated above.
1. *Each Member* - Begin implementing your assigned task.  You may want to work on a non-master branch.
1. *Each Member* - As you finish a task, merge it to ```master``` and ```git push```.  (NOTE: Before merging to master, it's a good idea to Do a ```git pull``` of ```master``` first, just in case changes have been delivered since you last branched from ```master```. In that case, you will need to merge before delivering!)  Oh, and after delivering to ```master```, and before pushing to the shared team repo, don't forget to make sure the website still works.

### Round One Tasks
- ```view_template``` - Move the HTML into a Jinja2 template
- ```stylesheet``` - Move CSS into a stylesheet
- ```tag_input_first``` - Move the tag input above the tag list
- ```more_config``` - Add a config parameter to set title to 'Hello Sol!'
- ```delete_route``` - Add a delete route, to where clicking on a tag deletes it
- ```about_page_with_nav``` - Add an "about" page, with navigation menu

### Round Two Tasks
- ```layout``` - Add a Jinja layout
- ```better_delete_route``` - Use a DELETE method (and some Javascript/jQuery) to delete tags
- ```peewee``` - Switch the ORM from Flask-Orator to Peewee (if you really want to bite off a big chunk!)
