
import random


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
def decimal_to_2s_complement(num, num_bits):
    # Convert positive numbers directly to binary
    if num >= 0:
        return bin(num)[2:].zfill(num_bits)
    # For negative numbers, compute 2's complement
    else:
        return bin(2**num_bits + num)[2:]

# convert a list of numbers in 2 complement 
def convert_to_2s_complement(random_numbers, num_bits):
    complement_numbers = []
    for num in random_numbers:
        complement_numbers.append(decimal_to_2s_complement(num, num_bits))
    return complement_numbers


if __name__ == "__main__":
    converted_list = []

    bit_width=8
    num_samples = 20
    # generate a list of values
    list = generate_list(num_samples,bit_width)
    # convert this list into 2 complement
    converted_list = convert_to_2s_complement(list, bit_width)
    for  i in range(len(list)) :
        print("decimal: ",list[i],"converted: ",converted_list[i])
    
    # Specify the file path
    file_path = "file.txt"

    # Open the file in write mode
    with open(file_path, 'w') as file:
        # Iterate over the values and write each value to a new line in the file
        for value in converted_list:
            file.write(str(value) + '\n')



