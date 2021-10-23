"""
DataShredder - By awesomelewis2007
A simple corruption engine made in python
Github:https://github.com/awesomelewis2007/Datashredder
"""

import binascii
import random
from tqdm import tqdm

VERSION = "0.1.3"

def corrupt(input_file,output_file,chance=1000,data=b"00"):
    """### corrupts a file with a chosen corruption data
    e.g:
    31 32 44 35 36 37 38 39 30 --> 31 FF 44 35 FF 37 FF FF 30

    In this example FF is the chosen corruption data
    Args:
        input_file ([str]): [input file]
        output_file ([str]): [output file]
        chance (int, optional): [This is the chance of the next byte of data being corrupted if i set it to 2 t is 1 in 2 chance of the next byte being corrupted]. Defaults to 1000.
        data (bytes, optional): [Data used to corrupt the image e.g 2B will be changed to 20 if i set this value to 20. this MUST be set is bytes]. Defaults to b"00".
    """
    with open(input_file, 'rb') as f:
        content = f.read()
    file_hex = binascii.hexlify(content)

    n = 2
    split_file_hex = [file_hex[index : index + n] for index in range(0, len(file_hex), n)]

    file = ""
    corruption_times = 0
    
    for i in tqdm(split_file_hex):
        if random.randint(1,chance) == 1:
            i = data
            corruption_times = corruption_times + 1
        file = file+i.decode()
    f = open(output_file,"wb")
    f.write(binascii.unhexlify(file))

def random_data_corrupt(input_file,output_file,chance=1000):
    """corrupts a file with random data
    e.g:
    31 32 44 35 36 37 38 39 30 --> 31 0A 44 35 F0 37 00 FA 30

    In this example FF is the chosen corruption data
    Args:
        input_file ([str]): [input file]
        output_file ([str]): [output file]
        chance (int, optional): [This is the chance of the next byte of data being corrupted if i set it to 2 t is 1 in 2 chance of the next byte being corrupted]. Defaults to 1000.
    """
    with open(input_file, 'rb') as f:
        content = f.read()
    file_hex = binascii.hexlify(content)

    n = 2
    split_file_hex = [file_hex[index : index + n] for index in range(0, len(file_hex), n)]

    file = ""
    corruption_times = 0
    
    for i in tqdm(split_file_hex):
        if random.randint(1,chance) == 1:
            a = random.choice(["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"])
            b = random.choice(["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"])
            c = a+b
            i = c.encode()
            corruption_times = corruption_times + 1
        file = file+i.decode()
    f = open(output_file,"wb")
    f.write(binascii.unhexlify(file))

def swap_corrupt(input_file,output_file):
    """corrupts a file with swapping the next piece of data 
    e.g:
    31 32 44 35 36 37 38 39 30 --> 32 44 35 36 37 38 39 30 

    This will corrupt the entire file
    Args:
        input_file ([str]): [input file]
        output_file ([str]): [output file]
    """
    with open(input_file, 'rb') as f:
        content = f.read()
    file_hex = binascii.hexlify(content)

    n = 2
    split_file_hex = [file_hex[index : index + n] for index in range(0, len(file_hex), n)]

    file = ""
    corruption_times = 0
    

    for i, ele in enumerate(split_file_hex[:-1]):
    
        file = file+split_file_hex[i + 1].decode()
    f = open(output_file,"wb")
    f.write(binascii.unhexlify(file))
if __name__ == "__main__":
    print("Welcome to Datashredder Demo")
    print("Version:"+VERSION)
    file_in = input("Input File>")
    file_out = input("Output File>")
    chance = input("chance of corruption>")
    if chance == "":
        chance == "1000"
    chance = int(chance)
    data = input("corruption data>").encode()
    if data == "":
        data == "00"        
    corrupt(input_file=file_in,output_file=file_out,chance=chance,data=data)
    print("Done! Go have a look at your result.")