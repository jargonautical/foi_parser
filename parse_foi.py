import csv
import sys
#sys.setdefaultencoding("ISO-8859-1")
keyword = input()
out_file = "foi_out_" + keyword + ".csv"
sys.stdout = open('foi_out_sc1.csv','w') #redirect all prints to this log file
sys.stdout = open(out_file,'w') #redirect all prints to this log file


#First, create a set of the keywords. Sets are faster than a list for
# checking if they contain an element. The curly brackets create a set.

#keywords = {'request'}
csv.field_size_limit(sys.maxsize)
#invalids = 0
#valids = 0
records = 0
filename = '161114_foi.csv'

# The with statement in Python makes sure that your file is properly closed
# (automatically) when an error occurs. This is a common idiom.
with open(filename, 'r', encoding='ISO-8859-1') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
        if keyword in row[6]:
            print("MATCH: ", row, sep = ",", file = sys.stdout)
            records += 1
    print ("Number of records containing '" + keyword + "': " +  'parsed matching records {0}'.format(records))
