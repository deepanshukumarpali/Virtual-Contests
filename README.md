##Virtual Contests for Codeforces


- What it does:

    Filters out the contests available for virtual participation in codeforces 
    i.e. the contests in which the user has not given any submission 
    so that, all problems will be new to user.

- How it works:

    First it fetches the contests in which user has given atleast 1 submission.
    Then it fetches total contests in codeforces contest page
    Then by Hashing Technique it stores contests in which user has not given any submission.

- What is used:

    Python/Django framework
    Codeforces API methods
        - contest.list
        - user.status



