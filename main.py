import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

import spectrometer_api as spec_api
import visualizer as vis7


def absorption_spectrum_processing(x, point_1,point_2,point_3):
    return np.log10((x-point_1-point_3) / (point_2-point_1-point_3)) * (-1)  

absorption_spectrum_processing = np.vectorize(absorption_spectrum_processing)


input("Waiting to measure darkness, press enter to capture.")
point_1 = spec_api.measure_and_get_data(return_2D_array_with_wave_length=True)
print("Dark spectrum saved.")
input("Waiting to measure reference(light), press enter to capture.")
point_2 = spec_api.measure_and_get_data()
print("Reference spectrum saved.")
input("Waiting to measure background(light off), press enter to capture")
point_3 = spec_api.measure_and_get_data()
print("Background spectrum saved.")

wave_lengths = point_1[:,0]
point_1 = point_1[:,1]

# K = background_spec - dark_spec

fig, ax = plt.subplots()

ax.set_xlim(100, 1000)
ax.set_ylim(2200, 4000)

def update(frame):
    data = spec_api.measure_and_get_data()
    data = absorption_spectrum_processing(data,point_1,point_2,point_3)
    ax.clear()  # Clear the current axes
    ax.plot(wave_lengths, data)  # Redraw the plot with updated data
    ax.set_ylim(-2.5,2.5)
    ax.set_xlim(400,700)

ani = FuncAnimation(fig, update, interval=50)

plt.show()
