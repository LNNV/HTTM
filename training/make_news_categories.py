# Thống kê số lượng data theo nhãn
count = {}
for line in open('training/news_categories.txt',encoding="utf8"):
    key = line.split()[0]
    count[key] = count.get(key, 0) + 1

for key in count:
    print(key, count[key])
# Thống kê các word xuất hiện ở tất cả các nhãn
total_label = 18
vocab = {}
label_vocab = {}
for line in open('training/news_categories.txt',encoding="utf8"):
    words = line.split()
    # lưu ý từ đầu tiên là nhãn
    label = words[0]
    if label not in label_vocab:
        label_vocab[label] = {}
    for word in words[1:]:
        label_vocab[label][word] = label_vocab[label].get(word, 0) + 1
        if word not in vocab:
            vocab[word] = set()
        vocab[word].add(label)
count = {}
for word in vocab:
    if len(vocab[word]) == total_label:
        count[word] = min([label_vocab[x][word] for x in label_vocab])
        
sorted_count = sorted(count, key=count.get, reverse=True)
for word in sorted_count[:100]:
    print(word, count[word])
# loại stopword khỏi dữ liệu
# lưu file dùng về sau
stopword = set()
with open('training/stopwords.txt', 'w', encoding="utf8") as fp:
    for word in sorted_count[:100]:
        stopword.add(word)
        fp.write(word+'\n')
with open('training/stopwords.txt', 'r',  encoding="utf8") as fp:
    for word in fp:
        stopword.add(word)
def remove_stopwords(line):
    words = []
    for word in line.strip().split():
        if word not in stopword:
            words.append(word)
    return ' '.join(words)
    
with open('training/news_categories.prep', 'w',encoding="utf8") as fp:
    for line in open('training/news_categories.txt',encoding="utf8"):
        line = remove_stopwords(line)
        fp.write(line+'\n')
