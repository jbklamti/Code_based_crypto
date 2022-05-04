#-*- encoding: utf-8 -*-
import sys
from operation_sur_elts_du_corps import *
from operation_sur_les_poly import *
op1=operation_sur_elts_du_corps()
op2=operation_sur_les_poly()
#=========================================================================================
#
#=========================================================================================
def dechiffrement(b, priv_k, ext_n):
    op1=operation_sur_elts_du_corps()
    op2=operation_sur_les_poly()
    poly_primitif=op2.determination_du_polynome_primitif(ext_n)
    s11=priv_k[0]
    s21=priv_k[1]
    n_1=len(s11)
    t_n_1=n_1/2
    racine_x=op2.racine_de_x_modulo_g(taille, s21, poly_primitif)
    S_x=[0]
    for i in xrange(n_1):
        a_1=op2.euclide_etendu(taille, [s11[i], 1], s21)[1]
        S_x=op2.somme_d_polynome(S_x, op2.produit_d_polynome(taille, [b[i]], a_1, poly_primitif))
    T_x=op2.euclide_etendu(S_x, s21)[1]
    h_x=op2.somme_d_polynome(T_x, [0, 1])
    ar=[op1.puissance(taille, h_x[2*i], t_n_1, poly_primitif) for i in xrange((t/2)-1)]
    tau1=[puissance(taille, h_x[2*i], t_n_1, poly_primitif) for i in xrange((t-1)/2)]
    tau2=prod_poly(ar, racine_x)
    tau_x=op2.somme_d_polynome(tau1, tau2)
    a_2=euclid_etendu(tau_x, s21)
    b_x=a_2[2]
    a_x=a_2[0]
    sigm_x=op2.somme_d_polynome(op2.produit_d_polynome(taille, a_x, a_x, poly_primitif),op2.produit_d_polynome(taille, [0, 1], op2.produit_d_polynome(taille, b_x, b_x, poly_primitif)))
    e_1=[]
    for i in xrange(n_1):
        eva_sigm_x=op2.evaluation_poly_f(sigm_x, s11[i])
        if eva_sigm_x==0:
            e_1.append[i]
    e_2=(n_1/2)*['0', '0']
    e_2.append('0')
    for i in e_1:
        e_1[i]='1'
    e_3="".join(e_2)
    m_1=int(b, 2)^int(e_3, 2)
    m_2=np.binary_repr(m_1, n_1)
    return m_2
