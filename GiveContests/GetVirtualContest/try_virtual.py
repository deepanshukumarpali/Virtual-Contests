from . import contest_list
from . import contest_list_CSV
from . import virtual_contest
from . import virtual_contest_list_CSV




def TryTheseContests(user,div):

    try:
        
        # Fetchting all codeforces Contests
        #
        AllContests=contest_list.GetContestIDs(div)


        # Writing all contest to ContestList.csv
        #
        # contest_list_CSV.WriteToCSV_ContestList(AllContests)


        # Fetching un-attempted Contest
        #
        NeededContest=virtual_contest.getContestForVirtualParticipation(user,AllContests,div)

        
        # Writing available contests to VirtualContestList.csv
        #
        # virtual_contest_list_CSV.WriteToCSV_ContestList(AllContests,NeededContest)

        return NeededContest


    except: return False

# TryTheseContests('deepanshu_pali')