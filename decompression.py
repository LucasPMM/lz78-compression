import utils
import glv

def decompress(input_file, output_file):
    with open(input_file, 'rb') as file:
        decoded = _iterate_file(file)

    utils.write_file(output_file, decoded)
    
    ####### ONLY FOR TESTS #######
    _statistics(input_file, output_file)
    ##############################

def _statistics(input_file, output_file):
    print('Decompression: ' + input_file + " -> " + output_file)
    utils.show_statistics(input_file, output_file)

def _iterate_file(file):
    decoded = ''
    trie = ['']
    while True:
        index = file.read(glv.INT_SIZE)
        if index == b'':
            break
        
        index = int.from_bytes(index, "big")
        char = file.read(glv.CHAR_SIZE)
        if char == b'':
            char = ''
        else:
            char = chr(int.from_bytes(char, 'big'))
        
        chain = trie[index]
        new_chain = chain + char
        decoded += new_chain
        trie += [new_chain]

    return decoded
