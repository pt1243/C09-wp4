import numpy as np

# Radiation values
J_s_hot = 14000         # [W/m^2] solar radiation
J_a_hot = 1040          # [W/m^2] albedo flux
J_p_hot = 8217          # [W/m^2] planetary radiation
J_s_cold = 0            # [W/m^2] solar radiation
J_a_cold = 0            # [W/m^2] albedo flux
J_p_cold = 7348         # [W/m^2] planetary radiation

# Geometry
t_arm = 16.25 / 1000    # [m] arm thickness
h = t_arm               # [m] axle length
t_1 = 10 / 1000
D_2 = 5 / 1000
e_2 = 20 / 1000
R = t_1
e = 40 / 1000
W = 2 * e
t_2 = 10 / 1000
h_1 = 2 * e

# Material properties
alpha_hot = 0.40
alpha_cold = 0.10
epsilon_hot = 0.07
epsilon_cold = 0.77
k_lug = 130

# Spacecraft properties
k_sc = 170
T_sc_hot = 357
T_sc_cold = 310
h_c = 1.5 * 10 ** 3
t_skin = 4 / 1000

# Constants
sigma =  5.670374419 * 10 ** -8 # [W/m^2 K^4]


L = h + 4 * t_1 + 2 * D_2 + 4 * e_2
bend_area = (1 - np.pi / 4) * R ** 2
side_area = W * t_2 + e * W + 1/2 * np.pi * e ** 2
top_area = L * W - 4*np.pi*D_2**2

side_area = L * t_2 + 2 * t_1 * h_1 + 2 * bend_area
sun_area = max(side_area, top_area)
emission_area = 2 * sun_area + 2 * side_area + top_area
conduction_area = top_area

denom = t_2 / (conduction_area * k_lug) + 1/(h_c * conduction_area) + t_skin/(k_sc * conduction_area)

hot_coefficients = [
    -sun_area * alpha_hot * (J_s_hot + J_a_hot + J_p_hot) - T_sc_hot / denom,
    1/denom,
    0,
    0,
    emission_area * sigma * epsilon_hot
]

hot_equation = np.polynomial.polynomial.Polynomial(hot_coefficients)
hot_roots = hot_equation.roots()

cold_coefficients = [
    -sun_area * alpha_cold * (J_s_cold + J_a_cold + J_p_cold) - T_sc_cold / denom,
    1/denom,
    0,
    0,
    emission_area * sigma * epsilon_cold
]

cold_equation = np.polynomial.polynomial.Polynomial(cold_coefficients)
cold_roots = cold_equation.roots()

for z in hot_roots:
    if z.imag == 0 and z.real > 0:
        lug_temp_hot = z.real
        print(f'Hot case:', lug_temp_hot, ' K')
for z in cold_roots:
    if z.imag == 0 and z.real > 0:
        lug_temp_cold = z.real
        print('Cold case:', lug_temp_cold, ' K')