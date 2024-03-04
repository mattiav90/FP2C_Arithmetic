
import random
import sys
import os 







#  generate a list of random int. 
def generate_list(length, bitwidth):
    # leave one bit for the sign. 
    bitwidth=bitwidth-1
    min_value = - (2**(bitwidth)) 
    max_value =  2**(bitwidth) -1
    print("considering a signed integer of ",bitwidth+1," bits (1 for the sign). min_val= ",min_value," max_value= ",max_value)
    random_numbers = [random.randint(min_value, max_value) for _ in range(length)]
    return random_numbers


#  convert decimal to 2 complement 
def decimal_to_2s_complement(number, width):
    if number >= 0:
        return format(number, '0' + str(width) + 'b')
    else:
        # Calculate 2's complement for negative numbers
        return format((1 << width) + number, '0' + str(width) + 'b')                     # return positive value as is

# convert a list of numbers in 2 complement 
def convert_to_2s_complement(random_numbers, num_bits):
    complement_numbers = []
    for num in random_numbers:
        binary_string = decimal_to_2s_complement(num, num_bits)
        # complement_numbers.append("0b" + binary_string[2:])
        complement_numbers.append( binary_string)
    return complement_numbers

def convert_bin_to_hex(list_in, list_out):
    list_out=[]
    for i in range(len(list_in)):
        print("decimal: ",list[i]," 2comp.binary:  ",bin_list[i], " 2comp.hex: ", hex(int(bin_list[i],2)) )
        list_out.append (hex(int(bin_list[i],2)))     
    return list_out



if __name__ == "__main__":

    # Retrieve the command-line arguments
    bit_width = int(sys.argv[1])
    num_samples = int(sys.argv[2])
    file_name = sys.argv[3]

    # Get the directory of the current Python script
    script_directory = os.path.dirname(os.path.realpath(__file__))
    # Specify the file path relative to the script directory
    file_path = os.path.join(script_directory, file_name)




    list = generate_list(num_samples,bit_width)
    # convert this list into 2 complement
    bin_list = []
    bin_list = convert_to_2s_complement(list, bit_width)

    # convert bin list in hex
    hex_list = []
    hex_list= convert_bin_to_hex(bin_list,hex_list)

# Open the file in write mode
with open(file_path, 'w') as file:
    # Iterate over the values and write each value to a new line in the file
    for i in range(len(hex_list)):
        file.write(hex_list[i])
        file.write("\n")





