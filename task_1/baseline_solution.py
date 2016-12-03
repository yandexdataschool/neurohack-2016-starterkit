import numpy as np
import sys

if sys.version_info.major == 2:
    input = raw_input


OFFSET = 3000

experiment_id = input()

alpha = 0.1

data_avg = 0

for i in range(OFFSET):
    cur_data = list(map(float, input().split())) 
    data_avg = alpha * data_avg + (1 - alpha) * cur_data[15]

print(data_avg)
sys.stdout.flush()

while True:
    cur_data = list(map(float, input().split()))
    data_avg = alpha * data_avg + (1 - alpha) * cur_data[15]
    print(data_avg)
    sys.stdout.flush()

   
