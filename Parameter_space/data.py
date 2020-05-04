#Data micrOMEGAs information

current_dir = os.getcwd()
data_folder = current_dir+'/data/'

t1 = np.genfromtxt(data_folder+"random_scan_saturation.dat", dtype=float, unpack=True, skip_header=True) 
t2 = np.genfromtxt(data_folder+"random_scan.dat.gz", dtype=float, unpack=True, skip_header=True) 
t3 = np.genfromtxt(data_folder+"random_scan2.dat.gz", dtype=float, unpack=True, skip_header=True) 
t4 = np.genfromtxt(data_folder+"random_scan3.dat.gz", dtype=float, unpack=True, skip_header=True) 

#Put all the data together in one file
tc = np.hstack((t1,t2,t3,t4))

(Mh1, Mh2, Mhp, MR, ld345, ld, a, omega, prot, Brh1, Brh2 , Brhpm, BrHAA, WH) = tc

#Data with Direct Detection limits (XENON1T experiment)
(MDM_X,SIG_X)=np.genfromtxt(data_folder+"XENON1T.dat",dtype=float,unpack=True,skip_header=False) 
XEN_SIG=interp1d(MDM_X, SIG_X, kind='linear')
XEN=XEN_SIG(Mh1)


