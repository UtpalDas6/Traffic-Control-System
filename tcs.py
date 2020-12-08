import emoji
import time
class Direction:
  def __init__(self,color):
    self.color = color
def current(N,E,W,S):
  print('====TRAFFIC====')
  print('N ',emoji.emojize(':'+N.color+':'))
  print('E ',emoji.emojize(':'+E.color+':'))
  print('S ',emoji.emojize(':'+S.color+':'))
  print('W ',emoji.emojize(':'+W.color+':'))
def tcs(N,E,W,S):
  while True:
    current(N,E,W,S)
    time.sleep(20)
    N.color = 'orange_heart'
    current(N,E,W,S)
    time.sleep(5)
    N.color = 'red_circle'
    E.color = 'green_heart'
    current(N,E,W,S)
    time.sleep(20)
    E.color = 'orange_heart'
    current(N,E,W,S)
    time.sleep(5)
    E.color = 'red_circle'
    S.color = 'green_heart'
    current(N,E,W,S)
    time.sleep(20)
    S.color = 'orange_heart'
    current(N,E,W,S)
    time.sleep(5)
    S.color = 'red_circle'
    W.color = 'green_heart'
    current(N,E,W,S)
    time.sleep(20)
    W.color = 'orange_heart'
    current(N,E,W,S)
    time.sleep(5)
    W.color = 'red_circle'
    N.color = 'green_heart'

N = Direction('green_heart')
E = Direction('red_circle')
S = Direction('red_circle')
W = Direction('red_circle')
tcs(N,E,W,S)
