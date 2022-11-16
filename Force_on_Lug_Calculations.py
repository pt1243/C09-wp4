import numpy as np

# Forces Location Lug
Fx = 989 # N
Fy = 989 # N
Fz = -2250 # N
Mx = 742 # Nm
My = 1122 # Nm
Mz = 5.87 # Nm

hz = 1819/1000 # mm
h = 16.25 # mm
y = 1500 # mm

F1 = Mx / hz
P = np.sqrt( ((F1 + Fy) ** 2) + ((Fz) ** 2))
theta = np.arctan(Fz / (F1 + Fy))

Plug = P / 2
Plug = round(Plug, 1)
Fxlug = Fx / 2
Fxlug = round(Fxlug, 1)


print("Aligned P force and x force on each lug respectively", Plug, Fxlug)