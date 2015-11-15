import random
import time
from copy import deepcopy
points = 0
attempt = 0
counter = 0

print "Welcome to 2048!"
print "The AI will play the game using Minimax and special Heuristics"
num_turns_entered = raw_input("Please enter the number of levels deep -------->    ")
sleep_time = raw_input("Please enter the sleep time between moves in milliseconds -------->    ")

game_grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] # 4x4 array of zeros
tempGrid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] # 4x4 array of zeros
first_position_list = [0,1,2,3]

# Set first randomly spaced value of 2
firstRandomRow = random.choice(first_position_list)
firstRandomColumn = random.choice(first_position_list)
game_grid[firstRandomRow][firstRandomColumn] = 2

def up(grid):
    i = 0
    for j in range(0,4):
        if grid[i][j]!=0 or grid[i+1][j]!=0 or grid[i+2][j]!=0 or grid[i+3][j]!=0: # are there non-zeros
            if grid[i][j]==0:
                while grid[i][j]==0: # until first non-zero box
                    grid[i][j] = grid[i+1][j]
                    grid[i+1][j] = grid[i+2][j]
                    grid[i+2][j] = grid[i+3][j]
                    grid[i+3][j] = 0
            if grid[i+1][j]==0 and (grid[i+2][j]!=0 or grid[i+3][j]!=0): # is second box zero and boxes below it non zero
                while grid[i+1][j]==0:
                    grid[i+1][j] = grid[i+2][j]
                    grid[i+2][j] = grid[i+3][j]
                    grid[i+3][j] = 0
            if grid[i+2][j]==0 and grid[i+3][j]!=0:
                while grid[i+2]==0:
                    grid[i+2] = grid[i+3]
                    grid[i+3][j] = 0

def upAdd(grid):
    i=0
    global points
    for j in range(0,4):
        if grid[i][j]==grid[i+1][j]: # are first and second boxes the same?
            grid[i][j]=grid[i][j]+grid[i+1][j] # first and second boxes storing in the first
            points += grid[i][j]  # yay they get points
            grid[i+1][j]=grid[i+2][j] # move third to 2nd pos
            grid[i+2][j]=grid[i+3][j] # move 4th to 3rd pos
            grid[i+3][j]=0 # reset box
        if grid[i+1][j]==grid[i+2][j]: # are second and third boxes the same
            grid[i+1][j]=grid[i+1][j]+grid[i+2][j] # add 2nd and 3rd boxes
            points += grid[i+1][j]  # yay they get points
            grid[i+2][j]=grid[i+3][j] # move 4th to 3rd pos
            grid[i+3][j]=0 # reset box
        if grid[i+2][j]==grid[i+3][j]: # are third and fouth boxes the same
            grid[i+2][j]=grid[i+2][j]+grid[i+3][j] # add 3rd and 4th boxes
            points += grid[i+2][j]  # yay they get points
            grid[i+3][j]=0 # reset box

def down(grid):
    i = 0
    for j in range(0,4):
        if grid[i][j]!=0 or grid[i+1][j]!=0 or grid[i+2][j]!=0 or grid[i+3][j]!=0: # are there non-zeros
            if grid[i+3][j]==0:
                while grid[i+3][j]==0: # until first non-zero box
                    grid[i+3][j] = grid[i+2][j]
                    grid[i+2][j] = grid[i+1][j]
                    grid[i+1][j] = grid[i][j]
                    grid[i][j] = 0
            if grid[i+2][j]==0 and (grid[i+1][j]!=0 or grid[i][j]!=0): # is second box zero and boxes below it non zero
                while grid[i+2][j]==0:
                    grid[i+2][j] = grid[i+1][j]
                    grid[i+1][j] = grid[i][j]
                    grid[i][j] = 0
            if grid[i+1][j]==0 and grid[i][j]!=0:
                while grid[i+1][j]==0:
                    grid[i+1][j] = grid[i][j]
                    grid[i][j] = 0

def downAdd(grid):
    i=0
    global points
    for j in range(0,4):
        if grid[i+3][j]==grid[i+2][j]: # are first and second boxes the same?
            grid[i+3][j]=grid[i+3][j]+grid[i+2][j] # first and second boxes storing in the first
            points += grid[i+3][j]  # yay they get points
            grid[i+2][j]=grid[i+1][j] # move third to 2nd pos
            grid[i+1][j]=grid[i][j] # move 4th to 3rd pos
            grid[i][j]=0 # reset box
        if grid[i+2][j]==grid[i+1][j]: # are second and third boxes the same
            grid[i+2][j]=grid[i+2][j]+grid[i+1][j] # add 2nd and 3rd boxes
            points += grid[i+2][j]  # yay they get points
            grid[i+1][j]=grid[i][j] # move 4th to 3rd pos
            grid[i][j]=0 # reset box
        if grid[i+1][j]==grid[i][j]: # are third and fouth boxes the same
            grid[i+1][j]=grid[i+1][j]+grid[i][j] # add 3rd and 4th boxes
            points += grid[i+1][j]  # yay they get points
            grid[i][j]=0 # reset box

