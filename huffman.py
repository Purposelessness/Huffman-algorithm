from collections import Counter
from collections import namedtuple
import heapq


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

    def __str__(self):
        return f"[left = {self.left} | right = {self.right}]"


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"
        print(f"'{self.char}' = {acc}")

    def __str__(self):
        return f"('{self.char}')"


def huffman_encode(s: str):
    h = []
    print(f"Encoding string: {s}")
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    print(f"Heap: {[f'{freq}, {str(val)}' for (freq, count, val) in h]}")
    count = len(h)
    while len(h) > 1:
        freq_1, count_1, left = heapq.heappop(h)
        freq_2, count_2, right = heapq.heappop(h)

        heapq.heappush(h, (freq_1 + freq_2, count, Node(left, right)))

        print(f"Heap: {[f'{freq}, {str(val)}' for (freq, count, val) in h]}")
        count += 1
    code = {}

    if h:
        [(freq, count, root)] = h
        root.walk(code, "")
    return code


def huffman_decode(encoded: str, code):
    res = []
    print(f"Decoding string: {encoded}")
    encoded_ch = ""
    for ch in encoded:
        encoded_ch += ch
        for decoded_ch in code:
            if code.get(decoded_ch) == encoded_ch:
                res.append(decoded_ch)
                print(f"{encoded_ch} = {decoded_ch} -> result: {''.join(res)}")
                encoded_ch = ""
                break
    return "".join(res)
