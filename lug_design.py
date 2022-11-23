import numpy as np

P = 1442.3/2 # N
R = 1111.3/2 # N
theta = np.radians(51.3)
P_ax = P*np.cos(theta)+R*np.cos(np.pi/2-theta) # N
P_tr = P*np.sin(theta)+R*np.sin(np.pi/2-theta) # N
print('P_ax = '+str(P_ax)+' P_tr = '+str(P_tr))

### INPUTS ###

#Dimensions INPUT
D_1 = 15 /1000 # mm
h = 16.25 / 1000# mm 
w = 20 /1000 # mm design parameter
t_1 = 5 /1000 # mm design parameter

# Material Properties INPUT
UTS_l = 439*10**6 # Pa Ultimate Tensile strength
YS_l = 393*10**6 # Pa Yield Strength
SS_l = 290*10**6 # Pa Shear Strength

# Stress Concentration Factors
K_t = 1 # Net section 
K_bry = 0.2 # Sgeart Out-bearing
K_ty = 0.32 # Transverse 

# 
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

#Net Section Tension
A_t = (w-D_1)*t_1
P_u = K_t*UTS_l*A_t
print(f'{P_u = }')

#Shear Out-bearing
A_br = (w-D_1)*t_1
P_bry = K_bry*UTS_l*A_br
print(f'{P_bry = }')

#Transverse Loading
A_brt = D_1*t_1
A_1 = (w-D_1*np.cos(np.pi/4))/2*t_1
A_2 = (w-D_1)/2*t_1
A_3 = (w-D_1)/2*t_1  
A_4 = (w-D_1*np.cos(np.pi/4))/2*t_1
A_av = 6/(3/A_1+1/A_2+1/A_3+1/A_4)
print(A_av)

P_ty = K_ty*A_brt*YS_l

#Factor of Safity
R_a = P_ax/min(P_u,P_bry)
print(f'{R_a = }')
R_tr = P_tr/P_ty
print(f'{R_tr = }')
MS = 1/(R_a**1.6+R_tr**1.6)**0.625-1
print(f'{MS = }')