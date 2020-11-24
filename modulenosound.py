#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as py
from numpy.fft import fft, fftfreq, fftshift


def Freq(x,y):
    tarray = np.arange(0,1,0.0001)
    yarray = 11*np.sin(2*np.pi*tarray*1000)+12*np.sin(2*np.pi*tarray*200)
    dx = x[1]-x[0]
    A_numpy = np.abs(fft(y))**2
    freq = fftfreq(len(y),dx)
    A = (np.real(A_numpy)[0:])
    for i in range(len(A)):
        if A[i] == max(A):
            F =(abs(freq[i]))
            return F


def Wave(x,y):
    py.plot(x,y)
    py.xlim(0,0.025)
    py.xlabel('Time (s)')
    py.ylabel('Amplitude')
    py.show()
    dx = x[1]-x[0]
    A_numpy = np.abs(fft(y))**2
    freq = fftfreq(len(y),dx)
    A = (np.real(A_numpy)[1:])
    py.plot(freq,np.real(A_numpy))
    py.xlabel('Frequency (Hz)')
    py.ylabel('Amplitude')
    py.xlim(0,1200)
    py.ylim(0,max(A))
    py.show()    

def Wave2(x,y):
    py.plot(x,y)
    py.xlim(0,0.01)
    py.xlabel('Time (s)')
    py.ylabel('Amplitude')
    py.show()
    dx = x[1]-x[0]
    A_numpy = np.abs(fft(y))**2
    freq = fftfreq(len(y),dx)
    A = (np.real(A_numpy)[1:])
    py.plot(freq,np.real(A_numpy))
    py.xlabel('Frequency (Hz)')
    py.ylabel('Amplitude')
    py.xlim(0,1200)
    py.ylim(0,max(A))
    py.show()   

def Frequency(file):
  a = np.loadtxt(file)
  x = a[:,0]
  y = a[:,1]
  dx = x[1]-x[0]
  A_numpy = np.abs(fft(y))**2
  freq = fftfreq(len(y),dx)
  A = (np.real(A_numpy)[0:])
  for i in range(len(A)):
    if A[i] == max(A):
        F =(abs(freq[i]))
        return F 

def Wavefile(file):
    a = np.loadtxt(file)
    x = a[:,0]
    y = a[:,1]
    py.plot(x,y)
    py.xlabel('Time')
    py.ylabel('Amplitude')
    py.xlim(0,0.005)
    py.show()

def deriv(s, t, G, mBH, mA, mS):
    import numpy as np
    xS0 = s[0]
    vxS0 = s[1]
    yS0 = s[2]
    vyS0 = s[3]
    xBH0 = s[4]
    vxBH0 = s[5]
    yBH0 = s[6]
    vyBH0 = s[7]
    xA0 = s[8]
    vxA0 = s[9]
    yA0 = s[10]
    vyA0 = s[11]

    f1 = vxS0
    f2 = ((G*mA*(xA0-xS0))/(((xA0-xS0)**2+(yA0-yS0)**2)**(1.5))) + ((G*mBH*(xBH0-xS0))/(((xBH0-xS0)**2+(yBH0-yS0)**2)**(1.5)))
    f3 = vyS0
    f4 = ((G*mA*(yA0-yS0))/(((xA0-xS0)**2+(yA0-yS0)**2)**(1.5))) + ((G*mBH*(yBH0-yS0))/(((xBH0-xS0)**2+(yBH0-yS0)**2)**(1.5)))
    f5 = vxBH0
    f6 = ((G*mA*(xA0-xBH0))/(((xA0-xBH0)**2+(yA0-yBH0)**2)**(1.5))) + ((G*mS*(xS0-xBH0))/(((xS0-xBH0)**2+(yS0-yBH0)**2)**(1.5)))
    f7 = vyBH0
    f8 = ((G*mA*(yA0-yBH0))/(((xA0-xBH0)**2+(yA0-yBH0)**2)**(1.5))) + ((G*mS*(yS0-yBH0))/(((xS0-xBH0)**2+(yS0-yBH0)**2)**(1.5)))
    f9 = vxA0
    f10 = ((G*mS*(xS0-xA0))/(((xS0-xA0)**2+(yS0-yA0)**2)**(1.5))) + ((G*mBH*(xBH0-xA0))/(((xBH0-xA0)**2+(yBH0-yA0)**2)**(1.5)))
    f11 = vyA0
    f12 = ((G*mS*(yS0-yA0))/(((xS0-xA0)**2+(yS0-yA0)**2)**(1.5))) + ((G*mBH*(yBH0-yA0))/(((xBH0-xA0)**2+(yBH0-yA0)**2)**(1.5)))

    return [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12]

def diffeq_solver_from_scipy(s_initial, tmin, tmax, nts, deriv, params):
    import numpy as np
    from scipy.integrate import odeint
    t = np.linspace(tmin,tmax,nts)
    s = odeint(deriv, s_initial, t, params)
    return t,s

