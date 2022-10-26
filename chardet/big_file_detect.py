from chardet.universaldetector import UniversalDetector

lines = '\n'.encode('utf-8').join(['hello'.encode('utf-8'), 'world'.encode('utf-8'), 'women'.encode('utf-8')])

# 大文件不使用全部的内容识别编码，只需使用足够的字符数量即可
detector = UniversalDetector()
for line in lines:
    detector.feed(line)
    if detector.done:
        break
detector.close()
print(detector.result)