class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.height = height
        self.width = width
        self.food = food
        self.score = 0
        self.path = [[0,0]]
         #this will act like a queue for the snake body. It always starts from 0,0        
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        head  = self.path[0]        #We find the next position where head of the snake moves. Head is always first in the queue
        if direction == 'U':
            new_head = [head[0]-1, head[1]]
        elif direction == 'D':
            new_head = [head[0]+1, head[1]] 
        elif direction == 'R':
            new_head = [head[0], head[1] + 1]
        elif direction == 'L':
            new_head = [head[0], head[1] - 1]
        
        if self.path and new_head in self.path:
            if self.path[-1] != new_head:
                return -1
            
        if new_head[0] == -1 or new_head[0] == self.height or new_head[1] == -1 or new_head[1] == self.width:
            return -1
        
        self.path.insert(0,new_head)
        if self.food and new_head == self.food[0]:
            self.food.pop(0)
            self.score += 1
        else:
            self.path.pop()
        return self.score

        

        
                
            #If next location is already occupied by its body and that part is before tail, then it bites itself and it's a game over
            
