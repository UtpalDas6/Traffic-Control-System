import time
class Direction:
  def __init__(self,color):
    self.color = color
def current(N,E,W,S):
  print('====TRAFFIC====')
  print('North ',N.color)
  print('East ',E.color)
  print('South ',S.color)
  print('West ',W.color)
def tcs(N,E,W,S):
  while True:
    current(N,E,W,S)
    time.sleep(20)
    N.color = 'Orange'
    current(N,E,W,S)
    time.sleep(5)
    N.color = 'Red'
    E.color = 'Green'
    current(N,E,W,S)
    time.sleep(20)
    E.color = 'Orange'
    current(N,E,W,S)
    time.sleep(5)
    E.color = 'Red'
    S.color = 'Green'
    current(N,E,W,S)
    time.sleep(20)
    S.color = 'Orange'
    current(N,E,W,S)
    time.sleep(5)
    S.color = 'Red'
    W.color = 'Green'
    current(N,E,W,S)
    time.sleep(20)
    W.color = 'Orange'
    current(N,E,W,S)
    time.sleep(5)
    W.color = 'Red'
    N.color = 'Green'

N = Direction('Green')
E = Direction('Red')
S = Direction('Red')
W = Direction('Red')
tcs(N,E,W,S)
