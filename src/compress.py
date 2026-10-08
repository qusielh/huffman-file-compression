
class Compress:

    def __init__(self):
        pass

    def compress_and_save(self, path):

        print("reading contents from input file...")
        text = Compress.read_file(path)

        frequencies = Compress.count_frequencies(text)
        print("writing frequencies to file...")
        Compress.write_to_file(frequencies, "freq")

        print("creating sorted node list...")
        node_list = Compress.create_sorted_node_list(frequencies)

        print("creating huffman tree")
        huffman_tree = Compress.build_huffman_tree(node_list)

        print("generating codes...")
        codes = Compress.generate_huffman_codes(huffman_tree)

        print("encoding data...")
        encoded_text = Compress.encode_text(text, codes)
        print("writing encoded data to file...")
        Compress.write_to_file(encoded_text, "enc")

    def read_file(path):
        with open(path, "r", encoding="utf-8") as file:
            text = file.read()

        return text

    def write_to_file(data, switch_code):

        if switch_code == "freq":
            with open("content/compress contents/frequencies.txt", "w") as file:
                file.write("Uni/Freq\n")
                for key in data:
                    file.write(f"{ord(key)}:{data[key]}\n")

        elif switch_code == "enc":
            with open("content/compress contents/compressed_text.txt", "w") as file:
                file.write(data)


    def count_frequencies(text):

        frequencies = {}
        total_char_count = 0

        for char in text:
            if char in frequencies:
                frequencies[char] += 1
            else:
                frequencies[char] = 1
            total_char_count = total_char_count + 1

        print("total number of character : " + str(total_char_count))
        return frequencies


    def create_sorted_node_list(frequencies):

        node_list = []
        for char in frequencies:
            node_list.append({'symbol': char, 'frequency': frequencies[char]})
            
        node_list.sort(key=lambda x: (x['frequency']))
    
        return node_list


    def build_huffman_tree(node_list):
        
        while len(node_list) > 1:
            node1 = node_list[0]
            node_list.remove(node_list[0])
            node2 = node_list[0]
            node_list.remove(node_list[0])
            parent_node = {'frequency': node1['frequency'] + node2['frequency'], 'left': node1, 'right': node2}
            node_list.append(parent_node)

        return node_list[0]
  

    def generate_huffman_codes(node, current_code=""):

        if 'symbol' in node:
            return {node['symbol']: current_code}

        codes = {}
        if 'left' in node:
            codes.update(Compress.generate_huffman_codes(node['left'], current_code + "0"))
        if 'right' in node:
            codes.update(Compress.generate_huffman_codes(node['right'], current_code + "1"))

        return codes


    def encode_text(text, codes):

        encoded = ""
        for char in text:
            encoded += codes[char]
        return encoded