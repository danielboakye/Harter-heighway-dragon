# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 20:10:51 2015

@author: Group 10
"""

import numpy as np
import matplotlib.pyplot as plt 
from math import sqrt
import scitools

def Heighway_dragon(z=0, n=15):
    z = np.vstack((0,1))
    for x in range(n):
        w = z[::-1]
        z = np.vstack((((z+(z*1j))/2.),1-((w-(w*1j))/2.)))
    return z

def plotH_dragon(z=0, n=5):
    for ei in range(n):
        plt.figure()
        z = Heighway_dragon(z, ei)
        plt.plot(z.real,z.imag)
        plt.axis('equal')
        plt.title('Heighway Dragon Curve  (iteration = '+str(ei+1)+')')
        if(ei>9):
            plt.savefig("dragon_"+"9"+str(ei)+".png")
        else:    
            plt.savefig("dragon_"+str(ei)+".png")
        plt.show()
    scitools.easyviz.movie('dragon_*.png',encoder='html',output_file='Heighway_dragon.html',fps=2)
plotH_dragon()


#question 2
def twin_dragon(z=0, n=15):
    z = np.vstack((0, 1,1-1j))
    for x in range(n):
        w = z[::-1]
        z = np.vstack((((w+(w*1j))/2.),1-((z+(z*1j))/2.)))
    return z
    
def plot_twin_dragon(z=0, n=5):
    for ei in range(n): 
        z = twin_dragon(z, ei)    
        r = len(z)
        plt.figure()
        plt.plot(z.real[:r/2],z.imag[:r/2],z.real[r/2:], z.imag[r/2:])
        plt.axis('equal')
        plt.title('Twin Dragon   (iteration = '+str(ei+1)+')')
        if(ei>9):
            plt.savefig("t_dragon_"+"9"+str(ei)+".png")
        else:    
            plt.savefig("t_dragon_"+str(ei)+".png")
        plt.show()    
    scitools.easyviz.movie('t_dragon_*.png',encoder='html',output_file='twin_dragon.html',fps=2)
plot_twin_dragon()

#
#
def terdragon(z=0, n=15):
    l1= (1/2.)-(1j/(2*(sqrt(3))))
    l2= (1/2.)+(1j/(2*(sqrt(3))))
    z = np.vstack((0, 1, 1))
    for x in range(n):
        z=np.vstack(((l1*z),((z*1j)/(sqrt(3)))+l1,(l1*z)+l2))

    return z
    
def plot_terdragon(z=0, n=5):
    for ei in range(n):
        z = terdragon(z, ei)
        plt.figure()
        m = len(z)
        plt.plot(z.real[:m/3],z.imag[:m/3],z.real[m/3:2*m/3],z.imag[m/3:2*m/3],z.real[2*m/3:],z.imag[2*m/3:])
        plt.axis('equal')
        plt.title('Terdragon Curve  (iteration = '+str(ei+1)+')')
        if(ei>9):
            plt.savefig("terdragon_"+"9"+str(ei)+".png")
        else:
            plt.savefig("terdragon_"+str(ei)+".png")
        plt.show()    
    scitools.easyviz.movie('terdragon_*.png',encoder='html',output_file='terdragon.html',fps=2)
plot_terdragon()   