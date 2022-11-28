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
theta = np.degrees(np.arctan(abs(Sum_Fz / Sum_Fy)))

print("The magnitude of the P force on each lug = %.1f [N], "
      "and the angle theta CCW from the y-axis = %.1f [rad]." % (P, theta))
print("The force on each lug in the x-direction = %.1f [N]." %Sum_Fx)

print(Sum_Fx, Sum_Fy, Sum_Fz)


#P = 1442.3/2 # N
#R = 1111.3/2 # N
theta = np.radians(51.3)
P_ax = abs(Sum_Fy) #P*np.cos(theta)+R*np.cos(np.pi/2-theta) # N
P_tr = abs(Sum_Fz) #P*np.sin(theta)+R*np.sin(np.pi/2-theta) # N
print('P_ax = '+str(P_ax)+' P_tr = '+str(P_tr))

### Pin Design ###
#Material Properties
YS_p = 393*10**6 # Pa Yield Strength of the pin
SS_p = 290*10**6 # Pa Shear Strength of the pin
FoS = 0.5 # Factor of Safity
#Shear
D_1 = ((2*P*(1+FoS))/(SS_p*np.pi))**(1/2)*10**3 #calculating D1 from shear
#Bending
print(str(D_1) + ' mm')

### INPUTS ###

#Dimensions INPUT
D_1 = 15*10**-3 # m
h = 16.25*10**-3 # m
w = 20*10**-3 # m design parameter
t_1 = 5*10**-3 # m design parameter

# Material Properties INPUT
UTS_l = 483*10**6 # Pa Ultimate Tensile strength of the lug
YS_l = 448*10**6 # Pa Yield Strength of the lug
SS_l = 331*10**6 # Pa Shear Strength of the lug

# Stress Concentration Factors
K_t = 1 # stress concentration factor for Net Section tension
K_bry = 0.2 # stress concentration factor for Shear Out-bearing
K_ty = 0.32 # Stress concentration factor for Transverse loading failure

#Calculating the areas for the transfers loading failure
A_1 = (w-D_1*np.cos(np.pi/4))/2*t_1
A_2 = (w-D_1)/2*t_1
A_3 = (w-D_1)/2*t_1
A_4 = (w-D_1*np.cos(np.pi/4))/2*t_1
A_av = 6/(3/A_1+1/A_2+1/A_3+1/A_4)
A_brt = D_1*t_1
print('W/D_1 for K_t: '+str(w/D_1))
print('e/D_1 for K_bry: '+str(w/(2*D_1)))
print('t_1/D_1 for K_bry: '+str(t_1/D_1))
print('A_av/A_br for K_ty: '+str(A_av/A_brt))

### Lug Design ###

#Net Section Tension Failure Force Calc
A_t = (w-D_1)*t_1
P_u = K_t*YS_l*A_t


#Shear Out-bearing Failure Force Calc
A_br = (w-D_1)*t_1
P_bry = K_bry*YS_l*A_br

#Transverse Loading Failure Force Calc
A_brt = D_1*t_1
A_1 = (w-D_1*np.cos(np.pi/4))/2*t_1
A_2 = (w-D_1)/2*t_1
A_3 = (w-D_1)/2*t_1
A_4 = (w-D_1*np.cos(np.pi/4))/2*t_1
A_av = 6/(3/A_1+1/A_2+1/A_3+1/A_4)

P_ty = K_ty*A_brt*YS_l

#Factor of Safety determination
R_a = P_ax/min(P_u,P_bry)
R_tr = P_tr/P_ty
MS = 1/(R_a**1.6+R_tr**1.6)**0.625-1
print('Factor of safety: ' + str(MS))

#Bending 
F_x = abs(Sum_Fx) # N
F_z = abs(Sum_Fz) # N
print('Fz='+str(F_z))
I_zz = t_1**3*w/12
I_xx = w**3*t_1/12
L = w/2  #this assumption can be changed
sigma_max = (F_x*L)/I_zz*t_1/2+(F_z*L)/I_xx*w/2
print(YS_l/sigma_max-1)
if sigma_max >= YS_l:
  print('The lug fails in bending')
else:
  print('The lug does NOT fail')