# Huffman File Compression Engine

A pure Python implementation of the Huffman lossless data compression algorithm. The project implements a complete encoding and decoding pipeline without third-party dependencies, featuring frequency mapping, tree reconstruction, and bitstream serialization.

---

## How It Works

Huffman coding is an entropy-encoding algorithm that achieves lossless data compression by assigning variable-length prefix codes to characters based on their frequency of occurrence. More frequent characters receive shorter binary codes, while rarer characters receive longer codes.

```
       [Root]
      /      \
    '0'      '1'
    /          \
  'e' (freq: 12) [Node]
                /      \
              '0'      '1'
              /          \
        't' (freq: 6)  'a' (freq: 5)
```

### The Compression Pipeline (`compress.py`)
1. **Frequency Mapping:** Reads the raw input stream and counts character frequencies using a hash map ($O(N)$).
2. **Priority Forest:** Initializes leaf nodes (`{'symbol': char, 'frequency': count}`) and sorts them by frequency.
3. **Tree Construction:** Greedily pairs the two lowest-frequency nodes to form a parent node with a combined frequency until a single root node remains.
4. **Prefix Code Generation:** Traverses the binary tree recursively (left edge = `0`, right edge = `1`), assigning unique prefix-free binary codes to every symbol.
5. **Serialization:** Replaces input characters with their bit representations and exports the frequency table alongside the encoded output.

### The Decompression Pipeline (`decompress.py`)
1. **Table Inversion:** Parses the exported frequency map and reconstructs the identical Huffman tree topology.
2. **Tree Traversal Decoding:** Iterates through the encoded bit sequence, stepping left (`0`) or right (`1`) from the root until reaching a leaf node, extracting symbols in $O(M)$ time where $M$ is the number of encoded bits.

---

## Project Structure

```text
├── Program.py             # Main entry point unifying encoder and decoder
├── compress.py            # Compression logic and tree generation
├── decompress.py          # Decompression logic and file recovery
└── content/
    ├── input text/        # Source text to compress (e.g., input.txt)
    ├── compress contents/ # Serialized frequency table and encoded text
    └── decompress contents/ # Fully recovered, decoded text
```

---

## Getting Started

### Prerequisites
* Python 3.8+ (Standard Library only — no `pip install` required)

### Running the Compression & Decompression
Place your target text file in `content/input text/input.txt` and run:

```bash
python Program.py
```

The script will:
1. Encode the file and write results into `content/compress contents/`.
2. Automatically run the decompression pipeline to verify integrity and write the reconstructed file to `content/decompress contents/decoded_text.txt`.