#-*- encoding: utf-8 -*-
from random import*
from copy import*
from math import*
import numpy as np
#========================================================================================
def factorial(a):
    if a==0 or a==1:
        r=1
        s=1
    elif a%2==0:
        x=a/2
        r, s=x, 1
        for i in xrange(1, x):
            s=s*i
            r=r*(x+i)
        r=r*a
    else:
        x=(a+1)/2
        r, s=x, 1
        for i in xrange(1, x):
            s=s*i
            r=r*(x+i)
    y=r*s
    return s*r
#==========Definition de la fonction combinaison qui fait le calcul combinatoire =========
def combinaison(a, b):
    "Veuillez saisir des entiers naturel svp"
    nCk= lambda n1,k1: factorial(n1)/(factorial(k1)*factorial(n1-k1))
    if b>a:
        x=0
    else:
        x=nCk(a, b)
    return x
#==========Definition de la fonction inerse_bin qui calcul l'inverse binomial=============
def inverse_bin(x, j):
    i=0
    while ((combinaison(i, j)>x) or (combinaison((i+1), j)<=x)):
        i+=1
    return i
#===============la fonction_erreur une entree en une erreure de poids t===================
def fonction_erreur(x, a, b):
    "Genere une erreur de poids b de long a"
    e=[str(0) for i in xrange(a)]
    if x>=combinaison(a, b):
        raise TypeError('Veuillez saisr x telque x<aCb')
    if 0<= x <combinaison(a, b):
        j=b
        while j>0:
            y=inverse_bin(x, j)
            x=x-combinaison(y, j)
            e[y]=str(1)
            j=j-1
        e.reverse()
        e="".join(e)
        return int(e, 2)# int(e, 2) convertit e de base 2 en base 10
#=========================================================================================
def Nie_encryp(mess, A):
    "mess de taille k+l avec l< combinaison(2^m, te)"
    R=A[0]
    te=A[1]
    (k, t_m)=np.shape(R)
    n=k+t_m
    er=fonction_erreur(int(mess, 2), n, te)
    mes=np.binary_repr(er)
    e_1=mes[:k]
    e_2=mes[k:]
    z=[int(j) for j in e_1]
    c=np.dot(np.transpose(R), np.transpose(z))
    c=[str(j%2) for j in c]
    c="".join(c)
    c=np.binary_repr(int(c, 2)^int(e_2, 2))
    return c