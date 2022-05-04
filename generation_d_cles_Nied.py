#-*- encoding: utf-8 -*-
import sys
from determination_du_polynome_primitif import *
from operation_sur_elts_du_corps import *
from matrice_gene_d_Nie_R_et_L import *
from polynome_unitaire_irreductible import *
from operation_sur_les_poly import *
from determination_du_corps_Galois import *
def generation_d_cles_Nied(m, t):
    "m=dégré d'extension et t=dégré du polynome de Goppa"
    taille=1<<m
    x1=determination_du_polynome_primitif()
    x2=determination_du_corps_Galois()
    x3=polynome_unitaire_irreductible()
    x4=matrice_gene_d_Nie_R_et_L()
    polynome_generateur_du_corps=x1.polyprimitif(m)
    corps_galois=x2.Galois_ring(m)
    polynome_d_Goppa=x3.rand_polynome_unit_irreductible(corps_galois, m, t, polynome_generateur_du_corps)
    K=x4.matrice_dual(m, t, polynome_d_Goppa, corps_galois, polynome_generateur_du_corps)
    privk=(K[0], polynome_d_Goppa)
    pubk=(K[1], t)
    return pubk, privk