import numpy as np
import matplotlib.pyplot as py #Plotting
from numpy.fft import fft, fftfreq, fftshift #Fast Fourier Transformations
from pysine import sine #sound module


def Freq(x,y):
    dx = x[1]-x[0]
    A_numpy = np.abs(fft(y))**2
    freq = fftfreq(len(y),dx) #FFT
    A = (np.real(A_numpy)[0:]) #The Amplitudes we Need
    for i in range(len(A)): #Goes through all of the A values
        if A[i] == max(A): 
            F =(abs(freq[i])) #Finds the frequency at which the amplitude is max
            sine(frequency=F,duration=3) #Plays the Frequecy as a sound
            return F #Returns the Frequency


def Wave(x,y): 
    py.plot(x,y)
    py.xlim(0,0.025) #Specifically the Mixed Frequencies
    py.xlabel('Time (s)')
    py.ylabel('Amplitude')
    py.show() #Plots the Actual Wave
    dx = x[1]-x[0]
    A_numpy = np.abs(fft(y))**2
    freq = fftfreq(len(y),dx)
    A = (np.real(A_numpy)[1:])
    py.plot(freq,np.real(A_numpy))
    py.xlabel('Frequency (Hz)')
    py.ylabel('Amplitude')
    py.xlim(0,1200) #Specifically for the Mixed Frequencies
    py.ylim(0,max(A))
    py.show() #Plots power spectrum   

def Wave2(x,y):
    py.plot(x,y)
    py.xlim(0,0.01) #Specifically for 1000Hz
    py.xlabel('Time (s)')
    py.ylabel('Amplitude')
    py.show() #Plots the Actual Wave
    dx = x[1]-x[0]
    A_numpy = np.abs(fft(y))**2
    freq = fftfreq(len(y),dx)
    A = (np.real(A_numpy)[1:])
    py.plot(freq,np.real(A_numpy))
    py.xlabel('Frequency (Hz)')
    py.ylabel('Amplitude')
    py.xlim(0,1200) #Specifically for 1000Hz
    py.ylim(0,max(A))
    py.show() #Plots the Power Spectrum  

def Frequency(file):
  a = np.loadtxt(file)
  x = a[:,0]
  y = a[:,1] #Taking Data From Oscilloscope File
  dx = x[1]-x[0] 
  A_numpy = np.abs(fft(y))**2
  freq = fftfreq(len(y),dx)  #Runs the FFT
  A = (np.real(A_numpy)[0:])
  for i in range(len(A)): #Goes through all A values
    if A[i] == max(A):
        F =(abs(freq[i])) #Finds Frequency at max A
        sine(frequency=F,duration=3) #Plays the Frequency
        return F #Returns the Frequency

def Wavefile(file):
    a = np.loadtxt(file)
    x = a[:,0]
    y = a[:,1] #Takes data from Oscilloscope File
    py.plot(x,y)
    py.xlabel('Time')
    py.ylabel('Amplitude')
    py.xlim(0,0.005) #Specifically for 1000Hz on Oscilloscope
    py.show() # Plots the Actual Wave

def deriv(s, t, G, mBH, mA, mS): #Part of the three body problem of the Black Hole
    import numpy as np
    #all of the arrays that we will be solving for
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
    
    #All of the derivatives that we will be using
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

def diffeq_solver_from_scipy(s_initial, tmin, tmax, nts, deriv, params): #Defines the odient solver
    import numpy as np
    from scipy.integrate import odeint
    t = np.linspace(tmin,tmax,nts)
    s = odeint(deriv, s_initial, t, params)
    return t,s

def winsound(): #Plays a short sound if you win
    sine(frequency=261.6256,duration=0.5)
    sine(frequency=0,duration=0.07)
    sine(frequency=261.6256,duration=0.5)
    sine(frequency=329.6276,duration=0.5)
    sine(frequency=391.9954,duration=0.75)
    sine(frequency=523.2511,duration=1)