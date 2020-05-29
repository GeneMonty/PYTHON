# Stats from JH website

#US Data

us_pop = 331002651
c= 1227430 #confirmed
d= 73095  #deaths
r= 189910 #recovered
ts= 7759771 #number of performed tests

#El fatality Rate d/c de los infected
infected_fatality_rate = d/c

#Porcentaje de pruebas ralizadas en ralacion a toda la poblacion
testing_ratio = ts / us_pop

#De todos los tested cuantos es el % de infectados
infection_ratio = c/ts

#De todos los tested cuanto es el % de muertos
death_ratio =  d / ts

#De todos los tested cuanto es el % de recuperados
recovered_ratio = r/ ts


#if all population gets infected

a_c=us_pop
a_d=0



print(
        'US Pop: {:,}'.format(us_pop),'\n'
        'Performed Tests: {:,}'.format(ts),  '\n\n'
        'Tested Population: % {:,.2f}'.format(testing_ratio*100),'\n'
        'From all the performed tests the ratio of:','\n\n'
        'Infection: % {:,.2f}'.format(infection_ratio * 100),
        '\n'
        'Death: % {:,.2f}'.format(death_ratio *100),
        '\n'
        'Recovered: % {:,.2f}'.format(recovered_ratio * 100),'\n\n'

        'EXTERNAL DATA','\n\n'
        'Infected: {:,}'.format(c),'\n'
        'Recovered: {:,}'.format(r),'\n'
        'Dead: {:,}'.format(d), '\n'
        'Infected Fatality Rate: % {:,.2f}'.format(infected_fatality_rate * 100),'\n\n'



)
