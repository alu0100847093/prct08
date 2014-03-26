#! encoding: UTF-8
#! /usr/bin/python
def aproximacion_pi(fin):
 
 if fin>0 :
  suma=0
  for i in range (1,fin+1):
   x_i=float(i-0.5)/fin
   fx_i=float (4)/(1+x_i*x_i)
   suma+=fx_i
  s= suma/fin
 return s
if __name__ == "__main__":
 import sys
 if (len(sys.argv)==3):
   t1=int(sys.argv[1])
   t2=int(sys.argv[2])
   
 else: 
  print("debe introducir n (intervalos) y veces (de ejecucion)por defecto sera 6 intervalos y 6 ejecucuines") 
  t2=6
  t1=6
 l=[]
 for i in range(1,t2+1):
   t1*=i
   s=aproximacion_pi(t1)
   l=l+[s]
   print s
 print l