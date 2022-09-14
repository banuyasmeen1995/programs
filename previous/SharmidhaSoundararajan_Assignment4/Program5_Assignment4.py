
import random
import math
import numpy as np

def main():
    time = 0
    for i in range(1,1000):   
        x = 0
        y = 0
        distance=0
        while(distance <= 1):
            result = ['N','S','E','W']
            direction = random.choices(result) #randomly generate values in 4 directions
            for j in direction:
                if(j == 'N'):
                    y += 0.6
                elif(j == 'S'):
                    y -= 0.6
                elif(j == 'E'):
                    x += 0.6
                else:
                    x -= 0.6  
            distance = math.sqrt((x)**2 + (y)**2)
            time += 1   
    print("Average time in seconds is", round(time/1000, 2))
main()
