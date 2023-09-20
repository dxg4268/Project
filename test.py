# test.py
"""
This whole content is to be appended to the main project file.
Notes:
    1. addRecord function's prompt just stores the data in csv file and function purpose is to actually execute the query, add codeaccordingly
    2. delRecord just calls the prompt and prompt does everything but code need to be added to it.

"""

import input_window
import csv
import mysql.connector as rt

#cn = rt.connect(host="localhost", user="root", passwd="", database="Hospital")
#cr = cn.cursor()

def addRecord():
    # Run the PyQt input window
    input_window.main()

    # After the input window is closed, read data from the CSV file
    with open("data.csv", mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            docID, docName, gen, dept, sal, exp, dob = row

        q = f'insert into Emp values({docID}, "{docName}", "{gen}", "{dept}", {sal}, {exp}, "{dob}")'
        print(q)


def delRecord():
    import delete_data
    delete_data.main()


def updateRecord():
    import update_record
    update_record.main()

    with open("update.csv", mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            docID, docName, gen, dept, sal, exp, dob = row
       

        q1 = f'update emp set DocName="{docName}" where DocID={docID};'
        q2 = f'update emp set Gender="{gen}" where DocID={docID};'
        q3 = f'update emp set Dept="{dept}" where DocID={docID};'
        q4 = f'update emp set Sal={sal} where DocID={docID};'
        q5 = f'update emp set Experience={exp} where DocID={docID};'
        q6 = f'update emp set DOB="{dob}" where DocID={docID};'
        
        print(q1)
        # use try block to update the values else display that docID does not exist
        try:
            pass

        except:
            print("Given DocID not found")


def searchRecord():
    import search_record
    search_record.main()


if __name__ == "__main__":
    searchRecord()

