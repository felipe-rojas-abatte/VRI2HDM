import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.interpolate
from scipy.interpolate import interp1d
import sys
import matplotlib.patches as mpatches
import matplotlib.ticker as ticker
from matplotlib.ticker import ScalarFormatter
import os

#Read the data file and save it in the variables

#(MDM,SIG)=np.genfromtxt("/home/felipe/Documents/Programas/micromegas_4.3.1f/VRI2HDM/Plots/data/LUX.dat",dtype=float,unpack=True,skip_header=False) 
#LUX_SIG=interp1d(MDM, SIG, kind='linear')

Mh = [10, 4000]
lim_inf = [0.1172,0.1172]
omega = [0.1184,0.1184]
lim_sup = [0.1196,0.1196]

current_dir = os.getcwd()
data_a2_folder = current_dir+'/data/a=2/'

#Read data for quasi-degenerate values of Masses
Mh1a, Mh2a, Mhca, MRa, ld345a ,lda, Aa, Omegaa, prota, Brh1a, Brh2a, Brhca, BrAAa, WHa = np.genfromtxt(data_a2_folder+"degen_ld345=1.dat", dtype=float, unpack=True, skip_header=True) 
Mh1b, Mh2b, Mhcb, MRb, ld345b ,ldb, Ab, Omegab, protb, Brh1b, Brh2b, Brhcb, BrAAb, WHb = np.genfromtxt(data_a2_folder+"degen_ld345=-1.dat", dtype=float, unpack=True, skip_header=True) 
Mh1c, Mh2c, Mhcc, MRc, ld345c ,ldc, Ac, Omegac, protc, Brh1c, Brh2c, Brhcc, BrAAc, WHc = np.genfromtxt(data_a2_folder+"degen_ld345=0.1.dat", dtype=float, unpack=True, skip_header=True) 
Mh1d, Mh2d, Mhcd, MRd, ld345d ,ldd, Ad, Omegad, protd, Brh1d, Brh2d, Brhcd, BrAAd, WHd = np.genfromtxt(data_a2_folder+"degen_ld345=-0.1.dat", dtype=float, unpack=True, skip_header=True) 
Mh1e, Mh2e, Mhce, MRe, ld345e ,lde, Ae, Omegae, prote, Brh1e, Brh2e, Brhce, BrAAe, WHe = np.genfromtxt(data_a2_folder+"degen_ld345=0.01.dat", dtype=float, unpack=True, skip_header=True) 
Mh1f, Mh2f, Mhcf, MRf, ld345f ,ldf, Af, Omegaf, protf, Brh1f, Brh2f, Brhcf, BrAAf, WHf = np.genfromtxt(data_a2_folder+"degen_ld345=-0.01.dat", dtype=float, unpack=True, skip_header=True) 


#Read data for no-degenerate values of Masses
Mh1i, Mh2i, Mhci, MRi, ld345i ,ldi, Ai, Omegai, proti, Brh1i, Brh2i, Brhci, BrAAi, WHi = np.genfromtxt(data_a2_folder+"nodegen_ld345=1.dat", dtype=float, unpack=True, skip_header=True) 
Mh1j, Mh2j, Mhcj, MRj, ld345j ,ldj, Aj, Omegaj, protj, Brh1j, Brh2j, Brhcj, BrAAj, WHj = np.genfromtxt(data_a2_folder+"nodegen_ld345=-1.dat", dtype=float, unpack=True, skip_header=True) 
Mh1k, Mh2k, Mhck, MRk, ld345k ,ldk, Ak, Omegak, protk, Brh1k, Brh2k, Brhck, BrAAk, WHk = np.genfromtxt(data_a2_folder+"nodegen_ld345=0.1.dat", dtype=float, unpack=True, skip_header=True) 
Mh1l, Mh2l, Mhcl, MRl, ld345l ,ldl, Al, Omegal, protl, Brh1l, Brh2l, Brhcl, BrAAl, WHl = np.genfromtxt(data_a2_folder+"nodegen_ld345=-0.1.dat", dtype=float, unpack=True, skip_header=True) 
Mh1m, Mh2m, Mhcm, MRm, ld345m ,ldm, Am, Omegam, protm, Brh1m, Brh2m, Brhcm, BrAAm, WHm = np.genfromtxt(data_a2_folder+"nodegen_ld345=0.01.dat", dtype=float, unpack=True, skip_header=True) 
Mh1n, Mh2n, Mhcn, MRn, ld345n ,ldn, An, Omegan, protn, Brh1n, Brh2n, Brhcn, BrAAn, WHn = np.genfromtxt(data_a2_folder+"nodegen_ld345=-0.01.dat", dtype=float, unpack=True, skip_header=True) 

#LUX=LUX_SIG(Mv1a)

re_sca = 0.00000001

