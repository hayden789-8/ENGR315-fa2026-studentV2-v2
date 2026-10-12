import sys

"""
Create a program which will provide answers to the questions posed in the assignment description.
We've provided a function which will parse the NYT covid database file (named "us-counties.csv"); 
however, its correct implementation will be up to you. DO NOT MODIFY THIS FUNCTION.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
"""


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information

    ____________________ DO NOT MODIFY THIS FUNCTION ___________________
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

################# YOUR CODE HERE #######################

#path to the COVID data 
file_path='data/covid/us-counties.csv'

#function to read the data file and store all data
data=parse_nyt_data(file_path)

#empty lists to store 
harrisonburg=[]
rockingham=[]

#looking through COVID file
for entry in data:
    
    #Check for harrisonburg 
    if entry[1]=='Harrisonburg city' and entry[2]=='Virginia':

        #store harrisonburg data in harrisonburg list
        harrisonburg.append(entry)
    
    #check for rockingham
    if entry[1]=='Rockingham' and entry[2]=='Virginia':
       
        #store rockingham data in rockingham list
        rockingham.append(entry)

################# QUESTION 1#######################

#variables for the first case dates
harrisonburg_first=''
rockingham_first=''

#check harrisonburg list
for entry in harrisonburg:

    #check first entry with more than 0 cumulative cases
    if entry[4]>0 and harrisonburg_first=='':
       
        #Store it
        harrisonburg_first=entry[0]

#check rockingham list
for entry in rockingham:

    #check first entry with more than 0 cumulative cases
    if entry[4]>0 and rockingham_first=='':

        #store it
        rockingham_first=entry[0]

print('-Question 1:')
print('Harrisonburg first positive case:','('+str(harrisonburg_first)+')')
print('Rockingham County first positive case:','('+str(rockingham_first)+')')

#################### QUESTION 2###################

#largest daily=0
harrisonburg_max=0

#harrisonburgs largest increase
harrisonburg_max_date=''

#compare harrisonburg day with yesterday
for i in range(1,len(harrisonburg)):

    #new cases calculation subtracting the previous cumulative total
    new_cases=harrisonburg[i][4]-harrisonburg[i-1][4]

    #daily increase>than previous max
    if new_cases>harrisonburg_max:

        #new largest number of cases
        harrisonburg_max=new_cases

        #largest increase
        harrisonburg_max_date=harrisonburg[i][0]

#largest daily increase for rockingham=0
rockingham_max=0

#rockingham largest increase
rockingham_max_date=''

#compare rockingham day with yesterday
for i in range(1,len(rockingham)):

    #new cases calculation by subtracting the previous cumulative total
    new_cases=rockingham[i][4]-rockingham[i-1][4]

    #daily increase>than the previous maximum
    if new_cases>rockingham_max:

        #new largest number of cases
        rockingham_max=new_cases

        #largest increase occurred
        rockingham_max_date=rockingham[i][0]

print('-Question 2:')
print('Harrisonburg greatest new cases:','('+str(harrisonburg_max_date)+')','('+str(harrisonburg_max)+')')
print('Rockingham County greatest new cases:','('+str(rockingham_max_date)+')','('+str(rockingham_max)+')')

#################### QUESTION 3###################

#harrisonburgs largest 7-day increase=0
harrisonburg_week_max=0

#store beginning/ending dates
harrisonburg_week_start=''
harrisonburg_week_end=''

#harrisonburg data starting 7-day entries after the beginning
for i in range(7,len(harrisonburg)):

    #new cases over 7-days using the cumulative totals
    seven_day_cases=harrisonburg[i][4]-harrisonburg[i-7][4]

    #Check if this 7-day increase is the largest
    if seven_day_cases>harrisonburg_week_max:

        #largest 7-day increase
        harrisonburg_week_max=seven_day_cases

        #first date in 7-day period
        harrisonburg_week_start=harrisonburg[i-6][0]

        #last date in 7-day period
        harrisonburg_week_end=harrisonburg[i][0]

#rockinghams largest seven-day increase=0
rockingham_week_max=0

#beginning/ending dates
rockingham_week_start=''
rockingham_week_end=''

#rockingham list starting 7 entries
for i in range(7,len(rockingham)):

    #new cases over 7 days using the cumulative totals
    seven_day_cases=rockingham[i][4]-rockingham[i-7][4]

    #is 7-day increase largest? 
    if seven_day_cases>rockingham_week_max:

        #new largest 7-day case increase
        rockingham_week_max=seven_day_cases

        #first date in the 7-day period
        rockingham_week_start=rockingham[i-6][0]

        #last date in 7-day period
        rockingham_week_end=rockingham[i][0]

print('-Question 3:')
print('Harrisonburg worst seven-day period:','('+str(harrisonburg_week_start)+') to ('+str(harrisonburg_week_end)+') ('+str(harrisonburg_week_max)+')')
print('Rockingham County worst seven-day period:','('+str(rockingham_week_start)+') to ('+str(rockingham_week_end)+') ('+str(rockingham_week_max)+')')  