l=[1,2,3]
s={1,2,3}
c=point(2.0,4.0)
def test1(data):
    if isinstance(data,list):
        print('list:',data)
    if isinstance(data,set):
        print('set:',data)
    if isinstance(data,class):
        print('class:',data)


t=