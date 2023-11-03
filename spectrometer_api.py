from seabreeze.spectrometers import list_devices, Spectrometer

print("Initializing spectrometer...")
print("Devices found:",list_devices())

spec = Spectrometer.from_first_available()
spec.integration_time_micros(100000)

def change_integration_time_micros(integration_time_micros):
    spec.integration_time_micros(integration_time_micros)

def measure_and_get_data() -> list:
    return {wavelength:intensity for wavelength, intensity in zip(spec.wavelengths(), spec.intensities())}