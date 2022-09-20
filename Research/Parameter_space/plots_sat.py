#size of the dots in scatter plot
dots=6
#Create the features of the colorbar
bounds=np.linspace(-7,5,13,endpoint=True)
lim_inf = np.log10(0.0000001)
lim_sup = np.log10(100)

bounds2=np.linspace(450,2500,20,endpoint=True)
lim_inf_Mh1 = 450
lim_sup_Mh1 = 2500

bounds_S=np.linspace(-0.12,0.24,11,endpoint=True)
lim_inf_S = -0.12
lim_sup_S = 0.24

bounds_T=np.linspace(-0.04,0.24,11,endpoint=True)
lim_inf_T = -0.04
lim_sup_T = 0.24

bounds_a=np.linspace(3,5,10,endpoint=True)
lim_inf_a = 3
lim_sup_a = 5

bounds_MR=np.linspace(2400,4500,20,endpoint=True)
lim_inf_MR = 2400
lim_sup_MR = 4500

#Define the quantity of colors in colorbar
cmap = plt.get_cmap('jet') 

current_dir = os.getcwd()
new_folder = current_dir+'/Systematic_cuts'+'/'+cuts

if not os.path.exists(new_folder):
    os.makedirs(new_folder)


#----------- Plot 1 Mh1-ld345-Omega-------------------------
fig, ax = plt.subplots(figsize=(6,4))
ax.scatter(Mh1[cut], ld345[cut], c='r', s=dots, edgecolor='', rasterized=True)
#Name of axes 
plt.xlabel("Mh$_1$ (GeV)", fontsize=15)
plt.ylabel("$\\lambda_{345}$", fontsize=20)
plt.xlim(min(Mh1),2130)
#plt.xscale('log')
#plt.xlim(min(Mh1),200)
plt.ylim(-1.7,1.5)
fig.tight_layout()
plt.savefig(new_folder+'/Mh1_ld345_Omega_'+cuts+'.pdf')


# ---------- Plot 2 Mh1-Mh2-Omega --------------------------
fig2, ax2 = plt.subplots(figsize=(6,4))
ax2.scatter(Mh1[cut], Mh2[cut], c='r', s=dots, edgecolor='', rasterized=True)

#Name of axes
plt.xlabel("Mh$_1$ (GeV)",fontsize=15)
plt.ylabel("Mh$_2$ (GeV)",fontsize=15)
plt.xlim(min(Mh1),max(Mh1))
plt.ylim(min(Mh2),max(Mh2))
#plt.xscale('log')
#plt.yscale('log')
fig2.tight_layout()
plt.savefig(new_folder+'/Mh1_Mh2_Omega_'+cuts+'.pdf')

# ---------- Plot 3 Mh1-Mhp-Omega --------------------------
fig3, ax3 = plt.subplots(figsize=(6,4))
cax3 = ax3.scatter(Mh1[cut], Mhp[cut], c='r', s=dots, edgecolor='', rasterized=True)

#Name of axes
plt.xlabel("Mh$_1$ (GeV)",fontsize=15)
plt.ylabel("M$_{H^{\\pm}}$ (GeV)",fontsize=15)
plt.xlim(min(Mh1),max(Mh1))
plt.ylim(min(Mhp),max(Mhp))
#plt.xscale('log')
#plt.yscale('log')
fig3.tight_layout()
plt.savefig(new_folder+'/Mh1_Mhp_Omega_'+cuts+'.pdf')

# ---------- Plot 4 Mh2-Mhp-Omega --------------------------
fig4, ax4 = plt.subplots(figsize=(6,4))
ax4.scatter(Mh2[cut], Mhp[cut], c='r', s=dots, edgecolor='', rasterized=True)

