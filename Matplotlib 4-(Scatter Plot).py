# Scatter Plot...
# SYNTAX:-import matplotlib.pyplot as plt  
        # x=[],  y=[] 
        # plt.scatter(x,y)  
        # plt.show(x,y)

import matplotlib.pyplot as plt
Day=[1,2,4,6,7]
No=[3,5,2,6,8]
colors=["r","b","g","y","r"]    #for different colour
colors=[10,25,46,56,30]
size=[140,260,480,690,80]            #for different size 

plt.xlabel("Day",fontsize=15)
plt.ylabel("No",fontsize=15)
plt.title("Scatter Plot",fontsize=25)

#print(plt.scatter(Day,No,color="r"))

#alpha= for color transparency
#marker= for marker parameter
#edgecolor= for edge colour
#linewidth= for edge size
#cmap= is also used for different color

#print(plt.scatter(Day, No,c=colors,s=size,alpha=0.6,marker="*",edgecolor="green",linewidth=0.8))
print(plt.scatter(Day, No,c=colors,s=size,cmap="viridis"))
plt.colorbar()
print(plt.show())




import matplotlib.pyplot as plt
Day=[1,2,4,6,7]
No=[3,5,2,6,8]
No2=[2,3,5,8,6]
colors=[10,25,46,56,30]
sizes=[140,260,480,690,80]            #for different size 

plt.xlabel("Day",fontsize=15)
plt.ylabel("No",fontsize=15)
plt.title("Scatter Plot",fontsize=25)

print(plt.scatter(Day, No,label="No",c=colors,s=sizes,cmap="viridis"))
print(plt.scatter(Day, No2,label="No2",color="r",s=sizes))
t=plt.colorbar()
t.set_label("Color Bar",fontsize=15)
plt.legend()
print(plt.show())