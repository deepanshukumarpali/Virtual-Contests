import requests
from . import contest_list
from . import contests_with_attempted_problem


def getContestForVirtualParticipation(user,totalContest,div):


    contest=contests_with_attempted_problem.GetSolvedProblems(user)

    forVirtual=[]
    link='https://codeforces.com/contest/'

    if(contest[0]==False):
        return contest

    contest=contest[1]

    for id in totalContest:
        if(id not in contest):
            forVirtual.append((id,totalContest[id],link+str(id)))

    if(len(forVirtual)==0):
        return (False,2)

    return (True,forVirtual)



