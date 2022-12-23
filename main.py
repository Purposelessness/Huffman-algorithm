from huffman import huffman_encode
from huffman import huffman_decode


def encode_file():
    with open("decoded.txt", "r") as f:
        s = f.readline().rstrip()
    print("Input:")
    print(s)
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    with open("encoded.txt", "w") as f:
        f.write(f"{encoded}\n")
        for ch in sorted(code):
            f.write(f"{ch}: {code[ch]}\n")
    print("")
    print("Output:")
    print(encoded)
    print(dict(sorted(code.items())))


def decode_file():
    with open("encoded.txt", "r") as f:
        encoded = f.readline().rstrip()
        if encoded == '':
            return
        s = f.readline().rstrip()
        code: dict[str, str] = {}
        while s != '':
            (ch, val) = tuple(s.split(': '))
            code[ch] = val
            s = f.readline().rstrip()
    print("Input:")
    print(encoded)
    print(code)
    decoded = huffman_decode(encoded, code)
    with open("decoded.txt", "w") as f:
        f.write(decoded)
    print("")
    print("Output:")
    print(decoded)


def task():
    print("1 - encode file (decoded.txt)\n2 - decode file (encoded.txt)")
    i = input()
    if i == "1":
        encode_file()
    else:
        decode_file()


if __name__ == "__main__":
    task()
