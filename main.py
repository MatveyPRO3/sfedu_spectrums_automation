import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

import spectrometer_api as spec_api

from datetime import datetime as dt
from os import makedirs

save_spectrums = False

makedirs("output",exist_ok=True)

def absorption_spectrum_processing(x, point_1,point_2,point_3):
    # return np.log10((x-point_1-point_3) / (point_2-point_1-point_3)) * (-1)  
    try:
        return np.log10((x-point_3) / (point_2-point_3)) * (-1)  
    except ZeroDivisionError:
        return 0
absorption_spectrum_processing = np.vectorize(absorption_spectrum_processing)

def save_spectrums_to_file(intensities):
    np.savetxt(f"output\\{dt.now()}_spectrum.csv".replace(":","_"), np.column_stack((wave_lengths, intensities)), delimiter=",")

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
    if save_spectrums:
        save_spectrums_to_file(data)
    ax.clear()  # Clear the current axes
    ax.plot(wave_lengths, data)  # Redraw the plot with updated data
    ax.set_ylim(-2,2)
    ax.set_xlim(400,700)

ani = FuncAnimation(fig, update, interval=1)

plt.show()
