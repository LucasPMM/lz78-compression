import os

def write_file(name, data):
    file = open(name, 'w')
    file.write(data)
    file.close()
    return

def show_statistics(input, output):
    input_stats = os.stat(input)
    output_stats = os.stat(output)
    ratio = (output_stats.st_size / input_stats.st_size) * 100
    print('Compress ratio ' + str(ratio) + "%")
    return

def is_input_invalid(input):
    possible_args = [3, 5]
    possible_actions = ['-c', '-x']
    possible_extentions = ['txt', 'z78']

    extention = input[2].split('.')[1]

    invalid_length = len(input) not in possible_args
    invalid_action = input[1] not in possible_actions
    invalid_extention = extention not in possible_extentions
    invalid_compression = input[1] == '-c' and extention != 'txt'
    invalid_decompression = input[1] == '-x' and extention != 'z78'
    invalid_output = len(input) == 5 and input[3] != '-o'

    if invalid_length or invalid_action or invalid_extention or invalid_compression or invalid_decompression or invalid_output:
        return True
        