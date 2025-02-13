import random
import matplotlib
import matplotlib.pyplot as plt
import time


def rollDice():
    roll = random.randint(1, 100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll >= 50:
        return True


def doubler_bettor(funds, initial_wager, wager_count):
    global broke_count
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1

    previousWager = 'win'

    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':

            if rollDice():
                value += wager
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager
                previousWager = 'loss'
                ##print value
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    broke_count += 1
                    currentWager += 10000000000000000
        elif previousWager == 'loss':
            if rollDice():
                wager = previousWagerAmount * 2

                value += wager

                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2

                value -= wager

                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:

                    currentWager += 10000000000000000
                    broke_count += 1

        currentWager += 1


    plt.plot(wX, vY)


xx = 0
broke_count = 0

while xx < 1000:
    doubler_bettor(10000, 100, 100)
    xx += 1

print ('death rate:',(broke_count/float(xx)) * 100)
print ('survival rate:',100 - ((broke_count/float(xx)) * 100))
plt.axhline(0, color='r')
plt.show()
