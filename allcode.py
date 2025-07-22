import heapq
import math
import docx2txt
import csv

def read_text(docx_file_path):
    text = docx2txt.process(docx_file_path)
    return text

def build_frequency_dict(text):
    frequency_dict = {}
    for char in text:
        if char == ' ':
            char = '(space)'
        if char == '\n':
            continue
        if char not in frequency_dict:
            frequency_dict[char] = 0
        frequency_dict[char] += 1
    return frequency_dict

def calculate_total_characters(frequency_dict):
    return sum(frequency_dict.values())

def calculate_probabilities(frequency_dict, total_characters):
    probabilities = {}
    for char, freq in frequency_dict.items():
        probabilities[char] = freq / total_characters
    return probabilities

class Node:
    def __init__(self, char=None, frequency=0, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(frequency_dict):
    heap = []
    for char, freq in frequency_dict.items():
        node = Node(char=char, frequency=freq)
        heapq.heappush(heap, node)
    while len(heap) > 1:
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)
        merged_node = Node(
            frequency=low.frequency + high.frequency,
            left=low,
            right=high
        )
        heapq.heappush(heap, merged_node)
    return heap[0] if heap else None

def traverse_huffman_tree(node, code="", result=None):
    if result is None:
        result = []
    if node.char is not None:
        result.append((node.char, code))
    if node.left:
        traverse_huffman_tree(node.left, code + "0", result)
    if node.right:
        traverse_huffman_tree(node.right, code + "1", result)
    return result

def calculate_entropy(probabilities):
    entropy = 0
    for p in probabilities.values():
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy

def find_average_number_of_bits(huffman_codes, probabilities):
    average_bits = 0
    for char, prob in probabilities.items():
        code_length = len(huffman_codes[char])
        average_bits += prob * code_length
    return average_bits

def main():
    text = read_text("To_Build_A_Fire_by_Jack_London.docx")
    frequency_dict = build_frequency_dict(text)
    total_characters = calculate_total_characters(frequency_dict)
    probabilities = calculate_probabilities(frequency_dict, total_characters)
    root = build_huffman_tree(frequency_dict)
    huffman_list = traverse_huffman_tree(root)
    huffman_list.sort(key=lambda x: x[0])
    huffman_codes = {char: code for char, code in huffman_list}
    entropy = calculate_entropy(probabilities)
    average_bits = find_average_number_of_bits(huffman_codes, probabilities)
    bits_ascii = total_characters * 8
    bits_huffman = 0
    for char, freq in frequency_dict.items():
        bits_huffman += freq * len(huffman_codes[char])
    percentage_compression = (bits_huffman / bits_ascii) * 100
    with open("huffman_result.csv", mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Character", "Frequency", "Probability", "HuffmanCode", "CodeLength"])
        for char, code in huffman_list:
            freq = frequency_dict[char]
            prob = probabilities[char]
            writer.writerow([char, freq, f"{prob:.6f}", code, len(code)])
    with open("summary_result.csv", mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Total Characters", total_characters])
        writer.writerow(["Entropy (bits/character)", f"{entropy:.5f}"])
        writer.writerow(["Average (bits/character)", f"{average_bits:.5f}"])
        writer.writerow(["Number Of Bits For ASCII", bits_ascii])
        writer.writerow(["Number Of Bits For Huffman", bits_huffman])
        writer.writerow(["Percentage Of Compression (%)", f"{percentage_compression:.2f}"])
    print(f"Total Characters:  {total_characters}")
    print(f"Entropy:          {entropy:.5f} bits/character")
    print(f"Average:          {average_bits:.5f} bits/character")
    print(f"Number Of Bits For ASCII:   {bits_ascii}")
    print(f"Number Of Bits For Huffman: {bits_huffman}")
    print(f"Percentage Of Compression:  {percentage_compression:.2f}%")

if __name__ == "__main__":
    main()
