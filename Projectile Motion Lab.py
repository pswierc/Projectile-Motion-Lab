import numpy as np
import matplotlib.pyplot as plt


#%matplotlib inline
#I didn't use this, because spyder is not too fond of it and I prefer to edit my code through spyder. I will still use Jupyter as needed. 

x = np.array([50, 47, 43, 41, 38])
y = np.array([76.38, 89.7, 93.56, 87.48, 78.02])
dy = np.array([.005, .005, .005, .005, .005])

plt.figure(figsize=(15,10))

plt.scatter(x, y, color='blue', marker='o')

plt.xlabel('$\\theta$ (degrees)')
plt.ylabel('$y_{mean}$ (m)')
plt.title('Height on wall vs Launcher Angle')

c,b,a=np.polynomial.polynomial.polyfit(x,y,2,w=dy)

plt.annotate('A = {value:.{digits}E}'.format(value=a, digits=3),
             (0.05, 0.9), xycoords='axes fraction')

plt.annotate('B = {value:.{digits}E}'.format(value=b, digits=3),
             (0.05, 0.85), xycoords='axes fraction')
             
plt.annotate('C = {value:.{digits}E}'.format(value=c, digits=3),
             (0.05, 0.8), xycoords='axes fraction')

xnew = np.linspace(x.min(), x.max(), 300)
fit = a*xnew**2 + b*xnew +c

plt.scatter(xnew, fit, color='red')
plt.show()

print ("C =",c , " B =",b, " A =",a)

theta_max = -1 * (b / (2 * a))

print("Maximum Theta:", theta_max)
