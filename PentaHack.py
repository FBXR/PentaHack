import time
import random 

pers = 0

while pers <= 100:

    timer = '{0}'.format(pers)
    print(f"The Pentagon is hacked to - {pers}%", end = '\r')
    time.sleep(random.uniform(0.1, 0.7))
    pers += random.randint(1, 5 )
    
print('The Pentagon has been successfully hacked! ')

time.sleep(3)
