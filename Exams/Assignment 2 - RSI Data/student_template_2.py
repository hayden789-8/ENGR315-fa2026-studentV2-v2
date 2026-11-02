"""
CULMINATING ASSIGNMENT 2: RSI

Create a program which will provide answers to the tasks posed in the assignment description.

For this assignment, you will start from scratch with this blank template.
It is your reponsibility to include all necessary program components in this file.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.

The relevant data file is named "all_participant_data_rsi.csv" and is located in data > drop-jump.

All file paths need to be relative and execute from this file's directory;
the Visual Studio Code setting "Python > Terminal: Execute in File Dir" 
must be enabled in File > Preferences > Settings.

See Canvas for additional requirements.
"""
################TASK 1##############

#read csv
import pandas as pd 

#statistical tests
from scipy import stats 


#read csv
data=pd.read_csv('data/drop-jump/all_participant_data_rsi.csv')

#store force plate rsi
force_plate=data['force_plate_rsi']

#store accelerometer rsi
accelerometer=data['accelerometer_rsi']

#t test
t_value,p_value=stats.ttest_rel(force_plate,accelerometer)

#sig level
alpha=0.05



print('-Task 1:')
print('Null hypothesis: The mean difference between the methods is zero.')
print('Alternative hypothesis: The mean difference between the two methods is not zero.')
print('T value:',round(t_value,4))
print('P value:',(p_value,))

#reject null hypothesis?
if p_value<alpha:
    print('Reject null hypothesis.')
    print('The two methods have a significant difference in mean.')
else:
    print('Fail to reject null hypothesis.')
    print('No significant mean differences.')



#############TASK 2####################

#for number calc
import numpy as np 

#for graphs
import matplotlib.pyplot as plt 

#normal distribution for accelerometer
mean,std=stats.norm.fit(accelerometer)

#histogram bins/count values
observed,bins=np.histogram(accelerometer,bins=8)

#normal distribution calc
expected=len(accelerometer)*np.diff(stats.norm.cdf(bins,mean,std))

#values outside limits in bin
expected[0]+=len(accelerometer)*stats.norm.cdf(bins[0],mean,std)

expected[-1]+=len(accelerometer)*(1-stats.norm.cdf(bins[-1],mean,std))

#chi square
chi2,p_value_chi2=stats.chisquare(observed,expected,ddof=2)


print('\n-Task 2: Chi2 Goodness of Fit Test')
print('Chi2 statistic:',round(chi2,4))
print('P value:',round(p_value_chi2,4))

#normal distribution good?
if p_value_chi2<alpha:
    print('Reject null hypothesis.')
    print('The normal distribution is not a good fit.')
else:
    print('Fail to reject null hypothesis.')
    print('The normal distribution is a good fit.')

#normal distribution curve
x=np.linspace(accelerometer.min(),accelerometer.max(),200)

#normal probability
y=stats.norm.pdf(x,mean,std)

#histogram
plt.hist(accelerometer,bins=8,density=True,alpha=0.6,label='Accelerometer RSI Data')

#normal distribution curve overlaid
plt.plot(x,y,label='Normal Distribution')

#titles/labels
plt.title('Accelerometer RSI Normal Distribution')
plt.xlabel('Reactive Strength Index (RSI)')
plt.ylabel('Probability Density')
plt.legend()

#graph!!
plt.show()




###################TASK 3####################

#participant f data
participant_f=data[data['trial'].str.startswith('F_trial_')]

#participant f
print('\n-Task 3: participant F')
print(participant_f.to_string(index=False))

#participant f rsi
force_f=participant_f['force_plate_rsi']

#participant f accelerometer
accel_f=participant_f['accelerometer_rsi']

#95% confidence interval force plate
force_ci=stats.t.interval(0.95,len(force_f)-1,loc=force_f.mean(),scale=stats.sem(force_f))

#95% confidence interval accelerometer
accel_ci=stats.t.interval(0.95,len(accel_f)-1,loc=accel_f.mean(),scale=stats.sem(accel_f))

print('\nForce plate mean RSI:',round(force_f.mean(),4))
print('Accelerometer mean RSI:',round(accel_f.mean(),4))

print('\nForce plate 95% confidence interval:',tuple(round(float(x),4) for x in force_ci))
print('Accelerometer 95% confidence interval:',tuple(round(float(x),4) for x in accel_ci))