import requests


def GetSolvedProblems(user):
    
    url='https://codeforces.com/api/user.status?handle='+ user
    r=requests.get(url)

    content=r.json()
    if(content['status']!='OK'): return False

    content=content['result']
    problems=set()

    for problem in content:
        problems.add(problem['contestId'])

    return problems