import trie as CTrie
import utils

def compress(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()
        with open(output_file, 'wb') as file:
            trie = CTrie.Trie('', numeric_value=0)
            chain = ''
            index = 1
            for c in text:
                contains = trie.contains(chain + c)
                if contains != -1:
                    chain += c
                else:
                    chain_index = trie.contains(chain)
                    trie.add(chain + c, index)
                    file.write(chain_index.to_bytes(3, 'big'))
                    file.write(ord(c).to_bytes(1, 'big'))
                    index += 1
                    chain = ''
            file.write((trie.contains(chain)).to_bytes(3, "big"))

    ####### ONLY FOR TESTS #######
    print('Compression: ' + input_file + " -> " + output_file)
    utils.show_statistics(input_file, output_file)
    ##############################