import requests


def GetSolvedProblems(user):
    
    url='https://codeforces.com/api/user.status?handle='+ user
    r=requests.get(url)

    content=r.json()
    if(content['status']!='OK'): return (False,1)

    content=content['result']
    problems=set()

    for problem in content:
        problems.add(problem['contestId'])


    return (True,problems)