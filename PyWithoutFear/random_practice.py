# #ch2p26
# #initialize multiple variables to a number
# a1=a2=a3=10

# #set of variables with diff values
# tt,ty,tz=10,20,30

#a ratio
# dead = 1999
# infected = 2000


# a = dead/infected

# print ("Dead %",a)

#Death Calculated based on potential recovery patientes ( recovered+dead)
#US CASES

# i=infected /r=recovered/d=Dead
# current_fatality_rate = cfr 
# potential_recovery_pool= prp 
# death_ratio_of_potenail_recov_pool = dr_recov_pool 
# potential_deaths_based_on_death_ratio = pd_based_ratio

# infected = 308044#278492#217540#211737
# recovered = 14616#9897#8802#8434
# dead = 8377#7166#5168#4718

# current_fatality_rate=round((dead/infected)*100,2)

# potential_recovery_pool = recovered + dead

# death_ratio_of_potential_recovery_pool = round ((dead/potential_recovery_pool)*100 , 2)

# potential_deaths_based_on_death_ratio = round((death_ratio_of_potential_recovery_pool*infected))

# a= 5/3
# format(a,'2f')
# print (format(a,'.2f'))
"""
lol string together
"""
us_pop = 331002651
i = 1227430
r = 189910
d = 73095
d_growth_rate= 0.03
r_growth_rate= 0.05
current_pool = r + d
#ratios
fatality_rate = d / i
pool_fr = d / current_pool

#death with pool fatality rate
p_deaths = current_pool * pool_fr
i_deaths = i * pool_fr

#deaths with current fatality rate
potential_deaths_pool = current_pool * fatality_rate
us_pop_potential_deaths = us_pop * fatality_rate

p_heal = (r * r_growth_rate) + r
p_death = (d * d_growth_rate) + d

print(
        'EXTERNAL DATA {:,}','',
        'US Pop: {:,}'.format(us_pop),
        'Infected: {:,}'.format(i),
        'Recovered: {:,}'.format(r),
        'Dead: {:,}'.format(d), 
        'Death Growth Rate: {:,.0f}'.format(d_growth_rate * 100,)+'%',
        'Recov Growth Rate: {:,.0f}'.format(r_growth_rate * 100,)+'%','',
        '<<<<<<>>>>>>>> ','',
        'Current Pool: {:,}'.format(current_pool),
        'Fatality Rate: {:,.2f}'.format(fatality_rate * 100)+'%',
        'Pool Fatality Rate: {:,.2f}'.format(pool_fr * 100)+'%',
        '',
        'NUMBERS WITH POOL FATALITY RATE [{:,.2f}'.format(pool_fr * 100)+'%]',
        'Pool Deaths: {:,}'.format(p_deaths),
        'Infected Deaths: {:,.0f}'.format(i_deaths),
        '',
        'NUMBERS WITH FATALITY RATE [{:,.2f}'.format(fatality_rate * 100)+'%]',
        'Pool Deaths: {:,.0f}'.format(potential_deaths_pool),
        'US Population Deaths: {:,.0f}'.format(us_pop_potential_deaths),
        '',
        'PROJECTED May/6',
        'New Deaths Tomorrow [Total]: {:,.0f}'.format(p_death-d),
        'New Recoveries Tomorrow [Total]: {:,.0f}'.format(p_heal-r),
        sep='\n')


#worldCASES

# infected=935817#211737
# recovered=193700#8434
# dead=47208#4718

# current_fatality_rate=dead/infected

# potential_recovery_pool = recovered + dead

# death_ratio_of_potential_recovery_pool = dead/potential_recovery_pool

# potential_deaths_based_on_death_ratio = (death_ratio_of_potential_recovery_pool*infected)
