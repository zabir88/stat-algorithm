import numpy as np
import matplotlib.pyplot as plt
import os
from functions_for_data import *

#Calling 3 data files from Directory A0_0
os.chdir('C:\Users\Zabir\Desktop\Physics\Python Independent Study\VMcorrs_20X128\840\A0_0')
mminus1_N0 = individual_datfile('KStarZero_JOne_mMinusOne_To_JOne_mMinusOne_Nsrc15_Ncfg199_20x128_um0p0840_sm0p0743_A0_0_sh_pt.dat')
mplus1_N0 = individual_datfile('KStarZero_JOne_mOne_To_JOne_mOne_Nsrc15_Ncfg199_20x128_um0p0840_sm0p0743_A0_0_sh_pt.dat') 
m0_N0 = individual_datfile('KStarZero_JOne_mZero_To_JOne_mZero_Nsrc15_Ncfg199_20x128_um0p0840_sm0p0743_A0_0_sh_pt.dat')

#Calling 3 data files from Directory A12_4
os.chdir('C:\Users\Zabir\Desktop\Physics\Python Independent Study\VMcorrs_20X128\840\A12_4')
mminus1_Nplus= individual_datfile('KStarZero_JOne_mMinusOne_To_JOne_mMinusOne_Nsrc15_Ncfg199_20x128_um0p0840_sm0p0743_A12_4_sh_pt.dat')
mplus1_Nplus= individual_datfile('KStarZero_JOne_mOne_To_JOne_mOne_Nsrc15_Ncfg199_20x128_um0p0840_sm0p0743_A12_4_sh_pt.dat')
m0_Nplus= individual_datfile('KStarZero_JOne_mZero_To_JOne_mZero_Nsrc15_Ncfg199_20x128_um0p0840_sm0p0743_A12_4_sh_pt.dat')

#Calling 3 data files from Directory A12_m4
os.chdir('C:\Users\Zabir\Desktop\Physics\Python Independent Study\VMcorrs_20X128\840\A12_m4')
mminus1_Nminus= individual_datfile('KStarZero_JOne_mMinusOne_To_JOne_mMinusOne_Nsrc10_Ncfg199_20x128_um0p0840_sm0p0743_A12_m4_sh_pt.dat')
mplus1_Nminus= individual_datfile('KStarZero_JOne_mOne_To_JOne_mOne_Nsrc10_Ncfg199_20x128_um0p0840_sm0p0743_A12_m4_sh_pt.dat')
m0_Nminus= individual_datfile('KStarZero_JOne_mZero_To_JOne_mZero_Nsrc10_Ncfg199_20x128_um0p0840_sm0p0743_A12_m4_sh_pt.dat')

#Average of +m and -m for all 3 Directories
avg_m_N0= array_avg(mminus1_N0,mplus1_N0)
avg_m_Nplus= array_avg(mminus1_Nplus,mplus1_Nplus)
avg_m_Nminus= array_avg(mminus1_Nminus,mplus1_Nminus)
 
#Arithmetic Mean 
z1= arithmetic_mean(avg_m_Nplus, avg_m_Nminus, avg_m_N0)
z2= arithmetic_mean(m0_Nplus, m0_Nminus, m0_N0)

#Geometric Mean
z3= geometric_mean(avg_m_Nplus, avg_m_Nminus, avg_m_N0)
z4= geometric_mean(m0_Nplus, m0_Nminus, m0_N0)

#Effective Mass Log Values of Arithmetic and Geometric Mean 
logz1= log_values(z1)    
logz2= log_values(z2)
logz3= log_values(z3)
logz4= log_values(z4)

#Average Effective Mass (Average of Arithmetic and Geometric Mean, then ratio and then the log values of them)  
mean_logz1= mean_log_values(z1)
mean_logz2= mean_log_values(z2)
mean_logz3= mean_log_values(z3)
mean_logz4= mean_log_values(z4)

