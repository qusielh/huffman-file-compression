from compress import Compress
from decompress import Decompress

class huffman(Compress, Decompress):

    def __init__(self):
        pass
       
    def encode(self, path):
        self.compress_and_save(path)
    
    def decode(self,path):
        self.decode_text(path)



def main():
    
    
    input_path = r"content/input text/input.txt"

    run_huffman = huffman()
    print("Starting algorithm...")
    run_huffman.encode(input_path)
    print("DONE!")
    print("-------------------------------")
    print("Running Decoder...")
    run_huffman.decode(r"content/compress contents/frequencies.txt")
   

if __name__ == "__main__":
    main()