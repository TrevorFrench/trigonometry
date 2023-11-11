# DEPENDENCIES
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# SETUP
plt.rcParams['font.family'] = 'Courier New'
plt.style.use('dark_background')
fig, ((sin, cos), (tan, unit)) = plt.subplots(2, 2, figsize=(10, 8))
x = np.linspace(0, 4 * np.pi, 720)

# SINE PLOT
sin_lin, = sin.plot([], [], lw=2)
sin.set_ylim(-1.5, 1.5)
sin.set_xlim(0, 4 * np.pi)
sin.set_title('sin(x)')

# COSINE PLOT
cos_lin, = cos.plot([], [], lw=2)
cos.set_ylim(-1.5, 1.5)
cos.set_xlim(0, 4 * np.pi)
cos.set_title('cos(x)')

# TANGENT PLOT
tan_lin, = tan.plot([], [], lw=2)
tan.set_ylim(-5, 5)
tan.set_xlim(0, 4 * np.pi)
tan.set_title('tan(x)')

# UNIT CIRCLE PLOT
circle, = unit.plot([], [], 'co')
unit.set_xlim(-1.5, 1.5)
unit.set_ylim(-1.5, 1.5)
unit.set_title('Unit Circle')
static_circle = plt.Circle((0, 0), 1, color='gray', fill=False)
unit.add_patch(static_circle)
unit.axhline(0, color='white', linestyle='dashed', linewidth=0.8)
unit.axvline(0, color='white', linestyle='dashed', linewidth=0.8)
quartile_markers = np.array([
    [1, 0],  # 0 degrees
    [0, 1],  # 90 degrees
    [-1, 0], # 180 degrees
    [0, -1], # 270 degrees
])
unit.scatter(quartile_markers[:, 0], quartile_markers[:, 1], c='white', marker='o', s=30)

# ASSEMBLE AND RENDER
def update(frame):
    sin_lin.set_data(x[:frame], np.sin(x[:frame]))
    cos_lin.set_data(x[:frame], np.cos(x[:frame]))
    tan_lin.set_data(x[:frame], np.tan(x[:frame]))
    angle = np.deg2rad(frame)
    circle.set_data(np.cos(angle), np.sin(angle))
    return sin_lin, cos_lin, tan_lin, circle

ani = FuncAnimation(fig, update, frames=len(x), interval=20, blit=True)
ani.save('trig_animation.gif', writer='imagemagick', fps=30)
#plt.show()
