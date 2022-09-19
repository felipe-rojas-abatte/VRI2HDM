/*====== Modules ===============
   Keys to switch on 
   various modules of micrOMEGAs  
================================*/
      
#define OMEGA            
  /* Calculate relic density and display contribution of  individual channels */

#define CDM_NUCLEON     
 /* Calculate amplitudes and cross-sections for  CDM-mucleon collisions */  

/*===== end of Modules  ======*/

/*===== Options ========*/
#define CLEAN
/*===== End of DEFINE  settings ===== */


#include"../include/micromegas.h"
#include"../include/micromegas_aux.h"
#include"lib/pmodel.h"
#include <time.h>
#include <math.h>

/*******START***********************/
int main(int argc,char** argv)
{  int err;
   char cdmName[10];
   int spin2, charge3,cdim;
   
  ForceUG=1;  /* Para trabajar en el gauge unitario usar 1 */

  VZdecay=1; VWdecay=1;  

 int npoints=100000,i;  /*Numero de puntos*/
 int seed = time(NULL);
 srand(seed);
 printf("seed= %i \n",seed); 

/* Creo un archivo donde guardo los tados */
 FILE *f1 = fopen("/home/felipe/Documents/Programas/micromegas_4.3.1f/VRI2HDM_new/random_scan.dat","w");
 
fprintf(f1,"%s %s %s %s %s %s %s %s %s %s %s %s %s %s \n", " Mh1   ", "   Mh2   ", "    Mhc   ","   MR   ","    ld345     ","    ld   ", "    a    ", "   Omega   ", "   protonSI  ", "  Br(H->h1h1) ", "  Br(H->h2h2) ", "   Br(H->h-h+) ","  Br(H->AA)    ","  Width_H  ");
 
double Mh1, Mh2, Mhc, MR, ld345, ld, a, massh1, massh2, masshc, LD345, LD, MRO, A, protonSI, OME, lamS, md2, vv, R, massW, massZ;

double ld1,ld2,ld3,ld4,ld5,LD3,LD4,LD5,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,deltaM;
 
 int N,pert,unit;
 N=0;
 float PI = 3.14159265359;
 
 /* Aquí determino los límites del espacio de parámetros */
 double massh1_min=450,        massh1_max=4500;
 double massh2_min=450,        massh2_max=4500;
 double masshc_min=450,        masshc_max=4500;
 double ld345_min=-2,         ld345_max=5;
 double ld_min=0,            ld_max=5;
 double MR_min= 2400,         MR_max=4500;
 double a_min= 3,	      a_max= 5;

  if(argc==1)
  { 
      printf(" Correct usage:  ./main  <file with parameters> \n");
      printf("Example: ./main data1.par\n");
      exit(1);
  }
                               
  err=readVar(argv[1]);
  
  if(err==-1)     {printf("Can not open the file\n"); exit(1);}
  else if(err>0)  { printf("Wrong file contents at line %d\n",err);exit(1);}
           
/* Aquí comienza el loop principal */

while(N <= npoints-1){

/*for (i = 1; i <= npoints; i++) {*/
  
  massh1     = massh1_min+(double) random()/RAND_MAX*(massh1_max-massh1_min);
  massh2     = massh2_min+(double) random()/RAND_MAX*(massh2_max-massh2_min);
  masshc     = masshc_min+(double) random()/RAND_MAX*(masshc_max-masshc_min);
  LD345      = ld345_min+(double) random()/RAND_MAX*(ld345_max-ld345_min);
  LD         = ld_min+(double) random()/RAND_MAX*(ld_max-ld_min);
  MRO        = MR_min+(double) random()/RAND_MAX*(MR_max-MR_min); 
  A          = a_min+(double) random()/RAND_MAX*(a_max-a_min); 

  /**********************************************/

/* Aquí asigna los valores aleatorios a las variables del modelo */

   if( massh1<massh2 && massh1<masshc )
   {			assignValW("Mh1",massh1);
			assignValW("Mh2",massh2);
			assignValW("Mhc",masshc);
			assignValW("ld345",LD345);
			assignValW("ld",LD);      
			assignValW("MR",MRO);      
			assignValW("a",A); 

  /* Esta funcion hace que se recalculen las variables dependientes del modelo en funcion de los nuevos valores adquiridos por las variables independientes */			
  			err=sortOddParticles(cdmName); }
   
   else{
     /* printf("Mass Dark Matter bigger than other 2 odd mass\n");*/ continue;
      			}

   if(err) { printf("Can't calculate %s\n",cdmName); continue;}

/* Extrae las variables del modelo */
    			
    			findVal("Mh1",&Mh1);
			findVal("Mh2",&Mh2);
			findVal("Mhc",&Mhc);
			findVal("ld345",&ld345);
			findVal("ld",&ld);
			findVal("MR",&MR);
			findVal("a",&a);
			findVal("vv",&vv);
			findVal("lam",&lamS);
			findVal("MZ",&massZ);
			findVal("MW",&massW);
			findVal("ld3",&ld3);
			findVal("ld4",&ld4);
			findVal("ld5",&ld5);
			ld1 = lamS;
			ld2 = ld;

/******  Agregamos restricciones teóricas para maximizar numero de puntos aceptados *******/
e1=ld3+ld4;
e2=ld3-ld4;
e3=ld3+ld5;
e4=ld3-ld5;
e5=ld3+2*ld4+3*ld5;
e6=ld3+2*ld4-3*ld5;
e7=-ld1-ld2+sqrt((ld1-ld2)*(ld1-ld2)+ld4*ld4);
e8=-ld1-ld2-sqrt((ld1-ld2)*(ld1-ld2)+ld4*ld4);
e9= -3*ld1-3*ld2+sqrt(9*(ld1-ld2)*(ld1-ld2)+(2*ld3+ld4)*(2*ld3+ld4));
e10=-3*ld1-3*ld2-sqrt(9*(ld1-ld2)*(ld1-ld2)+(2*ld3+ld4)*(2*ld3+ld4));
e11=-ld1-ld2+sqrt((ld1-ld2)*(ld1-ld2)+ld5*ld5);
e12=-ld1-ld2-sqrt((ld1-ld2)*(ld1-ld2)+ld5*ld5);

if(abs(ld1)<8*PI && abs(ld2)<8*PI && abs(ld3)<8*PI && abs(ld4)<8*PI && abs(ld5)<8*PI){pert = 1;}
  else{pert = 0;}

if(abs(e1)<8*PI && abs(e2)<8*PI && abs(e3)<8*PI && abs(e4)<8*PI && abs(e5)<8*PI && abs(e6)<8*PI && abs(e7)<8*PI && abs(e8)<8*PI && abs(e9)<8*PI && abs(e10)<8*PI && abs(e11)<8*PI && abs(e12)<8*PI){unit = 1;}
  else{unit = 0;}

if(pert == 1 && unit == 1){
   N = N+1;
   printf("N=%i check point \n",N);


/* Calculo de los Branching ratios del Higgs */
txtList braH;
 double BraHh1, BraHh2, BraHhc, BraHRO, BraHRc, WH, BraHAA;

/*Mass and width decay of neutral higgs*/
   WH = pWidth("H",&braH);

/*Branching ratios of Neutral higgs without Standard Model equivalents */
  BraHh1 = findBr(braH,"~h1,~h1");
  BraHh2 = findBr(braH,"~h2,~h2");
  BraHhc = findBr(braH,"~h+,~h-");
  BraHRO = findBr(braH,"RO,RO");
  BraHRc = findBr(braH,"R+,R-");  
  BraHAA = findBr(braH,"A,A");
 
/* Calcula la cantidad de materia oscura en el universo */

#ifdef OMEGA
{ int fast=1;
  double Beps=1.E-4, cut=0.01;
  double Omega;  
  int i,err; 
  /*printf("\n==== Calculation of relic density =====\n");   */

  if(CDM1 && CDM2) 
  {
    Omega= darkOmega2(fast,Beps);
 
    printf("Omega_1h^2=%.2E\n", Omega*(1-fracCDM2));
    printf("Omega_2h^2=%.2E\n", Omega*fracCDM2);
  } else
  {  double Xf;
     Omega=darkOmega(&Xf,fast,Beps);
    /* printf("Xf=%.2e Omega=%.2e\n",Xf,Omega);*/
    /* printf("Omega=%.2e\n",Omega);*/
  /*   if(Omega>0)printChannels(Xf,cut,Beps,1,stdout);*/
  }
OME = Omega;
}

#endif

/*if(OME < 0.1196 && OME > 0.1172){
 N = N+1;
   printf("N=%i check point \n",N);*/


/* Calcula la seccion eficaz de interaccion de materia oscura con materia barionica */

#ifdef CDM_NUCLEON
{ double pA0[2],pA5[2],nA0[2],nA5[2];
  double Nmass=0.939; /*nucleon mass*/
  double SCcoeff;        

/*printf("\n==== Calculation of CDM-nucleons amplitudes  =====\n");   */

  if(CDM1)
  {  
    nucleonAmplitudes(CDM1, pA0,pA5,nA0,nA5);
   /* printf("CDM[antiCDM]-nucleon micrOMEGAs amplitudes for %s \n",CDM1);
    printf("proton:  SI  %.3E [%.3E]  SD  %.3E [%.3E]\n",pA0[0], pA0[1],  pA5[0], pA5[1] );
    printf("neutron: SI  %.3E [%.3E]  SD  %.3E [%.3E]\n",nA0[0], nA0[1],  nA5[0], nA5[1] ); */

  SCcoeff=4/M_PI*3.8937966E8*pow(Nmass*Mcdm/(Nmass+ Mcdm),2.);
 /*   printf("CDM[antiCDM]-nucleon cross sections[pb]:\n");
    printf(" proton  SI %.3E [%.3E] SD %.3E [%.3E]\n",
       SCcoeff*pA0[0]*pA0[0],SCcoeff*pA0[1]*pA0[1],3*SCcoeff*pA5[0]*pA5[0],3*SCcoeff*pA5[1]*pA5[1]);
  /*  printf(" neutron SI %.3E [%.3E] SD %.3E [%.3E]\n",
       SCcoeff*nA0[0]*nA0[0],SCcoeff*nA0[1]*nA0[1],3*SCcoeff*nA5[0]*nA5[0],3*SCcoeff*nA5[1]*nA5[1]);*/
  }
  if(CDM2)
  {
    nucleonAmplitudes(CDM2, pA0,pA5,nA0,nA5);
  /*  printf("CDM[antiCDM]-nucleon micrOMEGAs amplitudes for %s \n",CDM2);
    printf("proton:  SI  %.3E [%.3E]  SD  %.3E [%.3E]\n",pA0[0], pA0[1],  pA5[0], pA5[1] );
    printf("neutron: SI  %.3E [%.3E]  SD  %.3E [%.3E]\n",nA0[0], nA0[1],  nA5[0], nA5[1] ); */

  SCcoeff=4/M_PI*3.8937966E8*pow(Nmass*Mcdm/(Nmass+ Mcdm),2.);
 /*   printf("CDM[antiCDM]-nucleon cross sections[pb]:\n");
    printf(" proton  SI %.3E [%.3E] SD %.3E [%.3E]\n",
       SCcoeff*pA0[0]*pA0[0],SCcoeff*pA0[1]*pA0[1],3*SCcoeff*pA5[0]*pA5[0],3*SCcoeff*pA5[1]*pA5[1]); 
     printf(" neutron SI %.3E [%.3E] SD %.3E [%.3E]\n",
       SCcoeff*nA0[0]*nA0[0],SCcoeff*nA0[1]*nA0[1],3*SCcoeff*nA5[0]*nA5[0],3*SCcoeff*nA5[1]*nA5[1]);*/
  } 
protonSI= SCcoeff*pA0[0]*pA0[0];    
}
#endif
  

/* Guarda los datos obtenidos por micromegas en el archivo random_scan.dat */
fprintf(f1,"%.2f   %.2f   %.2f   %.2f   %.3E   %.3E   %.2f     %.3E      %.3E     %.3E      %.3E       %.3E      %.3E      %.3E  \n", Mh1, Mh2, Mhc, MR, ld345, ld, a, OME, protonSI, BraHh1, BraHh2, BraHhc, BraHAA, WH);

/* Aquí termina el loop principal */
  }}

  killPlots();
  return 0;
}
