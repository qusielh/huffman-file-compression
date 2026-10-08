import compress

class Decompress:

    def __init__(self):
        pass

    def decode_text(self, path):

        print("reading frequencies...")
        frequencies = Decompress.read_frequencies_from_file(path)

        print("preparing for the decoding process to start...")

        node_list = compress.Compress.create_sorted_node_list(frequencies)

        huffman_tree = compress.Compress.build_huffman_tree(node_list)
        
        print("reading encoded data...")
        with open("content/compress contents/compressed_text.txt", "r") as file:
            encoded_text = file.read()

        decoded_text = ""
        current_node = huffman_tree

        for char in encoded_text:
            if char == "0":
                current_node = current_node["left"]
            elif char == "1":
                current_node = current_node["right"]
            if "symbol" in current_node:
                decoded_text = decoded_text + current_node["symbol"]
                current_node = huffman_tree
           
        print("writing decoded data to file...")
        with open("content/decompress contents/decoded_text.txt", "w") as file:
            file.write(decoded_text)

        print("DECODING FINISHED!\n\n\n\n")
        print("NOTE: please check 'content' folder to check the output in the files")

    def read_frequencies_from_file(file_path):

        frequencies = {}

        with open(file_path, "r", encoding="utf-8") as file:
            next(file)
            for line in file:
                parts = line.split(':')
                character = chr(int(parts[0]))
                frequency = int((parts[1]))
                frequencies[character] = frequency

        return frequencies
