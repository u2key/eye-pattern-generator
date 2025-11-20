#! /usr/bin/python3

def get_bit_value(bit_index, bits_per_data=12):
  bit_index_in_data_structure = bit_index % bits_per_data
  if bit_index_in_data_structure == 0:
    bit_value = 0
  elif bit_index_in_data_structure >= 1 and bit_index_in_data_structure <= 8:
    data = list(f"{int(bit_index / bits_per_data + 1) % 256:0>8b}")
    bit_value = int(data[8-bit_index_in_data_structure])
  elif bit_index_in_data_structure == 9:
    data = list(f"{int(bit_index / bits_per_data + 1) % 256:0>8b}")
    parity = 0
    for b in range(8):
      parity += int(data[7-b])
    bit_value = parity % 2
  else:
    bit_value = 1
  return bit_value

def get_bit_stream(step=0):
  global bit_stream, bit_stream_size, bit_index
  bit_stream = bit_stream[step:]
  for a in range(bit_index+bit_stream_size, bit_index+step+bit_stream_size):
    bit_stream.append(get_bit_value(a))
  bit_index = bit_index+step
  print(f"############################################")
  print(f"  Bit Index : {bit_index}")
  print(f"  Bit Stream: {bit_stream}")
  print(f"############################################")
  return bit_stream

def init_bit_stream(specified_bit_stream_size=15):
  global bit_stream, bit_stream_size, bit_index
  bit_stream = [get_bit_value(a) for a in range(specified_bit_stream_size)]
  bit_stream_size = specified_bit_stream_size
  bit_index = 0
