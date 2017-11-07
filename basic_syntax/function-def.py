ss=1
def f1(x,y):
    ans=x+y
    print('Answer = ',ans)

f1(3,5)

# default parameter
print('--default parameter--')

def car(price=500,color='black'):
    return ('%s,%s' % (price,color))

car(1000,'red')
print(car())
