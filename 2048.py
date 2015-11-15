import random
points = 0
attempt = 0

print "Welcome to 2048!"
print "Directions:"
print "Use the w,a,s,d keys to move up, left, down or right."
print "Press Ctrl-C to quit."
print "Press enter after entering an input to move to the next turn."
print "The goal is to get a tile to have the value 2048."
print "If you can no longer move, you lose!"
print "GOOD LUCK!!!"

grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] # 4x4 array of zeros
first_position_list = [0,1,2,3]

# Set first randomly spaced value of 2
firstRandomRow = random.choice(first_position_list)
firstRandomColumn = random.choice(first_position_list)
grid[firstRandomRow][firstRandomColumn] = 2

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

# definition of logic for each turn
while True:
    print "Points=>"
    print str(points)
    #line spacing
    print "\n\n"
    # printing game box each turn
    print grid[0][0],"\t",grid[0][1],"\t",grid[0][2],"\t",grid[0][3],"\n"
    print grid[1][0],"\t",grid[1][1],"\t",grid[1][2],"\t",grid[1][3],"\n"
    print grid[2][0],"\t",grid[2][1],"\t",grid[2][2],"\t",grid[2][3],"\n"
    print grid[3][0],"\t",grid[3][1],"\t",grid[3][2],"\t",grid[3][3],"\n"
    # take user input
    user_input = raw_input("Please enter your move -------->    ")
    # done printing


    # move up
    if user_input == "w":
        up(grid)
        upAdd(grid)
    # move down
    elif user_input == "s":
        down(grid)
        downAdd(grid)
    # move left
    elif user_input == "a":
        left(grid)
        leftAdd(grid)
    # mvoe right
    elif user_input == "d":
        right(grid)
        rightAdd(grid)
    # skip turn
    else:
        attempt += 1
        continue
    # done movement


    # finding all Zero entries [0]
    rowIndexZero = []
    columnIndexZero = []
    for i in range(0,4):
        for j in range(0,4):
            if grid[i][j] == 0:
                rowIndexZero.append(i)
                columnIndexZero.append(j)
            if grid[i][j] == 2048:
                print "You're smarter than almost everyone, YOU WIN!!"
                break
    # placing next random 2
    if len(rowIndexZero) > 1:
        random_index = rowIndexZero.index(random.choice(rowIndexZero))
        newRowEntry = rowIndexZero[random_index]
        newColumnEntry = columnIndexZero[random_index]
        grid[newRowEntry][newColumnEntry] = 2
    elif len(rowIndexZero) == 1:
        newRowEntry = rowIndexZero[0]
        newColumnEntry = columnIndexZero[0]
        grid[newRowEntry][newColumnEntry] = 2
    else:
        break

print "Good job, you scored ", str(points), "points this game!"
print "\n\n"
print "Total attempts ----> ", str(attempts)
