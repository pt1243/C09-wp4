import numpy as np

# Forces Location Lug
Fx = 989    #N
Fy = 989    #N
Fz = -2250  #N
Mx = 742    #Nm
My = 1122   #Nm
Mz = 5.87   #Nm

hz = 1819/1000  #m
h = 16.25/1000  #m

F1 = Mx / hz
F2 = My / hz

Sum_Fx = (Fx / 2) + F2  #maximum force in x direction on 1 of the lugs
Sum_Fy = (Fy / 2) + F1
Sum_Fz = (Fz / 2)

P = np.sqrt(((Sum_Fy) ** 2) + ((Sum_Fz) ** 2))
theta = np.arctan(abs(Sum_Fz / Sum_Fy)) * 180 / np.pi
print(Sum_Fy, Sum_Fz)

print("The magnitude of the P force on each lug = %.1f [N], "
      "and the angle theta CCW from the y-axis = %.1f [rad]." % (P, theta))
print("The force on each lug in the x-direction = %.1f [N]." %Sum_Fx)
