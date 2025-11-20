#! /usr/bin/python3

import csv
import numpy as np

def load_data(csv_path):
  with open(f"{csv_path}", "r") as f:
    r = csv.reader(f)
    data = [v for v in r]
  if data[4][0] != "Sample Interval":
    print(f"Sample Interval Not Found")
    exit(1)
  sample_interval = np.float64(data[4][1])
  data = np.array(data[11:], dtype=np.float64)
  return (sample_interval, data)
