class Trie:
    def __init__(self):
        self.data = {}
        self.is_word = False


class prefixTree:
    def __init__(self):
        self.root = Trie()

    def insert(self, arr):
        # 最后没有字符的地方标记is_word
        node = self.root
        for inx, ch in enumerate(arr):
            next_node = node.data.get(ch)
            if next_node is None:
                node.data[ch] = Trie()
            node = node.data[ch]
        node.is_word = True

    def search(self, prefix):
        def vis(node, string, word_list):
            if node.is_word is True:
                word_list.append(string)
            for ch in node.data.keys():
                vis(node.data[ch], string + ch, word_list)

        # 先找到prefix的单词，在接着找node上的词语
        # 如果是直接在prefix的node上找，可能会浪费时间
        word_list = []
        node = self.root
        for ch in prefix:
            node = node.data.get(ch)
        vis(node, prefix, word_list)
        return word_list


if __name__ == '__main__':
    trie = prefixTree()
    trie.insert("something")
    trie.insert("sobody")
    trie.insert("somebody1")
    trie.insert("somebody3")
    # print(trie)
    print(trie.search('some'))