'''#Standard Deviation 
stdlogz1= standard_dev(logz1, mean_logz1)
stdlogz2= standard_dev(logz2, mean_logz2)
stdlogz3= standard_dev(logz3, mean_logz3)
stdlogz4= standard_dev(logz4, mean_logz4)'''
print logz1.shape
print mean_logz1.shape
'''#Bootstrapped Arithmetic Mean
bootstrap_z1= bootstrap(z1,796, True)
bootstrap_z2= bootstrap(z2,796, True)

#Bootstrapped Geometric Mean
bootstrap_z3= bootstrap(z3,796, True)
bootstrap_z4= bootstrap(z4,796, True)

#Log Values of Bootstrapped Arithmetic and Geometric Mean 
bootstrap_logz1= bootstrap_log_values(bootstrap_z1)    
bootstrap_logz2= bootstrap_log_values(bootstrap_z2)
bootstrap_logz3= bootstrap_log_values(bootstrap_z3)
bootstrap_logz4= bootstrap_log_values(bootstrap_z4)

#Bootstrapped Effective Mass(Average of Bootstrapped Arithmetic and Geometric Mean, then ratio and then the log values of them) 
bootstrap_mean_logz1= bootstrap_mean_log_values(bootstrap_z1)
bootstrap_mean_logz2= bootstrap_mean_log_values(bootstrap_z2)
bootstrap_mean_logz3= bootstrap_mean_log_values(bootstrap_z3)
bootstrap_mean_logz4= bootstrap_mean_log_values(bootstrap_z4)

#Bootstrapped Standard Deviation 
bootstrap_stdlogz1= bootstrap_standard_dev(bootstrap_logz1, bootstrap_mean_logz1)
bootstrap_stdlogz2= bootstrap_standard_dev(bootstrap_logz2, bootstrap_mean_logz2)
bootstrap_stdlogz3= bootstrap_standard_dev(bootstrap_logz3, bootstrap_mean_logz3)
bootstrap_stdlogz4= bootstrap_standard_dev(bootstrap_logz4, bootstrap_mean_logz4)'''

#Time axis
t= (np.array(range(127), dtype=np.float64)).reshape(127,1)

'''#Plotting 
x1= plt.subplot(211)
x1.errorbar(t,mean_logz1,stdlogz1,linestyle= '-',label= "Arithmetic Mean", marker='.')
x1.set_xlabel('time')
x1.set_ylabel('Arithmetic Mean')
x1.legend(loc='upper left')
ax1= x1.twinx()
ax1.errorbar(t, bootstrap_mean_logz1, bootstrap_stdlogz1, linestyle= '-', label= 'Bootstrapped Arithmetic Mean', marker='.',fmt= 'rd')
ax1.set_ylabel('Bootstrapped Arithmetic Mean')
ax1.legend(loc='upper right')
plt.title('Standard deviation of Arithmetic and Bootstrapped Arithmetic Mean of Average Spin and field = 4')
plt.xlim([0,40])
x1.set_ylim([-0.01, 0.01])
ax1.set_ylim([-0.01, 0.01])

x2= plt.subplot(212)
x2.errorbar(t,mean_logz2,stdlogz2,linestyle= '-', label= 'Arithmetic Mean', marker='.')
x2.set_xlabel('time')
x2.set_ylabel('Arithmetic Mean')
x2.legend(loc='upper left')
ax2= x2.twinx()
ax2.errorbar(t, bootstrap_mean_logz2, bootstrap_stdlogz2, linestyle= '-',label= 'Bootstrapped Arithmetic Mean', marker='.',fmt= 'rd')
ax2.set_ylabel('Bootstrapped Arithmetic Mean')
ax2.legend(loc='upper right')
plt.title('Standard deviation of Arithmetic and Bootstrapped Arithmetic Mean of Zero Spin and field = 4')
plt.xlim([0,40])
x2.set_ylim([-0.01, 0.01])
ax2.set_ylim([-0.01, 0.01])

plt.show()'''
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 




