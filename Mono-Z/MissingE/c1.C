{
//=========Macro generated from canvas: c1/c1
//=========  (Thu Jul  6 09:39:58 2017) by ROOT version5.34/30
   TCanvas *c1 = new TCanvas("c1", "c1",2227,169,525,500);
   gStyle->SetOptStat(0);
   gStyle->SetOptTitle(0);
   c1->SetHighLightColor(2);
   c1->Range(-187.5,-0.02316812,1687.5,0.2085131);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetFrameBorderMode(0);
   c1->SetFrameBorderMode(0);
   
   TH1D *myhist2 = new TH1D("myhist2","Missing Transverse Energy",30,0,1500);
   myhist2->SetBinContent(1,0.0606711);
   myhist2->SetBinContent(2,0.1468264);
   myhist2->SetBinContent(3,0.161322);
   myhist2->SetBinContent(4,0.176519);
   myhist2->SetBinContent(5,0.1610882);
   myhist2->SetBinContent(6,0.1267196);
   myhist2->SetBinContent(7,0.0977284);
   myhist2->SetBinContent(8,0.0717766);
   myhist2->SetBinContent(9,0.057281);
   myhist2->SetBinContent(10,0.0398629);
   myhist2->SetBinContent(11,0.0260687);
   myhist2->SetBinContent(12,0.0149632);
   myhist2->SetBinContent(13,0.0114562);
   myhist2->SetBinContent(14,0.0075985);
   myhist2->SetBinContent(15,0.0053774);
   myhist2->SetBinContent(16,0.0019873);
   myhist2->SetBinContent(17,0.001169);
   myhist2->SetBinContent(18,0.0003507);
   myhist2->SetBinContent(19,0.0001169);
   myhist2->SetBinContent(22,0.0001169);
   myhist2->SetEntries(10000);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   myhist2->SetLineColor(ci);
   myhist2->SetLineWidth(2);
   myhist2->GetXaxis()->SetTitle("Missing P_T (GeV)");
   myhist2->GetXaxis()->SetLabelFont(42);
   myhist2->GetXaxis()->SetLabelSize(0.035);
   myhist2->GetXaxis()->SetTitleSize(0.035);
   myhist2->GetXaxis()->SetTitleFont(42);
   myhist2->GetYaxis()->SetTitle("d\\sigma/dP_{T}   (fb/GeV)");
   myhist2->GetYaxis()->SetLabelFont(42);
   myhist2->GetYaxis()->SetLabelSize(0.035);
   myhist2->GetYaxis()->SetTitleSize(0.035);
   myhist2->GetYaxis()->SetTitleOffset(1.1);
   myhist2->GetYaxis()->SetTitleFont(42);
   myhist2->GetZaxis()->SetLabelFont(42);
   myhist2->GetZaxis()->SetLabelSize(0.035);
   myhist2->GetZaxis()->SetTitleSize(0.035);
   myhist2->GetZaxis()->SetTitleFont(42);
   myhist2->Draw("");
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);
}
