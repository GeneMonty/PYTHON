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
infected=217540#211737
recovered=8802#8434
dead=5168#4718

current_fatality_rate=dead/infected

potential_recovery_pool = recovered + dead

death_ratio_of_potential_recovery_pool = dead/potential_recovery_pool

potential_deaths_based_on_death_ratio = (death_ratio_of_potential_recovery_pool*infected)

#worldCASES

# infected=935817#211737
# recovered=193700#8434
# dead=47208#4718

# current_fatality_rate=dead/infected

# potential_recovery_pool = recovered + dead

# death_ratio_of_potential_recovery_pool = dead/potential_recovery_pool

# potential_deaths_based_on_death_ratio = (death_ratio_of_potential_recovery_pool*infected)
