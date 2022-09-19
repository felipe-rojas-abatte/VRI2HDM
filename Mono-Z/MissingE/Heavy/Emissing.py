import ROOT
from math import sqrt, exp,pi
from random import gauss

Nbins=30
Nombre1="MR2100_a5.root"

f1=ROOT.TFile(Nombre1)

t1=f1.Get("h10")

hist1=ROOT.TH1D("myhist1","Z invariant mass",Nbins,0,1000)
hist2=ROOT.TH1D("myhist2"," ",Nbins,0,700)

for event in t1:
    e3=event.Epup[2]
    p3x=event.Xpup[2]
    p3y=event.Ypup[2]
    p3z=event.Zpup[2]
    
    e4=event.Epup[3]
    p4x=event.Xpup[3]
    p4y=event.Ypup[3]
    p4z=event.Zpup[3]

    e5=event.Epup[4]
    p5x=event.Xpup[4]
    p5y=event.Ypup[4]
    p5z=event.Zpup[4]

    minv2=e3**2-p3x**2-p3y**2-p3z**2
    PT=sqrt((p4x+p5x)**2+(p4y+p5y)**2)
    if minv2>0 :
        minv=sqrt(minv2)
	hist1.Fill(minv)

    hist2.Fill(PT)


#hist1.Draw()

#raw_input("Press Enter to Continue")  

integral=hist2.Integral()
sigma=0.005845
Ntotal=10000.0
anchobin=1500.0
escala=1/(Ntotal)
hist2.Scale(escala)
print hist2.Integral()
hist2.GetXaxis().SetTitle("Missing E_{T} (GeV)")
hist2.GetYaxis().SetTitle("1/#sigma d#sigma/dE_{T}^{miss} (GeV^{-1})")
hist2.Draw()



raw_input("Press Enter to Continue")  
    
