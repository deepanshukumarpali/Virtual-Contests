"""
import csv

def WriteToCSV_ContestList(Contest,IDs):

    headings=['ID','NAME']
    with open('VirtualContestList.csv','w') as f:

        writer=csv.writer(f)
        writer.writerow(headings)

        for id in IDs:
            writer.writerow([id,Contest[id]]) """