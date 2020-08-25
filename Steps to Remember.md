## Things New To Me

- Clonning new project to git from terminal

    * create new repository from github.com

    * cd to project directory

    * intitialize it as Git repository
        $ git init

    * add the files in your new local repository
        $ git add --all

    * Commit the files that are in your local repository
        $ git commit -m 'First commit'

    * copy remote URL from github repository

    * add this URL to your local repository
        $ git remote add origin [remote_repository_URL]
        $ git remote -v

    * push the changes in your local repository to github
        $ git push origin master

- Working on Heroku

    * make account on heroku

    * make requirements.txt which contains all your dependencies in your virtualenv
        $ pip freeze > requirements.txt

    * remember to change settings.py ALLOWED_HOSTS=['*']

    * make Procfile (without any extension) and write
        web: gunicorn [appname_in_Django_project].wsgi --log-file -

    * log into heroku in terminal, enter details once directed to browser
        $ heroku login

    * cd to project directory and create heroku app
        $ heroku create
    
    * add the given heroku remote URL
        $ heroku git:remote -a [remote_URL]

    * disable static files in django project
        $ heroku config:set DISABLE_COLLECTSTATIC=1
    
    * push into heroku repository
        $ push heroku master

- Updating WebApp

    * update changes to github repository
        $ git status
        $ git add -A
        $ git commit -m "first commit"
        $ git push origin master

    * update changes to heroku repository
        $ git push origin master 