#prot_a = ((Omegaa/0.112)*prota)/re_sca
#prot_b = ((Omegab/0.112)*protb)/re_sca
#prot_c = ((Omegac/0.112)*protc)/re_sca
#prot_d = ((Omegad/0.112)*protd)/re_sca
#prot_e = ((Omegae/0.112)*prote)/re_sca
#prot_f = ((Omegaf/0.112)*protf)/re_sca
#prot_g = ((Omegag/0.112)*protg)/re_sca
#prot_h = ((Omegah/0.112)*proth)/re_sca
#prot_i = ((Omegai/0.112)*proti)/re_sca
#prot_j = ((Omegaj/0.112)*protj)/re_sca
#prot_k = ((Omegak/0.112)*protk)/re_sca
#prot_l = ((Omegal/0.112)*protl)/re_sca
#prot_m = ((Omegam/0.112)*protm)/re_sca
#prot_n = ((Omegan/0.112)*protn)/re_sca
#prot_o = ((Omegao/0.112)*proto)/re_sca
#prot_p = ((Omegap/0.112)*protp)/re_sca

#N_LUX = LUX/re_sca

##----------------- Planck limits for Relic Density vs Mh1 for quasi-degenerate case
fig1 = plt.subplots()
#Name of axes
plt.xlabel("Mh$_1$ (GeV)",fontsize=15)
plt.ylabel("Relic Density $\\Omega h^2$",fontsize=15)
plt.title('Mh$_2$ = Mh$^{\pm}$ = Mh$_1 + 1$ GeV, M$_{\\rho}$=3000 GeV, a=2')
plt.yscale('log')  #Escala logaritmica para el eje y
plt.xscale('log')
plt.xlim(10,4000)

l1, = plt.plot(Mh1a, Omegaa, label='$\lambda_{345}=1$',color='b',linestyle='-',linewidth=1)
l2, = plt.plot(Mh1b, Omegab, label='$\lambda_{345}=-1$',color='b',linestyle='--',linewidth=1)
l3, = plt.plot(Mh1c, Omegac, label='$\lambda_{345}=0.1$',color='g',linestyle='-',linewidth=1)
l4, = plt.plot(Mh1d, Omegad, label='$\lambda_{345}=-0.1$',color='g',linestyle='--',linewidth=1)
l5, = plt.plot(Mh1e, Omegae, label='$\lambda_{345}=0.01$',color='m',linestyle='-',linewidth=1)
l6, = plt.plot(Mh1f, Omegaf, label='$\lambda_{345}=-0.01$',color='m',linestyle='--',linewidth=1)

plt.plot(Mh, lim_inf, linestyle='--',color='red')
plt.plot(Mh, lim_sup, linestyle='--',color='red')

#Creamos la primera leyenda
legend1 = plt.legend(handles=[l1,l3,l5,l2,l4,l6], loc="lower right", ncol=2, handlelength=2.5, borderaxespad=3, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

#plt.legend(loc="lower right", borderaxespad=0.1)
plt.savefig('Omega_Mh1_deg.pdf')

##------------------- Planck limits for Relic Density vs Mh1 for no-degenerate case
fig1 = plt.subplots()
#Name of axes
plt.xlabel("Mh$_1$ (GeV)",fontsize=15)
plt.ylabel("Relic Density $\\Omega h^2$",fontsize=15)
plt.title('Mh$_2$ = Mh$^{\pm}$ = Mh$_1 + 100$ GeV, M$_{\\rho}$=3000 GeV, a=2')
plt.yscale('log')  #Escala logaritmica para el eje y
plt.xscale('log')
plt.xlim(10,4000)

s1, = plt.plot(Mh1i, Omegai, label='$\lambda_{345}=1$',color='b',linestyle='-',linewidth=1)
s2, = plt.plot(Mh1j, Omegaj, label='$\lambda_{345}=-1$',color='b',linestyle='--',linewidth=1)
s3, = plt.plot(Mh1k, Omegak, label='$\lambda_{345}=0.1$',color='g',linestyle='-',linewidth=1)
s4, = plt.plot(Mh1l, Omegal, label='$\lambda_{345}=-0.1$',color='g',linestyle='--',linewidth=1)
s5, = plt.plot(Mh1m, Omegam, label='$\lambda_{345}=0.01$',color='m',linestyle='-',linewidth=1)
s6, = plt.plot(Mh1n, Omegan, label='$\lambda_{345}=-0.01$',color='m',linestyle='--',linewidth=1)

plt.plot(Mh, lim_inf, linestyle='--',color='red')
plt.plot(Mh, lim_sup, linestyle='--',color='red')

#Creamos la primera leyenda
legend2 = plt.legend(handles=[s1,s3,s5,s2,s4,s6], loc="upper right", ncol=2, handlelength=2.5, borderaxespad=0.5, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

plt.savefig('Omega_Mh1_nodeg.pdf')


#plt.show()


plt.clf()
