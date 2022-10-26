import chardet

# bytes
# {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
print(chardet.detect(b'hello'))

# utf-8
# {'encoding': 'utf-8', 'confidence': 0.7525, 'language': ''}
print(chardet.detect("我们".encode('utf-8')))

# gbk
# {'encoding': 'TIS-620', 'confidence': 0.8095977270813678, 'language': 'Thai'}
print(chardet.detect("我们".encode('gbk')))
