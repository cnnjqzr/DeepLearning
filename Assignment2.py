import string
import re
def words(text): return re.findall('[a-z]+', text.lower())
def add_words(word, words_dict):
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1
def process_line(line, words_dict):
    """处理文件每行数据"""
    line = line.strip()
    words_list = line.split()
    pattern = re.compile(r'[a-z]+')
    for word in words_list:
        word = word.lower().strip(string.punctuation)  # 删除进过分割的单词的尾部的一些符号
        match = pattern.match(word)
        if match:
            add_words(word, words_dict)  # 调用add_words函数，把单词插入到words_dict字典中

def print_result(words_dict):
    """按格式输出words_dict中的数据"""
    val_key_list = []
    for key, val in words_dict.items():
        val_key_list.append((val, key))
    val_key_list.sort(reverse=True)  # 对val值进行逆排序
    for val, key in val_key_list:
            print ("%-12s   %3d" % (key, val))
END = '$'
def make_trie(words):
    trie = {}
    for word in words:
        t = trie
        for c in word:
            if c not in t: t[c] = {}
            t = t[c]
        t[END] = {}
    return trie

def check_fuzzy(trie, word, path='', tol=1):
    if tol < 0:
        return set()
    elif word == '':
        return {path} if END in trie else set()
    else:
        ps = set()
        for k in trie:
            ps |= check_fuzzy(trie[k], word[1:], path+k,
                                 tol-1 if k != word[0] else tol)
        return ps

##################################################
def main():
    """主函数"""
    '''words_dict = {}
    pFile = open("tweets", "r")

    for line in pFile:
        process_line(line, words_dict)
    print ("the length of the dictionary:", len(words_dict))
    print_result(words_dict)'''
    dFile = open("english-words","r")
    word = []
    for line in dFile:
        line = line.strip('\n')
        word.append(line)
    trie_word = make_trie(word)
    print(check_fuzzy(trie_word, 'hellu', tol=1))

main()