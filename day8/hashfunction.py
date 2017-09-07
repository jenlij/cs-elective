def my_hash(word):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    return str(alpha.index(word[0])) + str(alpha.index(word[1]))
    

a = my_hash('adam')
print a