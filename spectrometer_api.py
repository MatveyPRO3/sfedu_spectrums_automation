from seabreeze.spectrometers import list_devices, Spectrometer
import numpy as np

print("Initializing spectrometer...")
l_devices = list_devices()
print("Devices found:",l_devices)
if not l_devices:
    print("Spectrometer not found!")
    exit()

spec = Spectrometer.from_first_available()
spec.integration_time_micros(100000)

def change_integration_time_micros(integration_time_micros):
    spec.integration_time_micros(integration_time_micros)

def measure_and_get_data(return_2D_array_with_wave_length=False) -> list:
    # return {wavelength:intensity for wavelength, intensity in zip(spec.wavelengths(), spec.intensities())}
    if return_2D_array_with_wave_length:
        return np.column_stack((spec.wavelengths(), spec.intensities()))
    else:
        return np.array(spec.intensities())
    
def disconnect():
    spec.close()