def left(grid):
    j = 0
    for i in range(0,4):
        if grid[i][j]!=0 or grid[i][j+1]!=0 or grid[i][j+2]!=0 or grid[i][j+3]!=0: # are there non-zeros
            if grid[i][j]==0:
                while grid[i][j]==0: # until first non-zero box
                    grid[i][j] = grid[i][j+1]
                    grid[i][j+1] = grid[i][j+2]
                    grid[i][j+2] = grid[i][j+3]
                    grid[i][j+3] = 0
            if grid[i][j+1]==0 and (grid[i][j+2]!=0 or grid[i][j+3]!=0): # is second box zero and boxes below it non zero
                while grid[i][j+1]==0:
                    grid[i][j+1] = grid[i][j+2]
                    grid[i][j+2] = grid[i][j+3]
                    grid[i][j+3] = 0
            if grid[i][j+2]==0 and (grid[i][j+3]!=0):
                while grid[i][j+2]==0:
                    grid[i][j+2] = grid[i][j+3]
                    grid[i][j+3] = 0

def leftAdd(grid):
    j=0
    global points
    for i in range(0,4):
        if grid[i][j]==grid[i][j+1]: # are first and second boxes the same?
            grid[i][j]=grid[i][j]+grid[i][j+1] # first and second boxes storing in the first
            points += grid[i][j]  # yay they get points
            grid[i][j+1]=grid[i][j+2] # move third to 2nd pos
            grid[i][j+2]=grid[i][j+3] # move 4th to 3rd pos
            grid[i][j+3]=0 # reset box
        if grid[i][j+1]==grid[i][j+2]: # are second and third boxes the same
            grid[i][j+1]=grid[i][j+1]+grid[i][j+2] # add 2nd and 3rd boxes
            points += grid[i][j+1]  # yay they get points
            grid[i][j+2]=grid[i][j+3] # move 4th to 3rd pos
            grid[i][j+3]=0 # reset box
        if grid[i][j+2]==grid[i][j+3]: # are third and fouth boxes the same
            grid[i][j+2]=grid[i][j+2]+grid[i][j+3] # add 3rd and 4th boxes
            points += grid[i][j+2]  # yay they get points
            grid[i][j+3]=0 # reset box

def right(grid):
    j = 0
    for i in range(0,4):
        if grid[i][j]!=0 or grid[i][j+1]!=0 or grid[i][j+2]!=0 or grid[i][j+3]!=0: # are there non-zeros
            if grid[i][j+3]==0:
                while grid[i][j+3]==0: # until first non-zero box
                    grid[i][j+3] = grid[i][j+2]
                    grid[i][j+2] = grid[i][j+1]
                    grid[i][j+1] = grid[i][j]
                    grid[i][j] = 0
            if grid[i][j+2]==0 and (grid[i][j+1]!=0 or grid[i][j]!=0): # is second box zero and boxes below it non zero
                while grid[i][j+2]==0:
                    grid[i][j+2] = grid[i][j+1]
                    grid[i][j+1] = grid[i][j]
                    grid[i][j] = 0
            if grid[i][j+1]==0 and (grid[i][j]!=0):
                while grid[i][j+1]==0:
                    grid[i][j+1] = grid[i][j]
                    grid[i][j] = 0

def rightAdd(grid):
    j=0
    global points
    for i in range(0,4):
        if grid[i][j+3]==grid[i][j+2]: # are first and second boxes the same?
            grid[i][j+3]=grid[i][j+3]+grid[i][j+2] # first and second boxes storing in the first
            points += grid[i][j+3]  # yay they get points
            grid[i][j+2]=grid[i][j+1] # move third to 2nd pos
            grid[i][j+1]=grid[i][j] # move 4th to 3rd pos
            grid[i][j]=0 # reset box
        if grid[i][j+2]==grid[i][j+1]: # are second and third boxes the same
            grid[i][j+2]=grid[i][j+2]+grid[i][j+1] # add 2nd and 3rd boxes
            points += grid[i][j+2]  # yay they get points
            grid[i][j+1]=grid[i][j] # move 4th to 3rd pos
            grid[i][j]=0 # reset box
        if grid[i][j+1]==grid[i][j]: # are third and fouth boxes the same
            grid[i][j+1]=grid[i][j+1]+grid[i][j] # add 3rd and 4th boxes
            points += grid[i][j+1]  # yay they get points
            grid[i][j]=0 # reset box

