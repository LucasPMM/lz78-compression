import utils

def decompress(input_file, output_file):
    decoded = ''
    trie = ['']
    
    with open(input_file, 'rb') as file:
        while True:
            index = file.read(3)
            if index == b'':
                break
            
            index = int.from_bytes(index, "big")
            char = file.read(1)
            if char == b'':
                char = ''
            else:
                char = chr(int.from_bytes(char, 'big'))
            
            chain = trie[index]
            new_chain = chain + char
            decoded += new_chain
            trie += [new_chain]

    utils.write_file(output_file, decoded)
    
    ####### ONLY FOR TESTS #######
    print('Decompression: ' + input_file + " -> " + output_file)
    utils.show_statistics(input_file, output_file)
    ##############################
