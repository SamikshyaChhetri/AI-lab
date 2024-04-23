i=0  # initialize variable movement
def Monkey_go_box(x,y):
  global i
  i=i+1
  print('step:',i,'monkey slave',x,'Go to ',y)

def Monkey_move_box(x,y):
  global i
  i = i + 1
  print('step:', i, 'monkey take the box from', x, 'deliver to', y)

def Monkey_on_box():
  global i
  i = i + 1
  print('step:', i, 'Monkey climbs up the box')

def Monkey_get_banana():
  global i
  i = i + 1
  print('step:', i, 'Monkey picked a banana')
  # indicate the locations of monkey, banana, and box respectively.
monkey=0
banana=1
box=2
print('The steps are as follows:')
#Please use the least steps to complete the monkey picking banana task
Monkey_go_box(monkey, box)
Monkey_move_box(box, banana)
Monkey_on_box()
Monkey_get_banana()