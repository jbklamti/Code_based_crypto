#-*- encoding: utf-8 -*-
import sys
from operation_sur_elts_du_corps import *
class operation_sur_les_poly:
#===============================================================================================
#
#===============================================================================================
     def degre_du_polynome(self, f):
          self.h=f
          l=-1
          k=len(f)
          while k-1>=0 and self.h[k-1]==0:
               del self.h[k-1]
               k=k-1
          k=k-1
          return k
#===============================================================================================
#
#===============================================================================================
     def harmonisation_du_polynome(self, f):
          h1=[0]
          d=operation_sur_les_poly()
          d1=d.degre_du_polynome(f)
          if (d1+1)==len(f):
               h1=f
          if len(f)>(d1+1):
               h1=f
               del h1[d1+1:]
          return h1
#===============================================================================================
#
#===============================================================================================
     def somme_d_polynome(self, f, g):
          h1=[]
          d=operation_sur_les_poly()
          d_1, d_2=d.degre_du_polynome(f), d.degre_du_polynome(g) 
          d_3=max(d_1, d_2)
          if d_1<d_3:
               for i in xrange(d_3+1):
                    if i<=d_1:
                         h1.append(f[i]^g[i])
                    else:
                         h1.append(g[i])
          else:
               for i in xrange(d_3+1):
                    if i<=d_2:
                         h1.append(f[i]^g[i])
                    else:
                         h1.append(f[i])
          return h1
#===============================================================================================
#
#===============================================================================================
     def produit_d_polynome(self, taille, f, g, poly_primitif):
          d=operation_sur_les_poly()
          d_1, d_2=d.degre_du_polynome(f), d.degre_du_polynome(g)
          d_3=d_1+d_2
          if d_1==-1 or d_2==-1:
               h=[0]
          else:
               h=[0 for i in range(d_3+1)]
               for k in xrange(d_3+1):
                    for i in xrange(d_1+1):
                         for j in xrange(d_2+1):
                              if k==(i+j):
                                   hk=operation_sur_elts_du_corps()
                                   h[k]^=hk.produit(taille, f[i], g[j], poly_primitif)
          return h
#===============================================================================================
#
#===============================================================================================
     def calcul_f_modulo_g(self, taille, f, g, poly_primitif):
          self.h=f
          d=operation_sur_les_poly()
          d_1, d_2=d.degre_du_polynome(f), d.degre_du_polynome(g)
          if d_2==-1:
               raise TypeError('Verifier f et g telque def(f)>=deg(g) puis saisir un polynome g non nul')
          elif d_1<d_2:
               return self.h
          elif d_2==0:
               return [0]
          else:
               a=operation_sur_elts_du_corps()
               while d_1>=d_2:
                    w=d_1-d_2
                    l=[0 for i in xrange(w+1)]
                    c=g[d_2]
                    b=a.inverse(taille, c, poly_primitif)
                    l[w]=a.produit(taille, self.h[d_1], b, poly_primitif)
                    self.h=d.somme_d_polynome(self.h, d.produit_d_polynome(taille, l, g, poly_primitif))
                    d_1=d.degre_du_polynome(self.h)
               return self.h
#===============================================================================================
#
#===============================================================================================
     def pgcd_d_deux_ploynome(self,taille, f, g, poly_primitif):
          d=operation_sur_les_poly()
          if d.degre_du_polynome(f)>=d.degre_du_polynome(g):
               self.q, self.l=f, g
          else:
               self.q, self.l=g, f
          if d.degre_du_polynome(self.l)==-1:
               return self.q 
          else:
               while d.degre_du_polynome(self.l)<>-1:
                    k=d.calcul_f_modulo_g(taille, self.q, self.l, poly_primitif)
                    self.q, self.l=self.l, k
               return self.q
#===============================================================================================
#
#===============================================================================================
     def evaluation_poly_f(self, taille, f, a, poly_primitif):
          b=operation_sur_les_poly()
          xx=operation_sur_elts_du_corps()
          res, ress=0, 1
          l=b.degre_du_polynome(f)
          for i in xrange(l+1):
               if f[i]<>0:
                    aa=xx.puissance(taille, a, i, poly_primitif)
                    res^=xx.produit(taille, f[i], aa, poly_primitif)
          return res
#===============================================================================================
#
#===============================================================================================
     def racine_de_x_modulo_g(self, taille, g, poly_primitif):
          d=operation_sur_les_poly()
          tee1=d.degre_du_polynome(g)
          tee2=d.degre_du_polynome(poly_primitif)
          h=m*tee-1
          he=1<<h
          racin=he*[0,0]
          racin.append(1)
          racin=d.calcul_f_modulo_g(taille, racin, g, poly_primitif)
          return racin
#================================================================================================
#
#================================================================================================
     def division_poly_f_par_g(taille, f, g, poly_primitif):
         h=f
         d=operation_sur_les_poly()
         dd=operation_sur_elts_du_corps()
         d_1, d_2=d.degre_du_polynome(f), d.degre_du_polynome(g)
         w=d_1-d_2
         if d.degre_du_polynome(d_2)==-1:
             raise TypeError("Saisir un polynome g non nul")
         elif d_2==0:
             q=f
             h=[0]
         elif d_1<d_2:
             q=[0]
             h=f
         else:
             q=[k for k in xrange(w+1)]
             for k in xrange(w+1):
                 l[w-k]=dd.produit(taille, h[d_1], dd.inverse(taille, g[d_2], poly_primitif), poly_primitif)
                 h=d.somme_d_polynome(h, d.produit_d_polynome(l, g))
                 d_1=d.degre_du_polynome(h)
         h=d.harmonisation_du_polynome(h)
         return q, h
#=========================================================================================================
#
#========================================================================================================
     def euclide_etendu(taille, f, g, poly_primitif, t):
         'f et g sont sous forme de liste'
         d=operation_sur_les_poly()
         dd=operation_sur_elts_du_corps()
         R0=f
         R1=g
         U0, V1=[1], [1]
         U1, V0=[0], [0]
         (Q2, R2)=d.division_poly_f_par_g(taille, R0, R1, poly_primitif)
         R0=R1
         R1=R2
         U2=d.somme_d_polynome(U0, d.produit_d_polynome(taille, Q2, U1, poly_primitif))
         V2=d.somme_d_polynome(V0, d.produit_d_polynome(Q2, V1))
         U0, U1=U1, V2
         V0, V1=V1, V2
         while R2>t:
             (Q2, R2)=d.division_poly_f_par_g(taille, R0, R1, poly_primitif)
             R0=R1
             R1=R2
             U2=d.somme_d_polynome(U0, d.produit_d_polynome(taille, Q2, U1, poly_primitif))
             V2=d.somme_d_polynome(V0, d.produit_d_polynome(taille, Q2, V1, poly_primitif))
             U0, U1=U1, U2
             V0, V1=V1, V0
         return U2, V2, R1


