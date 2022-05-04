#-*- encoding: utf-8 -*-
import sys
from determination_du_polynome_primitif import *
from operation_sur_elts_du_corps import *
class determination_du_corps_Galois:
     def Galois_ring(self, extension):
          poly_primitif=determination_du_polynome_primitif()
          poly_pri=poly_primitif.polyprimitif(extension)
          L=[0]
          n=1<<extension
          L1=operation_sur_elts_du_corps()
          for i in xrange(n-1):
               L.append(L1.puissance(n, 2, i, poly_pri))
          return L
