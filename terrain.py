# define a function that determines a brightness for any given point
# uses a seed that is a list of four numbers
def get_brightness(x,y,qc,seed):
    qc.data.clear() # empty the circuit
    
    # perform rotations whose angles depend on x and y
    qc.rx((1/8)*(seed[0]*x-seed[1]*y)*pi,0)
    qc.ry((1/8)*(seed[2]*x+seed[3]*y**2)*pi+pi,0)

    # calculate probability for outcome 1
    qc.measure(0,0)
    p = simulate(qc,shots=1000,get='counts')['1']/1000
    # return brightness depending on this probability
    # the chosen values here are fairly arbitrary
    if p>0.7:
        if p<0.8:
            return 1
        elif p<0.9:
            return 2
        else:
            return 3
    else:
        return 0
        
        
###########################################################


import pew
from microqiskit import QuantumCircuit, simulate
from math import pi
from random import random

pew.init()
screen = pew.Pix()

# initialize circuit
qc = QuantumCircuit(1,1)

# set a random seed, composed of four numbers
seed = [(2*(random()<0.5)-1)*(1+random())/2 for _ in range(4)]

# coordinate of the current screen
X,Y = 0,0
    
# loop to allow player to move half a screen
while True:
    
    # arrow keys move to neighbouring screens
    keys = pew.keys()
    if keys!=0:
        if keys&pew.K_UP:
            Y -= 4
        if keys&pew.K_DOWN:
            Y += 4
        if keys&pew.K_LEFT:
            X -= 4
        if keys&pew.K_RIGHT:
            X += 4
    
    # loop over all points on the screen, and display the brightness
    for x in range(8):
        for y in range(8):
            B = get_brightness(x+X,y+Y,qc,seed) # coordinate of the player is accounted for also
            screen.pixel(x,y,B)
    pew.show(screen)

    pew.tick(1/6)