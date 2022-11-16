# Calculate MMOI of one solar array at the c.g.

# spacecraft properties
m_sc = 339.7 # kg
thrust = 528 # N

# solar array properties
length = 6930.9 # mm
width = 4285 # mm
thickness = 16.25 # mm
m = 100.81 / 2 # kg

# offset from the lug to the SA center of gravity
d_x = 8430.9 - length / 2 # mm
d_y = 0 # mm
d_z = 0 # mm

# covert to m
length /= 1000
width /= 1000
thickness /= 1000
d_x /= 1000
d_y /= 1000
d_z /= 1000

I_xx_G = 1/12 * m * length ** 2
I_yy_G = 1/12 * m * width ** 2
I_zz_G = 1/12 * m * (length ** 2 + width ** 2)
#print('Mass Moments of inertia about the fully deployed SA center of gravity:')
#print(f'    {I_xx_G = } kg m^-2\n    {I_yy_G = } kg m^-2\n    {I_zz_G = } kg m^-2\n')

I_xx_lug = I_xx_G + m * d_x ** 2
I_yy_lug = I_yy_G + m * d_y ** 2
I_zz_lug = I_zz_G + m * d_z ** 2
#print('Mass moments of inertia from the lug:')
#print(f'    {I_xx_lug = } kg m^-2\n    {I_yy_lug = } kg m^-2\n    {I_zz_lug = } kg m^-2\n')

# ion thrust loads
a_z = thrust / m_sc # m/s^2
F_z = m * a_z # N
M_x = F_z * d_x # N m
print('Reaction loads from chemical thrusters')
print(f'    {F_z = } N\n    {M_x = } N m')
print(a_z)