#Name of axes
plt.xlabel("Mh$_2$ (GeV)",fontsize=15)
plt.ylabel("M$_{H^{\\pm}}$ (GeV)",fontsize=15)
plt.xlim(min(Mh2),max(Mh2))
plt.ylim(min(Mhp),max(Mhp))
#plt.xscale('log')
#plt.yscale('log')
fig4.tight_layout()
plt.savefig(new_folder+'/Mh2_Mhp_Omega_'+cuts+'.pdf')


# ---------- Plot 5 Mh1-a-Omega --------------------------
fig5, ax5 = plt.subplots(figsize=(6,4))
ax5.scatter(Mh1[cut], a[cut], c='r', s=dots, edgecolor='', rasterized=True)

#Name of axes
plt.xlabel("Mh$_1$ (GeV)",fontsize=15)
plt.ylabel("$a$ ",fontsize=15)
plt.xlim(min(Mh1),max(Mh1))
plt.ylim(min(a),max(a))
#plt.xscale('log')
fig5.tight_layout()
plt.savefig(new_folder+'/Mh1_a_Omega_'+cuts+'.pdf')


# ---------- Plot 6 Mh2-a-Omega --------------------------
fig6, ax6 = plt.subplots(figsize=(6,4))
cax6 = ax6.scatter(Mh2[cut], a[cut], c='r', s=dots, edgecolor='', rasterized=True)

#Name of axes
plt.xlabel("Mh$_2$ (GeV)",fontsize=15)
plt.ylabel("$a$ ",fontsize=15)
plt.xlim(min(Mh2),max(Mh2))
plt.ylim(min(a),max(a))
#plt.xscale('log')
fig6.tight_layout()
plt.savefig(new_folder+'/Mh2_a_Omega_'+cuts+'.pdf')


# ---------- Plot 7 RAA-Mhp-Omega --------------------------
fig7, ax7 = plt.subplots(figsize=(6,4))
ax7.scatter(Mhp[cut], RAA[cut], c='r', s=dots, edgecolor='', rasterized=True)

#Name of axes
plt.xlabel("M$_{H^{\\pm}}$ (GeV)",fontsize=15)
plt.ylabel("$\\mu_{\\gamma \\gamma}$ ",fontsize=15)
plt.xlim(min(Mhp),max(Mhp))
plt.ylim(0.2,1.8)
#plt.xscale('log')
fig7.tight_layout()
plt.savefig(new_folder+'/RAA_Mhp_Omega_'+cuts+'.pdf')


# ---------- Plot 8 Mh1-MR-Omega --------------------------
fig8, ax8 = plt.subplots(figsize=(6,4))
ax8.scatter(Mh1[cut], MR[cut], c='r', s=dots, edgecolor='', rasterized=True)

#Name of axes
plt.xlabel("Mh$_1$ (GeV)",fontsize=15)
plt.ylabel("$MR$ ",fontsize=15)
plt.xlim(min(Mh1),max(Mh1))
plt.ylim(min(MR),max(MR))
#plt.xscale('log')
fig8.tight_layout()
plt.savefig(new_folder+'/Mh1_MR_Omega_'+cuts+'.pdf')


#----------- Plot 9 ld345-ld-Mh1-------------------------
fig9, ax9 = plt.subplots(figsize=(6,4))
cax9 = ax9.scatter(ld345[cut], ld[cut], c=Mh1[cut], cmap=cmap, vmin=lim_inf_Mh1, vmax=lim_sup_Mh1, s=dots, edgecolor='', rasterized=True)
cbar9 = fig9.colorbar(cax9,ticks=bounds2, format="$%.d$")
cbar9.set_label('Mh$_1$ (GeV)', rotation=90, fontsize=15)

#Name of axes 
plt.xlabel("$\\lambda_{345}$", fontsize=15)
plt.ylabel("$\\lambda_2$", fontsize=15)
plt.xlim(-2,2)
plt.ylim(0,4.5)
fig9.tight_layout()
plt.savefig(new_folder+'/ld345_ld_Mh1_'+cuts+'.pdf')

