import requests
from . import contest_list
from . import contests_with_attempted_problem


def getContestForVirtualParticipation(user,totalContest,div):

    contest=contests_with_attempted_problem.GetSolvedProblems(user)

    forVirtual=[]

    for id in totalContest:
        if(id not in contest):
            forVirtual.append((id,totalContest[id]))

    return forVirtual



