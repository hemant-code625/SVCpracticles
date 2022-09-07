#printing line graph
from matplotlib.pyplot import*
x=(1,2,3,4,5,6)
y= (51,32,34,12,25,34)
plot(x,y, marker="o",color="red",markersize=15,linewidth=5,linestyle="dotted",markerfacecolor="blue",markeredgecolor="yellow")
show()

#printing parabola graph
from matplotlib.pyplot import*
from numpy import*

x= arange(-50,50,1)
y= x**2 
plot(x,y,linewidth="1",linestyle="dotted",color="red", marker="o",markerfacecolor="blue", markeredgecolor="yellow")
show()
