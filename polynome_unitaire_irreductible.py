#-*- encoding: utf-8 -*-
import sys
from random import *
from determination_du_corps_Galois import *
from operation_sur_elts_du_corps import *
from operation_sur_les_poly import *
class polynome_unitaire_irreductible:
#================================================================================================================
#ran_polynome_unitaire: Genère aléatoirement une polynôme un polyôme unitaire
#d= dégré du polynôme à génerer
#===============================================================================================================
     def ran_polynome_unitaire(self, G_F, d):
          if d==0:
               f=[1]
          else:
               f=[]
               s=sample(G_F, 1)[0]
               while s==0:
                    s=sample(G_F, 1)[0]
               f.append(s)
               for i in xrange(d-1):
                    f.append(sample(G_F, 1)[0])
               f.append(1)
          return f
#===============================================================================================================
#is_irreductible: teste si le polynôme est irréductible dans un corps de Galois
#taille= le nombre d'élements du corps de Galois c'est à dire 2^m ou m est le dégré d'extension
#f= le polynôme à tester
#poly_primitif= polynôme générateur du corps de Galois c'est à dire primitif
#================================================================================================================
     def is_irreductible(self, m, taille, f, poly_primitif):
           a=operation_sur_les_poly()
           d_1=a.degre_du_polynome(f)
           c=1
           h=[0,1]
           for i in xrange(0,(d_1/2)):
                 for i in xrange(m-1):
                       h=a.calcul_f_modulo_g(taille, a.produit_d_polynome(taille, h, h, poly_primitif), f, poly_primitif)
                 h_1=h
                 h_1=a.somme_d_polynome(h_1, [0, 1])
                 if a.degre_du_polynome(a.pgcd_d_deux_ploynome(taille, h_1, f, poly_primitif))<>0:
                       c=0
                       break
           if c<>0:
                 for i in xrange(taille):
                       if a.evaluation_poly_f(taille, f, i, poly_primitif)==0:
                             c=0
                             break
           return c
#======================================================================================================================
#rand_polynome_unit_irreductible: retourne un polynôme unitaire irréductible dans un corps de Galois
#taille= le nombre d'élements du corps de Galois c'est à dire 2^m ou m est le dégré d'extension
#d= dégré du polynôme
#poly_primitif= polynôme générateur du corps de Galois c'est à dire primitif
#======================================================================================================================
     def rand_polynome_unit_irreductible(self, G_F, ext, d, poly_primitif):
           taille=len(G_F)
           a=polynome_unitaire_irreductible()
           g=a.ran_polynome_unitaire(G_F, d)
           while a.is_irreductible(ext, taille, g, poly_primitif)==0:
                g=a.ran_polynome_unitaire(G_F, d)
           return g
