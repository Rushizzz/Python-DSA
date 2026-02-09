maze = [
    [1,0,0,0],
    [1,1,0,1],
    [0,1,0,0],
    [0,1,1,1]
]

maze2 = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,0]
]


def is_safe(maze, x, y):    
    if x >= 0 and x < len(maze) and y >= 0 and y < len(maze) and maze[x][y] == 1:
        return True

result = []

choices = ["u","d","l","r"]

def check_choice(maze,choice,x,y):
    if choice == "u":
        return is_safe(maze, x-1, y), x-1, y
    elif choice == "d":
        return is_safe(maze, x+1, y), x+1, y
    elif choice == "l":
        return is_safe(maze, x, y-1), x,y-1
    elif choice == "r":
        return is_safe(maze, x, y+1), x,y+1

def solve_maze(maze, x, y, destination):
    if destination == [x,y]:
        print("path found")
        print(result)
        return True
    else:
        for i in choices:
            safe, temp_x, temp_y = check_choice(maze,i,x,y)
            if safe:
                maze[x][y] = 0
                result.append([x,y])
                solve_maze(maze, temp_x, temp_y, destination)
    

        
solve_maze(maze2, 0, 0, [1,1] )

