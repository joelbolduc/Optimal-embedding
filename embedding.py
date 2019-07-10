# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 03:47:22 2019

@author: Joel
"""

import cmath
import random
from numpy import linalg
from sklearn.decomposition import PCA
import math

#This code implements an algorithm to embed points with distances in a linear space
#It can be proven that, given an pairwise distance matrix M, there exists
#an embedding such that the pairwise distances in that embedding match the matrix
#M'=M+eps*E for any given matrix E and with eps arbitrarely small, if we define the distance
#between two points X and Y as sum((Xi-Yi)^2) and allow for complex numbers in the embedding
#Morover, if we keep only the real part of the embedding, the resulting embedding minimizes
#the difference between the pairwise matrix M' and the pairwise matrix given by the real part of
#the embedding given by the algorithm.
#Moreover, this embedding lives in n-1 dimension space, where n is the number of points.
#This embedding can be used as a strating point for a dimensionality reduction that
#starts with coordinates rather than pairwise distances.
#This minimizing embedding is given by this algorithm.

M=[[0,7,5,3,5,7],[7,0,10,8,6,2],[5,10,0,3,5,7],[3,8,3,0,5,7],[5,6,5,5,0,3],[7,2,7,7,3,0]]
for i in range(len(M)):
    for j in range(len(M)):
        M[i][j]=pow(M[i][j],2)

def initialize(M):
    #initialization of a recursive algorithm that places points one after the other.
    u=[0.0]
    v=[float(M[0][1])]
    return [u,v]

def add_point(points,M):
    #We recursively add points. Given that previously placed points already satisfy
    #their parts of M', we shall place the new point in such a way as to respect the
    #distances between this new point and the existing points.
    for i in range(len(points)):
        points[i].append(0.0)
    distances=M[len(points)][:len(points)]
    new=list([None]*len(points))
    for i in range(len(points)-1):
        a=points[i+1][i]
        x=a/2-(distances[i+1]-distances[i])/(2*a)
        new[i]=x
        for j in range(len(distances)):
            distances[j]-=pow(x-points[j][i],2)
    s=M[-1][0]
    for i in range(len(new)):
        if(new[i]==None):
            break
        s-=pow(new[i],2)
    new[-1]=cmath.sqrt(s)
    points.append(new)
    return points

def embed(M,eps=5e-17):
    #this code initializes the algorithm with two points and places the other
    #using the add_points function
    import random
    #a perturbation is added to the M matrix,
    #because if points or not linearely independant, the algorithm encounters a 
    #division by zero and croaks. This perturbation,
    #which can be made arbitrarely small, prevents the problem.
    for i in range(len(M)):
        for j in range(len(M)):
            M[i][j]+=eps*(2*random.random()-1)
    points=initialize(M)
    while(len(points)<len(M)):
        points=add_point(points,M)
    return points