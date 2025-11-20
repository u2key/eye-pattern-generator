#! /usr/bin/python3

import numpy as np
import matplotlib
matplotlib.interactive(False)
import matplotlib.pyplot as plt

def generate_simple_eye_pattern(csv_name, bit_rate_mbps, samples_per_window, sample_interval_ns, data, alpha):
  print(f"###############################")
  print(f"  Generate Simple Eye-Pattern")
  print(f"###############################")
  bit_middle_ns = samples_per_window / 2 * sample_interval_ns
  print(f"Bit Middle: {bit_middle_ns} ns")
  x = np.arange(int(samples_per_window)) * sample_interval_ns
  for channel in range(len(data[0])):
    plt.figure()
    axes = plt.axes()
    axes.set_facecolor('black')
    window_number = 0
    while True:
      samples_start_index = int(window_number * samples_per_window)
      samples_end_index   = samples_start_index + int(samples_per_window)
      if samples_end_index >= len(data):
        break
      samples = data[samples_start_index:samples_end_index, channel].flatten()
      plt.plot(x, samples, color="green", alpha=alpha)
    plt.plot([bit_middle, bit_middle], [-1.0, 4.0], color="red")
    plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))
    plt.ylim(-1.0, 4.0)
    plt.yticks([0.0, 3.3])
    plt.title(f"Plot of {bit_rate_mbps} Mbps")
    plt.xlabel("Time [ns]")
    plt.ylabel("Voltage [V]")
    plt.savefig(f"alpha{alpha}_{csv_name}_ch{channel}.jpg")
    plt.close()
