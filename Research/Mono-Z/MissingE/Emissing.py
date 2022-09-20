import ROOT
from math import sqrt, exp,pi
from random import gauss

Nbins=30
Nombre1="MR2700_a5.root"
Nombre2="back_monoz.root"
f1=ROOT.TFile(Nombre1)
f2=ROOT.TFile(Nombre2)
t1=f1.Get("h10")
t2=f2.Get("h10")
hist1=ROOT.TH1D("myhist1","Z invariant mass",Nbins,0,200)
hist2=ROOT.TH1D("myhist2"," ",Nbins,0,1500)
hist_back=ROOT.TH1D("myhist3"," ",Nbins,0,1500)

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
    
    hist2.Fill(PT)

for event in t2:
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
    if (minv2>0):
        minv=sqrt(minv2)
    else:
        minv=0
    hist1.Fill(minv)
    hist_back.Fill(PT)


integral=hist_back.Integral()
sigma=5080.4
Ntotal=10000.0
anchobin=1500.0/Nbins
hist_back.Scale(sigma/Ntotal)
hist_back.Draw()

integral=hist2.Integral()
sigma=0.005845
Ntotal=10000.0
anchobin=1500.0
escala=sigma/(Ntotal)
hist2.Scale(escala)
print hist2.Integral()
hist2.GetXaxis().SetTitle("Missing P_{T} (GeV)")
hist2.GetYaxis().SetTitle("diffrential cross section (fb/GeV)")
hist2.Draw()
hist_back.Draw("Same")


raw_input("Press Enter to Continue")  
    
