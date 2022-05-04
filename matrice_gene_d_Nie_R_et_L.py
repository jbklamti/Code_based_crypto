#-*- encoding: utf-8 -*-
import sys
from operation_sur_les_poly import *
from operation_sur_elts_du_corps import *
import numpy as np
import scipy as scp
from math import *
class matrice_gene_d_Nie_R_et_L:
    def matrice_dual(self, ext, t, goppa_polynome, G_F, poly_primitif):
        x1=operation_sur_elts_du_corps()
        x2=operation_sur_les_poly()
        t11=ext*t
        taille=1<<ext
        matricedual=np.zeros([t11,taille], dtype=int)
        for i in xrange(taille):
            t14=G_F[i]
            t15=''
            for j in xrange(t):
                t12=x2.evaluation_poly_f(taille, goppa_polynome, t14, poly_primitif)
                t13=x1.inverse(taille, t12, poly_primitif)
                b=x1.produit(taille, x1.puissance(taille, t14, j, poly_primitif), t13, poly_primitif)
                t15+=np.binary_repr(b, ext)
            for l in xrange(t11):
                matricedual[l,i]=int(t15[l])
        h_1=matricedual
        b1=taille-t11
        U=np.eye(t11, dtype=int)
        R_transpose=np.zeros([t11, b1], dtype=int)
        P=np.eye(taille, dtype=int)
        tmp1=np.ones([taille, 1], dtype=int)
        tmp2=np.ones([t11, 1], dtype=int)
        for i in xrange(t11):
            if h_1[i,b1+i]==0:
                for l in xrange(taille):
                    if h_1[i ,l]<>0:
                        break
                tmp1[:,0], P[:,b1+i], P[:,l]=P[:,b1+i], P[:,l], tmp1[:,0]
                tmp2[:,0], h_1[:,b1+i], h_1[:,l]=h_1[:,b1+i], h_1[:,l], tmp2[:,0]
            for k in xrange(i+1, t11):
                if h_1[k,b1+i]<>0:
                    h_1[k,:]^=h_1[i,:]
                    U[k,:]^=U[i,:]
            for k in xrange(i):
                if h_1[k,b1+i]<>0:
                    h_1[k,:]^=h_1[i,:]
                    U[k,:]^=U[i,:]
        for i in xrange(b1):
            R_transpose[:,i]=h_1[:,i]
        L=np.dot(G_F, P)
        return L, R_transpose
