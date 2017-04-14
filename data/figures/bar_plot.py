# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

a = np.loadtxt('graphene_publications.txt')
a.sort(0)

font = {'family' : 'Helvetica',
        'size'   : 12}
matplotlib.rc('font', **font)


p1 = plt.bar(a[:,0],a[:,1])
plt.ylabel('Publications')
plt.xlabel('Year')
plt.savefig('graphene_papers.eps',bbox_inches='tight')
