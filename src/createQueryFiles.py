#!/usr/bin/python
# This python script can be used to create SQL query files
# Place all your SQL queries in a single file (say, listofSQLqueries.txt)
# Then run this script and it will create a single test file for every SQL
# statement in the above file.


def createQueryFiles():
    with open('/root/listofSQLqueries.txt') as f:
        lines = f.readlines()
        i = 15
        for line in lines:
            wf = open(
                '/root/testCaseName_' +
                str(i) +
                str('.') +
                str('q'),
                'a')
            wf.write(str(line.rstrip()))
            i = i + 1

if __name__ == "__main__":
    createQueryFiles()
