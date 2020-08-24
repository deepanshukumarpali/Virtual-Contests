from . import contest_list
from . import contest_list_CSV
from . import virtual_contest
from . import virtual_contest_list_CSV




def TryTheseContests(user,div):

    # Fetchting all codeforces Contests
    #
    AllContests=contest_list.GetContestIDs(div)

    if(AllContests[0]==False):
        return AllContests

    # Writing all contest to ContestList.csv
    #
    # contest_list_CSV.WriteToCSV_ContestList(AllContests)

    # Fetching un-attempted Contest
    #
    NeededContest=virtual_contest.getContestForVirtualParticipation(user,AllContests[1],div)

        
    # Writing available contests to VirtualContestList.csv
    #
    # virtual_contest_list_CSV.WriteToCSV_ContestList(AllContests,NeededContest)

    return NeededContest


# TryTheseContests('deepanshu_pali')