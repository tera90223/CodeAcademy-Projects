#!/usr/bin/env python
# coding: utf-8

# In[2]:


# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
def updated_damages(list_damages):
    updated_damages = []
    for cost in list_damages:
        if cost[-1] == 'M':
            cost = cost[:-1] 
            cost = float(cost) * 10**6
            updated_damages.append(cost)
        elif cost[-1] == 'B':
            cost = cost[:-1] 
            cost = float(cost) * 10**9
            updated_damages.append(cost)
        else:
            updated_damages.append(cost)
    return updated_damages

# test function by updating damages
ud_damages = updated_damages(damages)
print(ud_damages)

# 2 
# Create a Table
def hurricane_information(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricane_info = {}
    updated_damage_cost = updated_damages(damages)
    
    for n in range(0, len(names)):
        
        hurricane_info[names[n]] = {"Name": names[n], "Month": months[n],
                                "Year": years[n], 
                                "Max Sustained Wind": max_sustained_winds[n], 
                                "Areas Affected": areas_affected[n], 
                                "Damage": updated_damage_cost[n], "Deaths": deaths[n]
                               }
    return hurricane_info
# Create and view the hurricanes dictionary
updated_hurricane_info = hurricane_information(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
print("\n\n", updated_hurricane_info)

# 3
# Organizing by Year
from collections import defaultdict as dd 
def hurricane_information_by_year(hurricane_information):
    #create a new dictionary for the return value
    hurricane_by_year = dd(list)
    
    #parse through the dictionary provided to the function
    for info in hurricane_information.values():
        #create a variable to get year from the current key:value
        year = info.get("Year")
        
        #check if year is in the new dictionary
        #if True, append info to list
        # if false, create list with info
        #if year in hurricane_by_year:
        hurricane_by_year[year].append(info)
        #else:
         #   hurricane_by_year[year].append(info)    
    return hurricane_by_year

# create a new dictionary of hurricanes with year and key
sort_hurricane_information_by_year = hurricane_information_by_year(updated_hurricane_info)
print("\n\nHere is the hurricane information sorted by years: \n ", sort_hurricane_information_by_year)

# 4
# Counting Damaged Areas
def count_affected_areas(hurricane_information):
    counted_areas = {}
    
    for info in hurricane_information.values():
        areas = info.get("Areas Affected")
        for area in areas:
            if area in counted_areas:
                num = counted_areas.setdefault(area)
                num += 1
                counted_areas[area] = num
            else: 
                num = 1
                counted_areas[area] = num
    return counted_areas

# create dictionary of areas to store the number of hurricanes involved in
areas_counter_test = count_affected_areas(updated_hurricane_info)
print("\n\nThe next dictionary shows how many times an affected area was hit by a hurricane in our hurricane list. \n", areas_counter_test)

# 5 
# Calculating Maximum Hurricane Count
from collections import OrderedDict

def most_affected_area(count_affected_areas):
    od= OrderedDict(count_affected_areas)
    return list(od.items())[0]

# find most frequently affected area and the number of hurricanes involved in
temp = most_affected_area(areas_counter_test)
print("\n\nThe most affected area is " + str(temp[0]) + " with a number of " + str(temp[1]) + " hurricanes occurring in this area.")

# 6
# Calculating the Deadliest Hurricane
def most_hurricane_deaths(hurricane_information):
    hurricane_deaths = {}
    
    for name, info in hurricane_information.items():
        deaths = info.get("Deaths")
        hurricane_deaths[name] = deaths
    
    sorted_deaths = {key:value for key, value in sorted(hurricane_deaths.items(), key=lambda items:items[1])}
    
    return list(sorted_deaths.items())[-1] 
# find highest mortality hurricane and the number of deaths
most_deaths = most_hurricane_deaths(updated_hurricane_info)
print("\n\nThe hurricane which caused " + str(most_deaths[1]) + " deaths, making it the deadliest hurricane, was named " + str(most_deaths[0]) + ".")
                         
# 7
# Rating Hurricanes by Mortality
def mortality_ratings(hurricane_information):
    
    hurricane_mortality_ratings = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    
    for info in hurricane_information.values():
        death = info.get("Deaths")
        
        if death == 0:
            hurricane_mortality_ratings[0].append(info)
        elif death > 0 and death < 100:
            hurricane_mortality_ratings[1].append(info)
        elif death > 100 and death <= 500:
            hurricane_mortality_ratings[2].append(info)
        elif death > 500 and death <= 1000:
            hurricane_mortality_ratings[3].append(info)
        elif death > 1000 and death <= 10000:
            hurricane_mortality_ratings[4].append(info)
        elif death > 10000:
            hurricane_mortality_ratings[5].append(info)
            
    return hurricane_mortality_ratings

# categorize hurricanes in new dictionary with mortality severity as key
mortality_scalings = mortality_ratings(updated_hurricane_info)

print("\n\nHere is the hurricanes categorized by there mortality severity. The higher the ranking, the higher the mortality rate.\n", mortality_scalings)

# 8 Calculating Hurricane Maximum Damage
def most_damage(hurricane_information):
    damage_dict = {}
    
    for name, info in hurricane_information.items():
        damage = info.get('Damage')
        
        if damage == "Damages not recorded":
            damage = float(0)
            
        damage_dict[name] = damage
        
    sort_damage_dict = {key:value for key,value in sorted(damage_dict.items(),
                        key = lambda items:items[1])}
                        
    return (list(sort_damage_dict.items())[-1])
# find highest damage inducing hurricane and its total cost
greatest_damage = most_damage(updated_hurricane_info)
print("\n\nHurricane " + str(greatest_damage[0]) + " caused the most damage, resulting in the US spending " + str(greatest_damage[1]) + " dollars in reconstruction costs.")

# 9
# Rating Hurricanes by Damage
def damage_ratings(hurricane_information):
    hurricane_damage_ratings = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    
    for info in hurricane_information.values():
        damage = info.get('Damage')
        
        if damage == 0 or damage == "Damages not recorded":
            hurricane_damage_ratings[0].append(info)
        elif damage > 0 and damage <= 100000000:
            hurricane_damage_ratings[1].append(info)
        elif damage > 100000000 and damage <= 1000000000:
            hurricane_damage_ratings[2].append(info)
        elif damage > 1000000000 and damage <= 10000000000:
            hurricane_damage_ratings[3].append(info)
        elif damage > 10000000000 and damage <= 50000000000:
            hurricane_damage_ratings[4].append(info)
        elif damage > 50000000000:
            hurricane_damage_ratings[5].append(info)
            
    return hurricane_damage_ratings
# categorize hurricanes in new dictionary with damage severity as key
damage_scalings = damage_ratings(updated_hurricane_info)
print("\n\nHere is the hurricanes categorized by there damage severity. The higher the ranking, the higher the cost of damages for the US.\n", damage_scalings)


# In[ ]:




