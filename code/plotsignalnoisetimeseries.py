from __future__ import division
import numpy as np
import matplotlib.pylab as plt

def plotsignalnoisetimeseries(t, s, d, t1, t2, fileprefix):

    '''
    plot signal and data between t1 and t2 and save plot to .png file
    '''
    
    filename = fileprefix + '.png'
        
    # find indices for tlow, thigh
    n1 = np.where(t>=t1)[0]
    n2 = np.where(t>=t2)[0]
    
    plt.figure()
    plt.rc('text', usetex=True)
    plt.tick_params(labelsize=20)
    plt.plot(t[n1[0]:n2[0]], d[n1[0]:n2[0]], color='k')
    plt.plot(t[n1[0]:n2[0]], s[n1[0]:n2[0]], color='r')
        
    # set symmetric ylimits if both positive and negative
    axes = plt.gca()
    y1, y2 = axes.get_ylim()
    if y1<0. and y2>0.:
        ymin = -max(np.abs(y1),np.abs(y2))
        ymax =  max(np.abs(y1),np.abs(y2))
        axes.set_ylim([ymin, ymax])
    
    plt.xlabel('time (s)', size=22)
    plt.ylabel('data', size=22)
    plt.legend(['data', 'signal'])
    plt.savefig(filename, bbox_inches='tight', dpi=400)
    
    return
