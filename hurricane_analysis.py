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

# write your update damages function here:
fixed_damages = []
def fix_damage(list):
    for val in list:
        if val == 'Damages not recorded':
            fixed_damages.append(val)
        elif 'M' in val and '.' not in val:
            val1 = val.replace('M', '000000')
            fixed_damages.append(float(val1))
        elif 'M' in val and '.' in val:
            val1 = val.replace('M', '00000')
            val1 = val1.replace('.', '')
            fixed_damages.append(float(val1))        
        elif 'B' in val and '.' not in val:
            val1 = float(val.replace('B', '000000000'))
            fixed_damages.append(val1)
        elif 'B' in val and '.' in val:
            decimal_index = val.find('.')
            b_index = val.find('B')
            if b_index - decimal_index == 3:
                val1 = val.replace('B', '0000000')
                val1 = val1.replace('.', '')
                fixed_damages.append(float(val1))
            elif b_index - decimal_index == 2:
                val1 = val.replace('B', '00000000')
                val1 = val1.replace('.', '')
                fixed_damages.append(float(val1))
    return fixed_damages
fixed_damages = fix_damage(damages)








# write your construct hurricane dictionary function here:
hurricane_dict = {}
def hurricane_dict_constructor(names, months, years, max_sustained_winds, areas_affected, fixed_damages, deaths):
    for i in range(len(names)):
        hurricane_dict[names[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Winds': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': fixed_damages[i], 'Deaths': deaths[i]}
    return hurricane_dict
hurricane_dict = hurricane_dict_constructor(names, months, years, max_sustained_winds, areas_affected, fixed_damages, deaths)

# print(hurricane_dict['Cuba I']['Month'])





# write your construct hurricane by year dictionary function here:
hurricane_dict_year = {}
def hurricane_dict_year_constructor(years, names, dict):
    for i in range(len(years)):
        hurricane_dict_year[years[i]] = hurricane_dict[names[i]]
    return hurricane_dict_year
hurricane_dict_year = hurricane_dict_year_constructor(years, names, hurricane_dict)
# print(hurricane_dict_year)

# write your count affected areas function here:
area_list = []
new_area_list = []
specific_area_dict = {}
def area_count(names, hurricane_dict):
    for i in range(len(names)):
        area_list.append(hurricane_dict[names[i]]['Areas Affected'])
    for area_vals in area_list:
        for area in area_vals:
            new_area_list.append(area)
    for val in new_area_list:
        specific_count = new_area_list.count(val)
        if val not in specific_area_dict:
            specific_area_dict[val] = specific_count
    return specific_area_dict
specific_area_dict = area_count(names, hurricane_dict)





# write your find most affected area function here:
def most_affected_area(specific_area_dict):
    most_affected_count = 0
    for i in range(len(specific_area_dict)):
        key = list(specific_area_dict)[i]
        if specific_area_dict[key] > most_affected_count:
            most_affected_count = specific_area_dict[key]
    return most_affected_count
# print(most_affected_area(specific_area_dict))
    







# write your greatest number of deaths function here:
def deadliest(hurricane_dict):
    death_toll = 0
    for i in range(len(hurricane_dict)):
        key = list(hurricane_dict)[i]
        if hurricane_dict[key]['Deaths'] > death_toll:
            death_name = key
            death_toll = hurricane_dict[key]['Deaths']
    return death_name, death_toll
# print(deadliest(hurricane_dict))





# write your catgeorize by mortality function here:
def death_categorized(hurricane_dict):
    death_categorized_dict = {}
    zero_list = []
    one_list = []
    two_list = []
    three_list = []
    four_list = []
    five_list = []
    for i in range(len(hurricane_dict)):
        key = list(hurricane_dict)[i]
        value = hurricane_dict[key]['Deaths']
        if value == 0:
            zero_list.append(key)
        elif value > 0 and value <= 100:
            one_list.append(key)
        elif value > 100 and value <= 500:
            two_list.append(key)
        elif value > 500 and value <= 1000:
            three_list.append(key)
        elif value > 1000 and value <= 10000:
            four_list.append(key)
        elif value > 10000:
            five_list.append(key)
    death_categorized_dict[0] = zero_list
    death_categorized_dict[1] = one_list
    death_categorized_dict[2] = two_list
    death_categorized_dict[3] = three_list
    death_categorized_dict[4] = four_list
    death_categorized_dict[5] = five_list
    return death_categorized_dict
# print(death_categorized(hurricane_dict))
        






# write your greatest damage function here:
def costliest(hurricane):
    cost = 0
    for i in range(len(hurricane_dict)):
        key = list(hurricane_dict)[i]
        if type(hurricane_dict[key]['Damage']) == str:
            continue
        if hurricane_dict[key]['Damage'] > cost:
            most_damage = key
            most_damage_value = hurricane_dict[key]['Damage']
    return most_damage, most_damage_value 
# print(costliest(hurricane_dict))





# write your catgeorize by damage function here:
def costliest_categorized(hurricane_dict):
    costliest_categorized_dict = {}
    zero_list = []
    one_list = []
    two_list = []
    three_list = []
    four_list = []
    five_list = []
    for i in range(len(hurricane_dict)):
        key = list(hurricane_dict)[i]
        value = hurricane_dict[key]['Damage']
        if type(value) == str:
            continue
        if value == 0:
            zero_list.append(key)
        elif value > 0 and value <= 100000000:
            one_list.append(key)
        elif value > 100000000 and value <= 1000000000:
            two_list.append(key)
        elif value > 1000000000 and value <= 10000000000:
            three_list.append(key)
        elif value > 10000000000 and value <= 50000000000:
            four_list.append(key)
        elif value > 50000000000:
            five_list.append(key)
    costliest_categorized_dict[0] = zero_list
    costliest_categorized_dict[1] = one_list
    costliest_categorized_dict[2] = two_list 
    costliest_categorized_dict[3] = three_list
    costliest_categorized_dict[4] = four_list
    costliest_categorized_dict[5] = five_list
    return costliest_categorized_dict
# print(costliest_categorized(hurricane_dict))
    
        