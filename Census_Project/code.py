# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

census = np.append(data, new_record, axis = 0)


age = census[:, 0]
max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)


race = census[:,2]
race_0 = np.array([i for i in race if i == 0])
race_1 = np.array([i for i in race if i == 1])
race_2 = np.array([i for i in race if i == 2])
race_3 = np.array([i for i in race if i == 3])
race_4 = np.array([i for i in race if i == 4])
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
minimum = np.min([len_0,len_1,len_2,len_3,len_4])
if minimum == len_0:
    minority_race = 0
if minimum == len_1:
    minority_race = 1
if minimum == len_2:
    minority_race = 2
if minimum == len_3:
    minority_race = 3
if minimum == len_4:
    minority_race = 4


senior_citizens = np.array([i for i in age if i>60])
senior_citizens_len = len(senior_citizens)


working_hours = census[:, 6]
working_hours_sum = 0


for i in range(len(age)):
    if age[i]>60:
        working_hours_sum += working_hours[i]


avg_working_hours = round(working_hours_sum/senior_citizens_len, 2)


education_num = census[:, 1]
high = np.array([i for i in education_num if i > 10])
low = np.array([i for i in education_num if i <= 10])


pay_high = 0
pay_low = 0


income = census[:, 7]
for i in range(len(education_num)):
    if education_num[i] > 10:
        pay_high += income[i]
    if education_num[i] <= 10:
        pay_low += income[i]


avg_pay_high = round(pay_high/len(high), 2)
avg_pay_low = round(pay_low/len(low), 2)




