#Q. 68:

#Huffman Encoding(Matrix Operations)

#Given An array of Alphabets and their frequency. Your task is to print all the given alphabets Huffman Encoding.
#Note: If two elements have same frequency, then the element which if at first will be taken on left of Binary Tree and other one to right.
#Input:
#First line consists of test cases T. First line of every test case consists of string of alphabets and second line consists of its frequencies.
#Output:
#Print the HuffmanCodes in single line, with n spaces of each alphabet's HuffmanCodes respectively. In PreOrder form of Binary Tree.
#Constraints:
#1<=T<=100
#1<=|String length|<=26


import heapq

listQ  = []
class HuffmanItem:

    def __init__(self, frequency, letter, left_son, right_son):
        self.freq = frequency
        self.alpha = letter
        self.left = left_son
        self.right = right_son

    def __lt__(self, other):
        return self.freq < other.freq


def print_codes(tree, str_collector):
    if tree is None:
        return

    if tree.alpha != '$':
        listQ.append(int(str_collector))

    print_codes(tree.left, str_collector + '0')
    print_codes(tree.right, str_collector + '1')


if __name__ == '__main__':

    t = int(input())
    for _ in range(t):
        alpha = list(input())
        freq = list(map(int, input().split()))

        pq = []
        for i in range(len(alpha)):
            heapq.heappush(pq, HuffmanItem(freq[i], alpha[i], None, None))

        while len(pq) != 1:
            left = heapq.heappop(pq)
            right = heapq.heappop(pq)
            top = HuffmanItem(left.freq + right.freq, '$', left, right)
            heapq.heappush(pq, top)

        print_codes(heapq.heappop(pq), "")
        print(listQ)
        print()
