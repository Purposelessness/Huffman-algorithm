from collections import Counter
from collections import namedtuple
import heapq


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s: str):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq_1, count_1, left = heapq.heappop(h)
        freq_2, count_2, right = heapq.heappop(h)

        heapq.heappush(h, (freq_1 + freq_2, count, Node(left, right)))

        count += 1
    code = {}

    if h:
        [(freq, count, root)] = h
        root.walk(code, "")
    return code


def huffman_decode(encoded: str, code):
    res = []
    encoded_ch = ""
    for ch in encoded:
        encoded_ch += ch
        for decoded_ch in code:
            if code.get(decoded_ch) == encoded_ch:
                res.append(decoded_ch)
                encoded_ch = ""
                break
    return "".join(res)
