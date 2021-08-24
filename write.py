def write(size, name):
    with open(name, 'w') as f:
        f.write('a'*size)

write(1, '1B.txt')
write(10, '10B.txt')
write(100, '100B.txt')
write(1024, '1KB.txt')
write(1024*10, '10KB.txt')
write(1024*100, '100KB.txt')
write(1024*1024, '1MB.txt')
write(1024*1024*10, '10MB.txt')
write(1024*1024*100, '100MB.txt')
