#! /usr/bin/python3

import csv
import sys
import numpy as np
import matplotlib
matplotlib.interactive(False)
import matplotlib.pyplot as plt
from copy import deepcopy
from load_data import *
from generate_simple_eye_pattern import *
from generate_all_channels_overlapped_eye_pattern import *

def main(alpha=1.0):
  if len(sys.argv) < 3:
    exit(1)
  
  csv_path = sys.argv[1]
  csv_name = csv_path.replace("/", "").replace(".csv", "")
  print(f"CSV Name: {csv_name}")
  bit_rate_mbps = np.float64(sys.argv[2])
  bit_rate_bps = bit_rate_mbps * 1.0e+6
  print(f"Bit Rate: {bit_rate_mbps} Mbps")
  window_interval_ns = 1.0 / bit_rate_bps * 1.0e+9
  print(f"Window Interval: {window_interval_ns} ns")
  
  (sample_interval_ns, data) = load_data(csv_path)
  samples_per_window = window_interval_ns / sample_interval_ns
  print(f"Samples/Window = {samples_per_window} [samples]")
  
  generate_simple_eye_pattern(csv_name, bit_rate_mbps, samples_per_window, sample_interval_ns, data, alpha)
  generate_all_channels_overlapped_eye_pattern(csv_name, bit_rate_mbps, samples_per_window, sample_interval_ns, data, alpha)
  
if __name__ == "__main__": 
  main()
