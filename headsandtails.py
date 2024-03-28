import random
heads = 0
tails = 0

coin_flip = ['Heads', 'Tails']
print('Enter the number of flips you want: ')
flips = input()
flips = int(flips)


for i in range(flips):
    print(random.choice(coin_flip))
    if (random.choice(coin_flip) == 'Heads'):
        heads += 1
        
    elif (random.choice(coin_flip) == 'Tails'):
        tails += 1
        

print('Heads was flipped: ', heads, ' times,')
print('Tails was flipped: ', tails, ' times.')
