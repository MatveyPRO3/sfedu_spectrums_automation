import spectrometer_api as spec_api 
import visualizer as vis

print(spec_api.measure_and_get_data())
vis.build_frequency_intensities(spec_api.measure_and_get_data())