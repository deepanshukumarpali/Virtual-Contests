"""import csv

def WriteToCSV_ContestList(Contest):

    headings=['ID','NAME']
    with open('ContestList.csv','w') as f:

        writer=csv.writer(f)
        writer.writerow(headings)

        for con in Contest:
            writer.writerow([con,Contest[con]])"""