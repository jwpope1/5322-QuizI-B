'''
The Customer Service Represetatives (CSRs) in the marketing department with a security clearance of 'TS' were able
to thwart an attack on the server and for that management has decided to reward them with a 10% increase in their salary. 
To evaluate the impact on the budget, you have been asked to run a report on the employee file and display the results 
of BEFORE AND AFTER the salary increase. Also calculate the total difference between the old salary and the new
salary (as shown in the image).

You will create a dictionary that has the full employee name as the key and only their NEW salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as shown in the image)
'''

import csv

#open the file

outfile = open("employee_data.csv", 'r')


#create an empty dictionary

tsemp = {}
check = csv.reader(outfile, delimiter=',')
tsemp



#use a loop to iterate through the csv file
for x in check:

    #check if the employee fits the search criteria
    if x == "TS":
        print(x)

"""
print(f"Employee Name: {} Current Salary: ${}")
print(f"Employee Name: {} Current Salary: ${}")
print()
print('=========================================')
print()
print(f"Employee Name: {} Current Salary: ${}")
print(f"Employee Name: {} Current Salary: ${}")

#iternate through the dictionary and print out the key and value as per image




          

print()
print('=========================================')
print()
print(f"Total Increase in salary: ${}")
#print out the total difference between the old salary and the new salary as per image.

        
"""
outfile.close()