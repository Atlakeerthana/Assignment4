# -*- coding: utf-8 -*-
"""Assignment4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11kocB8mUSIgM1tw7YjxOSSkjEeT1HPsC
"""

# -*- coding: utf-8 -*-
"""Assignment4.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1U6yNvmAYwHM_coFqlCXD7tbOYQOnr-U_
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


#if using termux
import subprocess
import shlex
#end if

#creating x,y for 3D plotting
xx, yy = np.meshgrid([-4,4], range(4))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')


#defining planes:  n.T * x = c 
n1 = np.array([2,-1,3]).reshape((3,1))
A =  np.array([1,0,0]).reshape((3,1))
c1 = 1
n2 = np.array([2,-1,3]).reshape((3,1))
B =  np.array([0,0,0]).reshape((3,1))
c2= -3

#corresponding z for planes
z1 = (c1-n1[0]*xx-n1[1]*yy)/(n1[2])
z2 = (c2-n2[0]*xx-n2[1]*yy)/(n2[2])

#plotting planes
Plane1=ax.plot_surface(xx, yy, z1,label="P1", color='b',alpha=0.6)
Plane2=ax.plot_surface(xx, yy, z2,label="P2", color='g',alpha=0.6)
Plane1._facecolors2d=Plane1._facecolors3d
Plane2._facecolors2d=Plane2._facecolors3d

#show plot
plt.xlabel('$x$')
plt.ylabel('$y$')
#plt.legend(loc='best')
plt.grid() # minor

 
#if using termux
plt.savefig('figure4.png')
#else
#plt.show()