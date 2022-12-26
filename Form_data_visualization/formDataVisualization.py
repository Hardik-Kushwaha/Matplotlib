import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import numpy as np
df = pd.read_csv('Contact Information.csv')
BoysAge = [0]*5
GirlsAge = [0]*5
for gender,age in zip(df['Gender'],df['Age']):
    if gender == 'Male':
        if age == 'Below 18':
            BoysAge[0] += 1
        elif age == '18-25':
            BoysAge[1] += 1
        elif age == '25-30':
            BoysAge[2] += 1
        elif age == '30-40':
            BoysAge[3] += 1
        else:
            BoysAge[4] += 1
    else:
        if age == 'Below 18':
            GirlsAge[0] += 1
        elif age == '18-25':
            GirlsAge[1] += 1
        elif age == '25-30':
            GirlsAge[2] += 1
        elif age == '30-40':
            GirlsAge[3] += 1
        else:
            GirlsAge[4] += 1
AgeCategory = ['Below 18','18-25','25-30','30-40','40+']
width = 0.4
values = np.arange(len(AgeCategory))
fig,axis = plt.subplots(2,2)

axis[0,0].bar(values, BoysAge, label='Boys', width=width)
axis[0,0].bar(values+width, GirlsAge, label='Girls', width=width)
axis[0,0].set_title('Age distribution according to gender')
axis[0,0].legend(loc='upper right')
axis[0,0].set_xlabel('Age Distribution')
axis[0,0].set_ylabel('Number of persons')
plt.sca(axis[0, 0])
plt.xticks(values+0.2,AgeCategory)

cities = sorted(list(set(df['Address'])))
underGrad = [0]*len(cities)
grad = [0]*len(cities)
prof = [0]*len(cities)
for status,city in zip(df['Status'],df['Address']):
    if status == 'Under Graduate':
        if   city == cities[0]: underGrad[0] += 1
        elif city == cities[1]: underGrad[1] += 1
        elif city == cities[2]: underGrad[2] += 1
        elif city == cities[3]: underGrad[3] += 1
        elif city == cities[4]: underGrad[4] += 1
        elif city == cities[5]: underGrad[5] += 1
        elif city == cities[6]: underGrad[6] += 1
        elif city == cities[7]: underGrad[7] += 1
        elif city == cities[8]: underGrad[8] += 1
        elif city == cities[9]: underGrad[9] += 1
        else: underGrad[10] += 1
    elif status == 'Graduated':
        if   city == cities[0]: grad[0] += 1
        elif city == cities[1]: grad[1] += 1
        elif city == cities[2]: grad[2] += 1
        elif city == cities[3]: grad[3] += 1
        elif city == cities[4]: grad[4] += 1
        elif city == cities[5]: grad[5] += 1
        elif city == cities[6]: grad[6] += 1
        elif city == cities[7]: grad[7] += 1
        elif city == cities[8]: grad[8] += 1
        elif city == cities[9]: grad[9] += 1
        else: grad[10] += 1
    else:
        if   city == cities[0]: prof[0] += 1
        elif city == cities[1]: prof[1] += 1
        elif city == cities[2]: prof[2] += 1
        elif city == cities[3]: prof[3] += 1
        elif city == cities[4]: prof[4] += 1
        elif city == cities[5]: prof[5] += 1
        elif city == cities[6]: prof[6] += 1
        elif city == cities[7]: prof[7] += 1
        elif city == cities[8]: prof[8] += 1
        elif city == cities[9]: prof[9] += 1
        else: prof[10] += 1

axis[0,1].plot(cities, underGrad, label='UnderGrad')
axis[0,1].plot(cities, grad, label='Graduated')
axis[0,1].plot(cities, prof, label='Professional')
axis[0,1].legend(loc='upper right')
axis[0,1].set_title('Status distribution of people according to cities')
axis[0,1].set_xlabel('Cities')
axis[0,1].set_ylabel('Number of persons')

hMap = Counter(df['Address'])
theme = plt.get_cmap('jet')
exp = [0.1]*11
axis[1,0].set_prop_cycle("color", [theme(2. * i / len(df['Address'])) for i in range(len(df['Address']))])
axis[1,0].pie(hMap.values(),labels=hMap.keys(),explode=exp,autopct='%1.0f%%', pctdistance=0.8,startangle=180)
axis[1,0].set_title('Population density of Citites')

colors = sorted(list(set(df['Favourite Color'])))
maleClr = [0]*len(colors)
femaleClr = [0]*len(colors)
for gender,clr in zip(df['Gender'],df['Favourite Color']):
    if gender == 'Male':
        if clr == colors[0]: maleClr[0] += 1
        elif clr == colors[1]: maleClr[1] += 1
        elif clr == colors[2]: maleClr[2] += 1
        elif clr == colors[3]: maleClr[3] += 1
        elif clr == colors[4]: maleClr[4] += 1
        elif clr == colors[5]: maleClr[5] += 1
        else: maleClr[6] += 1
    else: 
        if clr == colors[0]: femaleClr[0] += 1
        elif clr == colors[1]: femaleClr[1] += 1
        elif clr == colors[2]: femaleClr[2] += 1
        elif clr == colors[3]: femaleClr[3] += 1
        elif clr == colors[4]: femaleClr[4] += 1
        elif clr == colors[5]: femaleClr[5] += 1
        else: femaleClr[6] += 1
axis[1,1].scatter(colors,maleClr, label='Male')
axis[1,1].scatter(colors,femaleClr, label='Female')
axis[1,1].legend(loc='upper right')
axis[1,1].set_title('Favourite color people according to gender')
axis[1,1].set_xlabel('Colors')
axis[1,1].set_ylabel('Number of persons')

plt.show()