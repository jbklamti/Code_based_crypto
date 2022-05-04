import sys
import numpy as np
class operation_sur_elts_du_corps:
     def produit(self, taille, x, y, poly_primitif):
          self.ret=taille
          res1=0
          self.y1, self.x1=y, x
          while (self.y1<>0):
               if (self.y1&1)!=0:
                    res1=self.x1^res1
               self.x1=self.x1<<1
               if (self.x1&self.ret)<>0:
                    self.x1=self.x1^poly_primitif
               self.y1=self.y1>>1
          return res1
     def puissance(self, taille, x, n, poly_primitif):
          self.n1=n
          r2=operation_sur_elts_du_corps()
          r1=1
          while self.n1<>0:
               r1=r2.produit(taille, r1, x, poly_primitif)
               self.n1=self.n1-1
          return r1
     def inverse(self, taille, x, poly_primitif):
          if x==0:
               raise TypeError("Veuillez saisir un element non car l'element nul\ n'a pas d'inverse ")
          res, self.x1=1, x
          m=len(np.binary_repr(poly_primitif))-1
          i=1
          a=operation_sur_elts_du_corps()
          while i<m:
               self.x1=a.produit(taille, self.x1, self.x1, poly_primitif)
               res=a.produit(taille, self.x1, res, poly_primitif)
               i+=1
          return res
     def x_multiplie_galois(self, taille, galois, poly_primitif):
          self.res, self.ret=galois, taille
          self.res=self.res<<1
          if self.res&self.ret<>0:
               self.res=self.res^poly_primitif
          return self.res
     
