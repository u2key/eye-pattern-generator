#! /usr/bin/python3

import numpy as np
import matplotlib
matplotlib.interactive(False)
import matplotlib.pyplot as plt

def generate_continuous_bits_eye_pattern(csv_name, bit_rate_mbps, samples_per_window, sample_interval_ns, continuous_bits_data, alpha):
  print(f"#######################################")
  print(f" Generate Continuous Bits Eye-Pattern")
  print(f"#######################################")
  maximum_number_of_continuous_bits = len(continuous_bits_data)
  ns_per_window = sample_interval_ns * samples_per_window
  samples_per_windows = [(samples_per_window * (a + 2.0)) for a in range(maximum_number_of_continuous_bits)]
  for a in range(maximum_number_of_continuous_bits):
    number_of_continuous_bits = np.float64(a + 1)
    time_ns = np.arange(samples_per_windows[a]) * sample_interval_ns
    if number_of_continuous_bits == 1:
      gauge_time_ns = np.array([ns_per_window * number_of_continuous_bits, ns_per_window * (number_of_continuous_bits + 0.5)])
      gauge_colors  = ["red", "orange"]
    else:
      gauge_time_ns = np.array([ns_per_window * (number_of_continuous_bits - 0.5), ns_per_window * number_of_continuous_bits, ns_per_window * (number_of_continuous_bits + 0.5)])
      gauge_colors  = ["orange", "red", "orange"]
    number_of_channels = len(continuous_bits_data[a])
    for channel in range(number_of_channels):
      plt.figure()
      axes = plt.axes()
      axes.set_facecolor('black')
      for b in range(len(continuous_bits_data[a][channel])):
        plt.plot(time_ns, continuous_bits_data[a][channel][b], color="green", alpha=alpha)
      for b in range(len(gauge_colors)):
        plt.plot([gauge_time_ns[b], gauge_time_ns[b]], [-1.0, 4.0], color=gauge_colors[b], alpha=1.0)
      plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))
      plt.ylim(-1.0, 4.0)
      plt.yticks([0.0, 3.3])
      plt.title(f"Plot of {bit_rate_mbps} Mbps")
      plt.xlabel("Time [ns]")
      plt.ylabel("Voltage [V]")
      plt.savefig(f"alpha{alpha}_{csv_name}_continuous{number_of_continuous_bits}_ch{channel}.jpg")
      plt.close()
