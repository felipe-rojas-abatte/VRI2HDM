      program separa
      implicit none
      real*8 masa, sigma
      integer i,a

      open(unit=10,file='mydata.dat',status='unknown')
      open(unit=11,file='light_a3.dat',status='unknown')
      open(unit=12,file='light_a4.dat',status='unknown')
      open(unit=13,file='light_a5.dat',status='unknown')
      
      do i=1,90
         read(10,*)a,masa,sigma
         if (a==3) then
         write(11,*)masa,sigma
      end if
      
      if (a==4) then
         write(12,*)masa,sigma
      end if

      if (a==5) then
         write(13,*)masa,sigma
      end if
      end do

      close(10)
      close(11)
      close(12)
      close(13)
      end
