# There could be a much simpler solution, just copy and past those string lines from lab intro. But I decided to take it to an upper challenge, bring aglity to this program:
# 1. menu is editable. you can add or delete thing in each menu.
# 2. program will double check client's order input, if customer want to order something not on the menu, it will ge rejected. 

# defind 4 menus. 
Appetizers=['Wings','Cookies','Spring Rolls']
Entrees=['Salmon','Steak','Meat Tornado','A Literal Garden']
Desserts=['Ice Cream','Cake','Pie']
Drinks=['Coffee','Tea','Unicorn Tears']

# setup greeting messages
greeting = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""
ordering="""***********************************
** What would you like to order? **
***********************************"""


#display greetings and menu to customers
print(greeting)
print('Appetizers','----------',*Appetizers,'', sep='\n')
print('Entrees','-------',*Entrees,'',sep='\n')
print('Desserts', '--------', *Desserts, '', sep='\n')
print('Drinks', '------', *Drinks,'', sep='\n')
print(ordering)

# make a dict to hold all the customer's order
order={}

# function part.
while True:
  takeIn=input()
  if takeIn=='quit':
    break
  elif takeIn in (set(Appetizers)|set(Entrees)|set(Desserts)|set(Drinks)):
    if takeIn not in order:
      order[takeIn] = 1
      print(f'** 1 order of {takeIn} have been added to your meal **')
    elif takeIn in order:
      order[takeIn]+=1
      print(f'** {order[takeIn]} orders of {takeIn} have been added to your meal **')
  else: #this is the extra piece I've added. If customer type something not in menu, he will be notified.
    print(f'** Sorry, we do not provide {takeIn} yet, please order something else **')
