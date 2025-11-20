#! /usr/bin/python3

import numpy as np
import matplotlib
matplotlib.interactive(False)
import matplotlib.pyplot as plt

def generate_all_channels_overlapped_eye_pattern(csv_name, bit_rate_mbps, samples_per_window, sample_interval_ns, data, alpha):
  print(f"################################################")
  print(f"  Generate All Channels Overlapped Eye-Pattern")
  print(f"################################################")
  bit_middle_ns = samples_per_window / 2 * sample_interval_ns
  print(f"Bit Middle: {bit_middle_ns} ns")
  time_ns = np.arange(int(samples_per_window)) * sample_interval_ns
  colors = ['orange', 'blue', 'green', 'white']
  plt.figure()
  axes = plt.axes()
  axes.set_facecolor('black')
  if len(colors) < len(data[0]):
    print(f"The data contain {len(data[0])} column, but {len(colors)}colors are specified")
    exit(1)
  for channel in range(len(data[0])):
    window_number = 0
    while True:
      samples_start_index = int(window_number * samples_per_window)
      samples_end_index   = samples_start_index + int(samples_per_window)
      if samples_end_index >= len(data):
        break
      samples = data[samples_start_index:samples_end_index, channel].flatten()
      plt.plot(time_ns, samples, color=colors[channel], alpha=alpha)
      window_number = window_number + 1
  plt.plot([bit_middle_ns, bit_middle_ns], [-1.0, 4.0], color="red")
  plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))
  plt.ylim(-1.0, 4.0)
  plt.yticks([0.0, 3.3])
  plt.title(f"Plot of {bit_rate_mbps} Mbps")
  plt.xlabel("Time [ns]")
  plt.ylabel("Voltage [V]")
  plt.savefig(f"alpha{alpha}_{csv_name}.jpg")
  plt.close() 
    
