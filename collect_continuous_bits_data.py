#! /usr/bin/python3

import numpy as np
from copy import deepcopy
from get_bit_stream import *

def collect_continuous_bits_data(max_continuous_bits_length, samples_per_window, data):
  number_of_channels = len(data[0])
  continuous_bits_data = [[[] for _ in range(number_of_channels)] for _ in range(max_continuous_bits_length)]
  samples_per_windows = [(samples_per_window * (a + 2.0)) for a in range(max_continuous_bits_length)]
  samples_index_start = [0 for _ in range(number_of_channels)]
  complete_flag = [False for _ in range(number_of_channels)]
  break_all_loop = False
  
  init_bit_stream(specified_bit_stream_size=15)
  bit_stream = get_bit_stream(step=0)

  while not break_all_loop:
    number_of_same_bits = 0
    for a in range(len(bit_stream)):
      if bit_stream[a] == bit_stream[0]:
        number_of_same_bits = number_of_same_bits + 1
      else:
        break
    print(f"########################")
    print(f"Number of Same Bits: {number_of_same_bits}")
    print(f"########################")
    if number_of_same_bits > max_continuous_bits_length:
      print(f"Number of Same bits > Max Continuous Bits Length ({number_of_same_bits} > {max_continuous_bits_length})")
      continue
    for channel in range(number_of_channels):
      if not complete_flag[channel]:
        continue
      samples_index_end = samples_index_start[channel] + int(samples_per_windows[number_of_same_bits-1])
      if samples_index_end > len(data):
        complete_flag[channel] = True;
        continue
      continuous_bits_data[number_of_same_bits-1][channel].append(data[samples_index_start[channel]:samples_index_end].flatten())
    
    number_of_complete_flag = 0
    for channel in range(number_of_channels):
      if complete_flag[channel]:
        number_of_complete_flag = number_of_complete_flag + 1
    if number_of_complete_flag == number_of_channels:
      break
    
    samples_index_start_last = deepcopy(samples_index_start)
    for channel in range(number_of_channels):
      samples_index_start[channel] = samples_index_start[channel] + int(samples_per_window / 10)
      end_of_samples_flag = False
      while True:
        samples_index_start[channel] = samples_index_start[channel] + 1
        if samples_index_start[channel] >= len(data):
          end_of_samples_flag = True
          break
        elif data[samples_index_start[channel]-1][channel] < 1.65 and data[samples_index_start[channel]][channel] >= 1.65:
          break
        elif data[samples_index_start[channel]-1][channel] >= 1.65 and data[samples_index_start[channel]][channel] < 1.65:
          break
      if end_of_samples_flag:
        continue
      number_of_same_samples_actual = samples_index_start[channel] - samples_index_start_last[channel]
      number_of_same_bits_actual = number_of_same_samples_actual / samples_per_window
      number_of_same_bits_difference = abs(number_of_same_bits_actual - number_of_same_bits)
      if number_of_same_bits_difference > 0.7:
        print(f"##########################################")
        print(f"  Channel: {channel}")
        print(f"  Number of Same Bits           : {number_of_same_bits}")
        print(f"  Number of Same Bits Actual    : {number_of_same_bits_actual}")
        print(f"  Number of Same Bits Difference: {number_of_same_bits_difference}")  
        print(f"##########################################")
    bit_stream = get_bit_stream(step=number_of_same_bits)
  return continuous_bits_data
