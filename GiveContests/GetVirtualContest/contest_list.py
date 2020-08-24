import requests

def GetContestIDs(div):
    
    url='https://codeforces.com/api/contest.list?gym=false'
    r=requests.get(url)

    content=r.json()
    if(content['status']!='OK'): return (False,3)
    
    content=content['result']
    Contest={}

    for contest in content:
        if(contest['phase']=='FINISHED' and all(_ in contest['name'] for _ in ['Codeforces','Div. '+str(div)])):
            Contest[contest['id']]=contest['name']

    # print(Contest)
    # print(div)
    
    return (True,Contest)







