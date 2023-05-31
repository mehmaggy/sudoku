#Import modules
import pygame
import genrate_grid as gen
#Create the screen
screen = pygame.display.set_mode((500,600))
#Initialize the pygame font
pygame.font.init()
#Set the screen title
pygame.display.set_caption("SUDOKU SOLVER")
#initialize varaibles
x = 0
y = 0
dif = 500/9 
val = 0
#Create new sudoku puzzle
grid = gen.new_puzzle
#Load fonts for future use
font1 = pygame.font.SysFont("comicsans",40)
font2 = pygame.font.SysFont("comicsans",30)
def get_cord(pos):
    global x 
    x = pos[0]//dif
    global y
    y = pos[1]//dif
#Highlight the cell selected
def draw_box():
    for i in range(2):
        pygame.draw.line(screen,'red',(x*dif,(y+i)*dif),(x*dif+dif,(y+i)*dif),7)
        pygame.draw.line(screen,'red',((x+i)*dif,y*dif),((x+i)*dif,y*dif+dif),7)
#Enter value in the selected cell
def draw_val(val):
    text1 = font1.render(str(val),1,'blue')
    screen.blit(text1,(x*dif+20,y*dif+5))
def raise_error():
    text1 = font2.render("wrong",1,"red")
    screen.blit(text1,(50,510))
#Display instructions for the game
def instruction():
    text1 = font2.render("Enter value to solve the puzzle",1,"black")
    screen.blit(text1,(20,540))
#Solve the sudoku using backtracking algorithm
def solve(grid,col,row):
    while grid[col][row] != 0:
        if col < 8:
            col += 1
        elif col == 8 and row < 8:
            col = 0
            row += 0
        elif col == 8 and row == 8:
            return True
    pygame.event.pump()
    for it in range(1,10):
        if valid(grid,col,row,it) == True:
            grid[col][row] = it
            #Highlight the current cell while solving
            global x,y
            x = col
            y = row
            #Set white colored background
            screen.fill("white")
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid,col,row):
                return True
        else:
            grid[col][row] = 0
            #Set white colored background
            screen.fill("white")
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)
    return False
#Declare result
def result():
    text1 = font1.render("Finished",1,"green")
    screen.blit(text1,(20,560))
#Check if the value entered is valid
def valid(m,i,j,val):
    for it in range(9):
        if m[i][it] == val:
            return False
        if m[it][j] == val:
            return False
    it = i//3
    jt = j//3
    for i in range(it*3,it*3+3):
        for j in range(jt*3,jt*3+3):
            if m[i][j] == val:
                return False
    return True
#Function to draw grid lines for making sudoku
def draw():
    #Draw the lines
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                #Fill grid with default numbers
                text1 = font1.render(str(grid[i][j]),1,'black')
                screen.blit(text1,(i*dif+20,j*dif+5))
    for i in range(10):
        if i%3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen,'blue',(0,i*dif),(500,i*dif),thick)#Horizontal lines
        pygame.draw.line(screen,'blue',(i*dif,0),(i*dif,500),thick)#Verticle lines
run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0
#Initialize the loop that keeps the window running
while run:
    #White color background
    screen.fill('white')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #Get the mouse position from insert number
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        #Get the number to be inserted if key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-=1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x+=1
                flag1 = 1
            if event.key == pygame.K_UP:
                y-= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y+= 1
                flag1 = 1
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9
            if event.key == pygame.K_RETURN:
                flag2 = 1
    if flag2 == 1:
        if solve(grid,0,0) == False:
            error = 1
        else:
            rs = 1
        flag2 = 0
    if val != 0:
        draw_val(val)
        if valid(grid,int(x),int(y),val) == True:
            grid[int(x)][int(y)] = val
            flag1 =0
        else:
            grid[int(x)][int(y)] = 0
        val = 0
    if error == 1:
        raise_error()
    if rs == 1:
        result()
    draw()
    instruction()
    if flag1 == 1:
        draw_box()
    #Update window
    pygame.display.update()
#Quit pygame window
pygame.quit()