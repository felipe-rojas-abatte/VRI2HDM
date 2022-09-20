# Excludes anomalous Relic Density points  
cut0=(omega>0)

########################
#Teoretical constraints#
########################

#--------Definition of parameters
pi=np.pi
EE=0.31343     
MZ=91.188
MW=80.385      
CW=MW/MZ 
SW =(1-CW**2)**0.5 
vv=2*MW/EE*SW
MH=125
alp=EE**2/(4*pi)

#-------Definition of lambda couplings as function of independet parameters
l1=(EE/SW*MH/MW)**2/8  #CAMBIAR A 8
l2=ld
ld_max=4*pi/3
l345_min=-2.*(l1*ld_max)**0.5
l3 =2./vv**2*(Mhp**2+1/2*ld345*vv**2-Mh1**2)
l4 =1./vv**2*(Mh2**2+Mh1**2-2*Mhp**2) 
l5 =1./vv**2*(Mh1**2-Mh2**2) 

#------Definition of eigenvectors for unitarity 
e1=l3+l4
e2=l3-l4
e3=l3+l5
e4=l3-l5
e5=l3+2*l4+3*l5
e6=l3+2*l4-3*l5
e7=-l1-l2+((l1-l2)**2+l4**2)**0.5
e8=-l1-l2-((l1-l2)**2+l4**2)**0.5
e9= -3*l1-3*l2+(9*(l1-l2)**2+(2*l3+l4)**2)**0.5
e10=-3*l1-3*l2-(9*(l1-l2)**2+(2*l3+l4)**2)**0.5
e11=-l1-l2+((l1-l2)**2+l5**2)**0.5
e12=-l1-l2-((l1-l2)**2+l5**2)**0.5

#-------Bounded from Below limits on the potential
cutV1 = (l1>0)
cutV2 = (l2>0)                      
cutV3 = (2*(l1*l2)**0.5+l3>0)       #(check)
cutV4 = (2*(l1*l2)**0.5+l3+l4+l5>0) #(check)
cutV5 = (2*(l1*l2)**0.5+l3+l4-l5>0) #(check)

cut1 = cutV1&cutV2&cutV3&cutV4#&cutV5

#-------Stability of the Potential
cut_inert1 = (Mh1>0)
cut_inert2 = ( (Mh1/vv)**2 > (ld345/2 - (l1*l2)**0.5))
cut_neut = (l5<0)&(l4+l5<0) 

cut2 = cut_inert1&cut_inert2&cut_neut 

#-------Perturbativity and Unitarity Constraints
cut_pert=(abs(l1)<8*pi)&(abs(l2)<8*pi)&(abs(l3)<8*pi)&(abs(l4)<8*pi)

cut_unit=(abs(e1)<8*pi)&(abs(e2)<8*pi)&(abs(e3)<8*pi)&(abs(e4)<8*pi)&(abs(e5)<8*pi)&(abs(e6)<8*pi)&(abs(e7)<8*pi)&(abs(e8)<8*pi)&(abs(e9)<8*pi)&(abs(e10)<8*pi)&(abs(e11)<8*pi)&(abs(e12)<8*pi)

cut_unit2=(ld345<12.)

cut3 = cut_pert&cut_unit&cut_unit2

#------Electroweak Precision Test
def ft(x,y):
    with np.errstate(divide='ignore', invalid='ignore'):  # elimino el warning de division por 0
       ft=(x+y)/2-x*y/(x-y)*np.log(x/y)
       ft=np.nan_to_num(ft)  # Replace nan with zero and inf with finite numbers.
    return ft

def mhprlim(l3):
    return np.fmax(0.21*l3+0.639,-0.5*l3+1.6)
   
def fs(x1,x2):
    with np.errstate(divide='ignore', invalid='ignore'):
       fs1=-(x1-x2)*(5*x1**2-22*x1*x2+5*x2**2)/(x1-x2)**3
       fs2= (6*x1**2*(x1-3*x2)*np.log(x1))/(x1-x2)**3
       fs3=(-6*x2**2*(x2-3*x1)*np.log(x2))/(x1-x2)**3
       fs=fs1+fs2+fs3
       fs=np.nan_to_num(fs)
    return fs

x1=(Mh1/Mhp)**2
x2=(Mh2/Mhp)**2

#-----Evaluation of S and T Chi^2 limit

Sn=1./(72*pi)*fs(x1,x2)
Tn=1./(32*pi**2*alp*vv**2)*(ft(Mhp**2,Mh2**2)+ft(Mhp**2,Mh1**2)-ft(Mh2**2,Mh1**2))

rho_ST=0.91	
DS=0.09
DSi=DS*(1-rho_ST**2)**0.5
Smid=0.06
DT=0.07
DTi=DT*(1-rho_ST**2)**0.5
Tmid=0.1
chi2lim2=5.99	
chi2lim1=2.30
#chi2lim2=3.84	
#chi2lim1=1
#deltaS=(Sn-Smid)
#deltaT=(Tn-Tmid)
chi2ST=1./(1.-rho_ST**2)*( (Sn-Smid)**2/DS**2+(Tn-Tmid)**2/DT**2-2.*(Sn-Smid)*(Tn-Tmid)*rho_ST/(DS*DT))
TB=np.linspace(Tmid-4*DT,Tmid+4*DT,51,endpoint=True)
SB=np.linspace(Smid-4*DS,Smid+4*DS,51,endpoint=True)
Sv,Tv = np.meshgrid(SB,TB)
chi2STc=1./(1.-rho_ST**2)*((Sv-Smid)**2/DS**2+(Tv-Tmid)**2/DT**2-2.*(Sv-Smid)*(Tv-Tmid)*rho_ST/(DS*DT))
del x1,x2

cut4=(chi2ST<chi2lim2)

##############################
#Experimantal LHC constraints#
##############################

#----- LEP limits
MZ=91.188 #(Z-boson mass)
MW=80.385 #(W-boson mass)

cut_LEPW = (Mh1+Mhp > MW)&(Mh2+Mhp > MW)
cut_LEPZ = (Mh1+Mh2 > MZ)&(2*Mhp > MZ)

cut_LEPa=(Mh1>80)|(Mh2>100)|(Mh2-Mh1<8)
cut_LEPb=(Mhp>70)

cut5 = cut_LEPW&cut_LEPZ&cut_LEPa&cut_LEPb 

# ------ Diphoton and Invisible Higgs decay limits (h->AA), (h->inv)

SMBrHAA=2.28E-03  # SM Branching of Higgs decay into diphoton
RAA=BrHAA/SMBrHAA  # Diphoton parameter

cut_RAA = (RAA<1.16+0.40)&(RAA>1.16-0.36) 
cut_invH = (Brh1 + Brh2 < 0.28)

cut6 = cut_RAA & cut_invH

######################################
#Experimantal Dark Matter constraints#
######################################

#------- Relic Density limits (PLANCK experiment)
cut7=(omega<0.1196)
cut10=cut1&(omega>0.1172)

# Direct Detection limits (LUX experiment)
R_ome = omega/0.112  #Re-scale of Omega
Psi_hat = R_ome*prot

cut8=(Psi_hat<XEN)



