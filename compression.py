import trie as T
import utils
import glv

def compress(input_file, output_file):
    with open(input_file, 'r') as input:
        text = input.read()
        with open(output_file, 'wb') as output:
            _iterate_file(output, text)

    ####### ONLY FOR TESTS #######
    _statistics(input_file, output_file)
    ##############################


def _statistics(input_file, output_file):
    print('Compression: ' + input_file + " -> " + output_file)
    utils.show_statistics(input_file, output_file)

def _iterate_file(file, text): 
    index = 1
    chain = ''
    trie = T.Trie('', numeric_value=0)

    for c in text:
        contains = trie.contains(chain + c)
        if contains != -1:
            chain += c
            continue

        chain_index = trie.contains(chain)
        trie.add(chain + c, index)
        file.write(chain_index.to_bytes(glv.INT_SIZE, 'big'))
        file.write(ord(c).to_bytes(glv.CHAR_SIZE, 'big'))
        chain = ''
        index += 1

    compressed = (trie.contains(chain)).to_bytes(glv.INT_SIZE, "big")
    return compressed