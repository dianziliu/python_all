import random
def create_data():
    f=open("data.txt","w")
    for i in range(1000):
        j=random.randrange(1,99)
        f.write(str(j)+ '')
    pass
