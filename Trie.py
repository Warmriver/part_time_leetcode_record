# coding=utf-8
# Implementation of Trie
class Node:
    def __init__(self, val, nodes, end):
        self.val = val
        self.end = end
        self.nodes = nodes
    def printWords(self, words, w):
        w += self.val
        if self.end:
            words.append(w)
        else:
            for node in self.nodes:
                node.printWords(words, w)

def generateTrie():
    f_list = ['bitch', 'fuck', 'fucker', 'noob', 'bastard']
    #f_list = ['bitch', 'fuck']
    root = Node('*', [], False)
    for w in f_list:
        w_nodes = root.nodes
        for i, l in enumerate(w):
            l_node = Node(l, [], True if i == len(w) - 1 else False)
            if not w_nodes:
                w_nodes.append(l_node)
                w_nodes = l_node.nodes
            else:
                hit = False
                for w_node in w_nodes:
                    if l_node.val == w_node.val:
                        w_nodes = w_node.nodes
                        hit = True
                        break
                if not hit:
                    w_nodes.append(l_node)
                    w_nodes = l_node.nodes
    return root

def test_gen():
    root = generateTrie()
    print('root node first level vals are...')
    for c in root.nodes:
        print('-------------')
        print(c.val, c.end)
        print('for {0}, level 2 has...'.format(c.val))
        for cc in c.nodes:
            print(cc.val, cc.end)

    dicts = []
    root.printWords(dicts, '')
    print(dicts)


def check(word, nodes):
    temp_nodes = nodes
    hit = False
    for i, l in enumerate(word):
        if not temp_nodes:
            return False
        for node in temp_nodes:
            if node.val == l:
                temp_nodes = node.nodes
                hit = True
                break
            else:
                hit = False
        if not hit:
            return False
        if node.end and i == len(word) - 1:
            return True
        if not node.end and i == len(word) - 1:
            return False
    return False

if __name__ == '__main__':
    root_node = generateTrie()
    while True:
        str_input = input("please input one word, press n and enter to stop \n")
        if str_input == 'n':
            print("bye")
            break
        valid = check(str_input, root_node.nodes)
        print("is valid: {0}".format(valid))
