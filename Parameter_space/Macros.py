from __future__ import division
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.interpolate
import sys
import matplotlib.patches as mpatches
from scipy.interpolate import interp1d
import matplotlib.ticker as mtick
import shutil as sh
import math
import os
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset


# Abro archivo con base de datos
print('Reading data files')
exec(open('data.py').read())

# Abro archivo con cortes
print('Reading cuts file')
exec(open('cuts.py').read())

# Abro archivo con graficos

######################
# plot_set:
#   0 = No cuts
#   1 = Bounded from Below limits on the potential
#   2 = 1 + Stability of the Potential 
#   3 = 2 + Perturbativity and Unitarity Constraints
#   4 = 3 + Electroweak precision Test
#   5 = 4 + LEP limits 
#   6 = 5 + LHC Higgs constraints (Diphoton Higgs decay, Invisible Braching)
#   7 = 6 + Upper PLANCK limit
#   8 = 7 + LUX limits
#   10 = 8 + Lower PLANCK limit    
# 

plot_set=2

print('----------------------')
print('  Generating plots:')
print('----------------------')

if plot_set==1:
	cut=cut0
	cuts='no_cuts'
	print('	Generating plots with no cuts \n')
	exec(open('plots.py').read())

if plot_set==1:
	cut=cut0&cut1
	cuts='cut1'
	print('	Generating plots with '+cuts+': ')
	print('	   - Bounded from Below limits on the potential \n')
	exec(open('plots.py').read())

if plot_set==1:
	cut=cut0&cut1&cut2
	cuts='cut12'
	print('	Generating plots with '+cuts+': ')
	print('	   - Bounded from Below limits on the potential')
	print('	   - Stability of the Potential \n')
	exec(open('plots.py').read())

##################################

if plot_set==1:
	cut=cut0&cut1&cut2&cut3
	cuts='cut123'
	print('	Generating plots with '+cuts+': ')
	print('	   - Bounded from Below limits on the potential')
	print('	   - Stability of the Potential')
	print('	   - Perturbativity and Unitarity Constraints \n')
	exec(open('plots.py').read())

if plot_set==1:
	cut=cut0&cut1&cut2&cut3&cut4
	cuts='cut1234'
	print('	Generating plots with '+cuts+': ')
	print('	   - Bounded from Below limits on the potential')
	print('	   - Stability of the Potential')
	print('	   - Perturbativity and Unitarity Constraints ')
	print('	   - Electroweak precision test \n')
	exec(open('plots.py').read())

if plot_set==1:
	cut=cut0&cut1&cut2&cut3&cut4&cut5
	cuts='cut12345'
	print('	Creando graficos con '+cuts+': ')
	print('	   - Bounded from Below limits on the potential')
	print('	   - Stability of the Potential')
	print('	   - Perturbativity and Unitarity Constraints')	
	print('	   - Electroweak precision test ')
	print('	   - LEP limits \n')
	exec(open('plots.py').read())

if plot_set==1:
	cut=cut0&cut1&cut2&cut3&cut4&cut5&cut6
	cuts='cut123456'
	print('	Creando graficos con '+cuts+': ')
	print('	   - Bounded from Below limits on the potential')
	print('	   - Stability of the Potential')
	print('	   - Perturbativity and Unitarity Constraints')	
	print('	   - Electroweak precision test ')
	print('	   - LEP limits ')
	print('	   - LHC Higgs constraints \n')
	exec(open('plots.py').read())

if plot_set==1:
	cut=cut0&cut1&cut2&cut3&cut4&cut5&cut6&cut7
	cuts='cut1234567'
	print('	Creando graficos con '+cuts+': ')
	print('	   - Bounded from Below limits on the potential')
	print('	   - Stability of the Potential')
	print('	   - Perturbativity and Unitarity Constraints')	
	print('	   - Electroweak precision test ')
	print('	   - LEP limits ')
	print('	   - LHC Higgs ')
	print('	   - Upper PLANCK limit \n')
	exec(open('plots.py').read())

if plot_set==2:
	cut=cut0&cut1&cut2&cut3&cut4&cut5&cut6&cut7&cut8
	cuts='cut12345678'
	print('	Creando graficos con '+cuts+': ')
	print('	   - Bounded from Below limits on the potential')
	print('	   - Stability of the Potential')
	print('	   - Perturbativity and Unitarity Constraints')	
	print('	   - Electroweak precision test ')
	print('	   - LEP limits ')
	print('	   - LHC Higgs ')
	print('	   - Upper PLANCK limit ')
	print('	   - Limites XENON \n')
	exec(open('plots.py').read())

if plot_set==2:
	cut=cut0&cut1&cut2&cut3&cut4&cut5&cut6&cut7&cut10
	cuts='cut123456710'
	print('	Creando graficos con '+cuts+': ')
	print('	   - Bounded from Below limits on the potential')
	print('	   - Stability of the Potential')
	print('	   - Perturbativity and Unitarity Constraints')	
	print('	   - Electroweak precision test ')
	print('	   - LEP limits ')
	print('	   - LHC Higgs ')
	print('	   - Upper PLANCK limit ')
	print('	   - Limites XENON ')
	print('	   - Lower PLANCK limit \n')
	exec(open('plots_sat.py').read())

print('------------------------')
print('  Done !!!')
print('------------------------')
plt.clf()

