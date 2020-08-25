## Virtual Contests for Codeforces

#### Link: https://guarded-chamber-89041.herokuapp.com/


- How to Use

    * go to above mentioned link
    * enter your codeforces userhandle
    * enter the division which you want
    * hit GET VIRTUAL CONTEST to list all available contest


- What it does:

    * Filters out the contests available for virtual participation in codeforces 
    * i.e. the contests in which the user has not given any submission 
    * So that, all problems will be new to user.

- How it works:

    * First it fetches the contests in which user has given atleast 1 submission.
    * Then it fetches total contests in codeforces contest page
    * Then by Hashing Technique it stores contests in which user has not given any submission.

- What is used:

    * Python/Django framework
    * Codeforces API methods
        - contest.list
        - user.status



