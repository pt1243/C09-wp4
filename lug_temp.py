import numpy as np

# Radiation values
J_s_hot = 14000         # [W/m^2] solar radiation
J_a_hot = 1040          # [W/m^2] albedo flux
J_p_hot = 8217          # [W/m^2] planetary radiation
J_s_cold = 0            # [W/m^2] solar radiation
J_a_cold = 0            # [W/m^2] albedo flux
J_p_cold = 7348         # [W/m^2] planetary radiation

# Dimensions
t_arm = 16.25 / 1000    # [m] arm thickness
h = t_arm
t_1 = ...
D_2 = ...
e_2 = ...
R = t_1
e = ...
W = 2 * e
t_2 = ...
h_1 = 2 * e
alpha = 1
epsilon = 1

# Constants
sigma =  5.670374419 * 10 ** -8 # [W/m^2 K^4]


L = h + 4 * t_1 + 2 * D_2 + 4 * e_2
bend_area = (1 - np.pi / 4) * R ** 2
side_area = W * t_2 + e * W + 1/2 * np.pi * e ** 2
top_area = L * W - 4*np.pi*D_2**2

front_area = L * t_2 + 2 * t_1 * h_1 + 2 * bend_area
emission_area = 2 * front_area + 2 * side_area + top_area
conduction_area = top_area

# Hot case
Q_absorbed_hot = front_area * alpha * (J_s_hot + J_a_hot + J_p_hot)
T_hot = (Q_absorbed_hot / (emission_area * sigma * epsilon)) ** (1 / 4)
print(f'{T_hot = }')

# Cold case
Q_absorbed_cold = front_area * alpha * (J_s_cold + J_a_cold + J_p_cold)
T_cold = (Q_absorbed_cold / (emission_area * sigma * epsilon)) ** (1 / 4)
print(f'{T_cold = }')
