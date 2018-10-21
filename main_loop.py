class fp(object):
    def __init__(self, north, east, alt, vel, leg, maxGs, rph, successRadius, wayp=None):
        self.north = north
        self.east = east
        self.alt = alt
        self.vel = vel
        self.leg = leg
        self.maxGs = maxGs
        self.rph = rph
        self.successRadius = successRadius
        self.wayp = []

curLoc = [0, 0, 0] #x, y, z
curWayp = [100, 100, 100]

def calcDist3D(curLoc, curWayp):
    return 0

def updateACPos(curLoc, newState):
    return 0

def getNewHeading(fp, curState, curLoc):
    return 0

def getNewPitch(fp, curState, curLoc):
    return 0

def getNewACState(fp, curState, curLoc):
    newHdg, newRoll = getNewHeading(fp, curState, curLoc)
    newPitch = getNewPitch(fp, curState, curLoc)
    newVel = curState[1]

    newState = [newVel, newRoll, newPitch, newHdg]
    newLoc = updateACPos(curLoc, newState)

temp = fp(1, 2, 3, 4, 5, 6, 7, 8)
temp.north = [0, 0, 100, 0]
temp.east = [0, 100, 100, 0]
temp.alt = [0, 100, 50, 0]
temp.vel = [20, 20, 20, 20]
temp.rph = [1, 1, 1]
temp.wayp = [[100, 100, 100], [100, 100, 200]]
temp.leg = 0
temp.maxGs = 50
temp.successRadius = 5

print temp.alt

iteration_num = 100

curState = [0, temp.leg, temp.vel[0], temp.rph, temp.wayp[0]]

c = 0
while c < iteration_num:

    #determine if the desired waypoint has been reached
    if calcDist3D(curLoc, curWayp) <= temp.successRadius:
        #yay we're within the waypoint
        temp.leg += 1

        if temp.leg > len(temp.wayp):
            #reached all waypoints
            print "DONE"
            exit()

        #update waypoint
        curWayp = temp.wayp[temp.leg]

    #calculate new state
    curState, curLoc = getNewACState(temp, curState, curLoc)
