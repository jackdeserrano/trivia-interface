with open('scores.txt', 'w+') as f:
    for i in range(1000000):
        f.write(f'{i} 0 0\n')