#----------- Plot 10 Mh2-Mhc-S-------------------------
fig10, ax10 = plt.subplots(figsize=(6,4))
cax10 = ax10.scatter(Mh2[cut], Mhp[cut], c=Sn[cut], cmap=cmap, vmin=lim_inf_S, vmax=lim_sup_S, s=dots, edgecolor='', rasterized=True)
cbar10 = fig10.colorbar(cax10,ticks=bounds_S, format="$%.2f$")
cbar10.set_label('S', rotation=90, fontsize=15)

#Name of axes 
plt.xlabel("Mh$_2$ (GeV)", fontsize=15)
plt.ylabel("M$_{H^{\\pm}}$ (GeV)", fontsize=15)
plt.xlim(min(Mh2),max(Mh2))
plt.ylim(min(Mhp),max(Mhp))
#plt.xscale('log')
#plt.yscale('log')
fig10.tight_layout()
plt.savefig(new_folder+'/Mh2_Mhc_S_'+cuts+'.pdf')

#----------- Plot 11 Mh2-Mhc-T-------------------------
fig11, ax11 = plt.subplots(figsize=(6,4))
cax11 = ax11.scatter(Mh2[cut], Mhp[cut], c=Tn[cut], cmap=cmap, vmin=lim_inf_T, vmax=lim_sup_T, s=dots, edgecolor='', rasterized=True)
cbar11 = fig11.colorbar(cax11,ticks=bounds_T, format="$%.2f$")
cbar11.set_label('T', rotation=90, fontsize=15)

#Name of axes 
plt.xlabel("Mh$_2$ (GeV)", fontsize=15)
plt.ylabel("M$_{H^{\\pm}}$ (GeV)", fontsize=15)
plt.xlim(min(Mh2),max(Mh2))
plt.ylim(min(Mhp),max(Mhp))
#plt.xscale('log')
#plt.yscale('log')
fig11.tight_layout()
plt.savefig(new_folder+'/Mh2_Mhc_T_'+cuts+'.pdf')

#----------- Plot 12 Mh1-ld345-a-------------------------
fig12, ax12 = plt.subplots(figsize=(6,4))
cax12 = ax12.scatter(Mh1[cut], ld345[cut], c=a[cut], cmap=cmap, vmin=lim_inf_a, vmax=lim_sup_a, s=dots, edgecolor='', rasterized=True)
cbar12 = fig12.colorbar(cax12,ticks=bounds_a, format="$%.2f$")
cbar12.set_label('$a$', rotation=90, fontsize=15)

#Name of axes 
plt.xlabel("Mh$_1$ (GeV)", fontsize=15)
plt.ylabel("$\\lambda_{345}$", fontsize=20)
plt.xlim(min(Mh1),2500)
#plt.xscale('log')
#plt.xlim(min(Mh1),)
plt.ylim(-1.7,1.5)
fig12.tight_layout()
plt.savefig(new_folder+'/Mh1_ld345_a_'+cuts+'.pdf')

#----------- Plot 13 Mh1-ld345-MR-------------------------
fig13, ax13 = plt.subplots(figsize=(6,4))
cax13 = ax13.scatter(Mh1[cut], ld345[cut], c=MR[cut], cmap=cmap, vmin=lim_inf_MR, vmax=lim_sup_MR, s=dots, edgecolor='', rasterized=True)
cbar13 = fig13.colorbar(cax13,ticks=bounds_MR, format="$%.d$")
cbar13.set_label('MR (GeV)', rotation=90, fontsize=15)

#Name of axes 
plt.xlabel("Mh$_1$ (GeV)", fontsize=15)
plt.ylabel("$\\lambda_{345}$", fontsize=20)
plt.xlim(min(Mh1),2500)
#plt.xscale('log')
#plt.xlim(min(Mh1),200)
plt.ylim(-1.7,1.5)
fig13.tight_layout()
plt.savefig(new_folder+'/Mh1_ld345_MR_'+cuts+'.pdf')

plt.close('all')




