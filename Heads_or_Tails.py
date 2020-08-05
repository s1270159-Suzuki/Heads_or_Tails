import random

def main():
  k = 0
  l = 0

  name = input('Who are you?')
  print('Hello, {}'.format(name))

  print('Tssing a coin...')

  for i, a in enumerate(range(3)):
    b = Heads_or_Tails()
    print('Round {}: {}'.format(i+1,b))
    if(b == 'Heads'):
      k = k + 1
    else:
      l = l + 1

  print('Heads: {}, Tails: {}'.format(k,l))

  if(k > l):
    print('You won')
  else:
    print('You lost')
    

def Heads_or_Tails():
  if(random.randrange(2) == 0):
    return 'Heads'
  else:
    return 'Tails'

if __name__ == '__main__':
  main()