def analyze(gridA, movement_direction, num_turns):
    # do the move_direction and calculate the total
    # for example if called analyze(gridA, down, 2)
    # you would do downmove and downAdd and then compute the total for that state of the grid and assign that to total
    # keep highest number in top left and maybe numbers lined up along sides will be heuristic
    total = 0
    highest_number_on_grid = 0

    tempGrid2 = deepcopy(gridA)

    if movement_direction == "up":
        up(tempGrid2)
        upAdd(tempGrid2)
        # compute total
        for m in range(0,4):
            for n in range(0,4):
                if tempGrid2[m][n] > highest_number_on_grid:
                    highest_number_on_grid = tempGrid2[m][n]
        if tempGrid2[0][0] = highest_number_on_grid:
            total += 10
    elif movement_direction == "down":
        down(tempGrid2)
        downAdd(tempGrid2)
        total = 0
        # compute total
    elif movement_direction == "left":
        left(tempGrid2)
        leftAdd(tempGrid2)
        total = 0
        # compute total
    elif movement_direction == "right":
        right(tempGrid2)
        rightAdd(tempGrid2)
        total = 0
        # compute total

    turns = num_turns - 1
    highestNum = 0

    if num_turns > 0:
        upNum = analyze(tempGrid2, up, turns)
        downNum = analyze(tempGrid2, down, turns)
        leftNum = analyze(tempGrid2, left, turns)
        rightNum = analyze(tempGrid2, right, turns)

        # assuming we're adding all the values back up the tree
        highestNum = upNum
        if downNum > highestNum:
            highestNum = downNum
        if leftNum > highestNum:
           highestNum = leftNum
        if rightNum > highestNum:
            highestNum = rightNum

    return total + highestNum




# definition of logic for each turn
# call analyze for each direction (with a copy of the game grid) and pick whichever has the highest number as the direction to actually make a move to
while True:
    print "Points=>"
    print str(points)
    #line spacing
    print "\n\n"
    # printing game box each turn
    print game_grid[0][0],"\t",game_grid[0][1],"\t",game_grid[0][2],"\t",game_grid[0][3],"\n"
    print game_grid[1][0],"\t",game_grid[1][1],"\t",game_grid[1][2],"\t",game_grid[1][3],"\n"
    print game_grid[2][0],"\t",game_grid[2][1],"\t",game_grid[2][2],"\t",game_grid[2][3],"\n"
    print game_grid[3][0],"\t",game_grid[3][1],"\t",game_grid[3][2],"\t",game_grid[3][3],"\n"
    # take user input
    # user_input = raw_input("Please enter your move -------->    ")
    # done printing


    time.sleep (float(sleep_time) / 1000.0)
    counter += 1
    num_turns_entered = int(float(num_turns_entered))
    # num_turns_hardcode = 3


    #movement and analytics go here
    tempGrid = deepcopy(game_grid)
    highest_route_estimate = 0
    num1 = analyze(tempGrid, "up", num_turns_entered)
    num2 = analyze(tempGrid, "down", num_turns_entered)
    num3 = analyze(tempGrid, "left", num_turns_entered)
    num4 = analyze(tempGrid, "right", num_turns_entered)
    highest_route_estimate = num1
    if num2 > highest_route_estimate:
        highest_route_estimate = num2
    if num3 > highest_route_estimate:
        highest_route_estimate = num3
    if num4 > highest_route_estimate:
        highest_route_estimate = num4
    if highest_route_estimate == num1:
        up(game_grid)
        upAdd(game_grid)
        print "Moving up"
    elif highest_route_estimate == num2:
        down(game_grid)
        downAdd(game_grid)
        print "Moving down"
    elif highest_route_estimate == num3:
        left(game_grid)
        leftAdd(game_grid)
        print "Moving left"
    elif highest_route_estimate == num4:
        right(game_grid)
        rightAdd(game_grid)
        print "Moving right"


    print "Iteration: ", str(counter)




    # finding all Zero entries [0]
    rowIndexZero = []
    columnIndexZero = []
    for i in range(0,4):
        for j in range(0,4):
            if game_grid[i][j] == 0:
                rowIndexZero.append(i)
                columnIndexZero.append(j)
            if game_grid[i][j] == 2048:
                print "This AI has reached the goal of 2048!!"
                break
    # placing next random 2
    if len(rowIndexZero) > 1:
        random_index = rowIndexZero.index(random.choice(rowIndexZero))
        newRowEntry = rowIndexZero[random_index]
        newColumnEntry = columnIndexZero[random_index]
        game_grid[newRowEntry][newColumnEntry] = 2
    elif len(rowIndexZero) == 1:
        newRowEntry = rowIndexZero[0]
        newColumnEntry = columnIndexZero[0]
        game_grid[newRowEntry][newColumnEntry] = 2
    else:
        break

print "The AI scored ", str(points), "points this game!"
print "\n\n"
