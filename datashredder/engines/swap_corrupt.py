import binascii
import random
from tqdm import tqdm
def swap_corrupt(input_file,output_file):
    with open(input_file, 'rb') as f:
        content = f.read()
    file_hex = binascii.hexlify(content)

    n = 2
    split_file_hex = [file_hex[index : index + n] for index in range(0, len(file_hex), n)]

    file = ""
    

    for i, ele in enumerate(split_file_hex[:-1]):
    
        file = file+split_file_hex[i + 1].decode()
    f = open(output_file,"wb")
    f.write(binascii.unhexlify(file))