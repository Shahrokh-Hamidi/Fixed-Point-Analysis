# Created by Shahrokh Hamidi
# PhD., Electrical & Computer Engineering
# Waterloo, ON., Canada
# January 2024
# shahrokh.hamidi@uwaterloo.ca
# shahrokh.hamidi@gmail.com

import ctypes
import os
import time
import numpy as np
from ctypes import cdll
import matplotlib.pyplot as plt
import matplotlib

#%matplotlib qt


class C_Python:
        
       path = os.getcwd()
       clibrary = ctypes.CDLL(os.path.join(path, 'fixed_point_analysis.dll'))
       clibrary.quantization.restype = ctypes.POINTER(ctypes.c_int)

    
       def __init__(self):
           pass


class FIR_Filter(C_Python):

    def __init__(self):
        super().__init__()
        self.h = np.array([0.0187490466138748,	0.0489640406949407,	-0.00644746604815452,	-0.0898751011138371,	0.00697123550157515,	0.312829602738135,	0.492302903696701,	0.312829602738135,	0.00697123550157515,	-0.0898751011138371,	-0.00644746604815452,	0.0489640406949407,	0.0187490466138748])
        self.Specs()
        

    def Specs(self):
    
        
        self.input = (ctypes.c_double * len(self.h))()
        self.output = ctypes.POINTER(ctypes.c_int)
        self.init()
    



    def init(self):
        
        for i in range(len(self.h)):
            self.input[i] = self.h[i]
    


    def get_output(self):
        
        self.output = C_Python.clibrary.quantization(self.input, len(self.input), q_bit)

        return self.output





def IPR_H(h_):

    H_ = np.fft.fft(h_, nfft)
    H_ = H_/np.max(abs(H_))

    return H_





def Display(h):

    plt.stem(h, 'b')
    plt.plot(h, 'r--', lw = 2, label = 'Reference')
    plt.title('FIR Filter', fontsize = 14)
    plt.legend()
    plt.xlabel('$Samples$', fontsize = 16)
    plt.ylabel('$h[n]$', fontsize = 16)
    matplotlib.rc('font', size=16)
    matplotlib.rc('axes', titlesize = 14)
    plt.grid()
    plt.tight_layout()
    plt.show()




def Display_F(H, H_q):

    
    plt.plot(f/1e3, 20*np.log10(abs(H)), 'k', lw = 2, label = 'Reference')
    plt.plot(f/1e3, 20*np.log10(abs(H_q)), 'r--', lw = 2,  label = 'Quantized')
    plt.title(f'No. of fractional bits: {q_bit}', fontsize = 14)
    plt.legend()
    plt.xlabel('$Frequency\;\; [KHz]$', fontsize = 16)
    plt.ylabel('$|H(f)| \;\;[dB]$', fontsize = 16)
    matplotlib.rc('font', size=16)
    matplotlib.rc('axes', titlesize = 14)
    plt.grid()
    plt.tight_layout()
    plt.xlim(0, fs/1e3/2.)
    plt.show()




def Display_phase(H, H_q):

    
    plt.plot(f/1e3, np.unwrap(np.angle(H)), 'k', lw = 2, label = 'Reference')
    plt.plot(f/1e3, np.unwrap(np.angle(H_q)), 'r--', lw = 2,  label = 'Quantized')
    plt.title(f'No. of fractional bits: {q_bit}', fontsize = 14)
    plt.legend()
    plt.xlabel('$Frequency\;\; [KHz]$', fontsize = 16)
    plt.ylabel('$ \measuredangle H(f)\;\;[rad]$', fontsize = 16)
    matplotlib.rc('font', size=16)
    matplotlib.rc('axes', titlesize = 14)
    plt.grid()
    plt.tight_layout()
    plt.xlim(0, fs/1e3/2.)
    plt.show()





if __name__ == '__main__':
    
    nfft = 512
    fs = 48e3
    global  q_bit
    q_bit = 4
    
    fir_filter = FIR_Filter()
    output = fir_filter.get_output()
    
    h_q = []
    for i in range(len(fir_filter.h)):
    
        h_q.append(output[i])
    
    
    C_Python.clibrary.free_memory(output)
    
    h_q = np.array(h_q)
    
    f = np.linspace(0, fs, nfft)
    
    H = IPR_H(fir_filter.h)
    H_q = IPR_H(h_q)

    
    Display(fir_filter.h)    
    Display_F(H, H_q)
    Display_phase(H, H_q)
    
    
    
    
    
                           
