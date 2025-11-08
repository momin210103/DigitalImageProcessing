import heapq

class Node:
    def __init__(self,freq,symbol=None):
        self.freq = freq
        self.symbol = symbol
        self.left = None
        self.right = None
    def __lt__(self,other):
        return self.freq<other.freq


def buildhuffmantree(sf):
    heap = []
    for symbol,freq in sf:
        node = Node(freq,symbol)
        heapq.heappush(heap,node)
    while len(heap)>1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap,merged)
    return heap[0]
def getCode (root,currentNode="",codebook=None):
    if codebook is None:
         codebook = {}
    if root is None:
        return codebook
    if root.symbol is not None:
        codebook[root.symbol] = currentNode
    getCode(root.left,currentNode+'0',codebook)
    getCode(root.right, currentNode + '1', codebook)
    return codebook



sf = [('A',0.3),('B',0.3),('C',0.2),('D',0.1),('E',0.1)]
print(sf)

root = buildhuffmantree(sf)
hcode = getCode(root)
for symbol,code in hcode.items():
    print(f"{symbol}:{code}")


























# import heapq

# class Node:
#     def __init__(self, freq, symbol=None):  # <-- FIXED double underscores
#         self.freq = freq
#         self.symbol = symbol
#         self.left = None
#         self.right = None
#
#     def __lt__(self, other):  # <-- FIXED double underscores
#         return self.freq < other.freq
#
#
# def buildHuffmanTree(sf):
#     heap = []
#     for symbol, freq in sf:
#         node = Node(freq, symbol)
#         heapq.heappush(heap, node)
#
#     while len(heap) > 1:
#         left = heapq.heappop(heap)
#         right = heapq.heappop(heap)
#
#         merged = Node(left.freq + right.freq)
#         merged.left = left
#         merged.right = right
#         heapq.heappush(heap, merged)
#
#     return heap[0]
#
#
# def ghcode(root, current_code="", codebook=None):
#     if codebook is None:
#         codebook = {}
#
#     if root is None:
#         return codebook
#
#     if root.symbol is not None:
#         codebook[root.symbol] = current_code
#
#     ghcode(root.left, current_code + "0", codebook)
#     ghcode(root.right, current_code + "1", codebook)
#
#     return codebook
#
# sf = [('A', 0.1), ('B', 0.1), ('C', 0.2), ('D', 0.3), ('E', 0.3)]
# print(sf)
#
# root = buildHuffmanTree(sf)
# huffman_codes = ghcode(root)
#
# print("\nHuffman Codes:")
# for symbol, code in huffman_codes.items():
#  print(f"{symbol}: {code}")


