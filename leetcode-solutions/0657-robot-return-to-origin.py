class Solution:
    # pretty straightforward recursion
    def judgeCircle(self, moves):
        # Initialize robot's position at the origin (0,0).
        # x_position tracks horizontal movement, y_position tracks vertical movement.
        x_position = 0
        y_position = 0

        # Iterate through each move in the given sequence.
        for move in moves:
            if move == 'U':
                y_position += 1  # Move Up increases y-coordinate
            elif move == 'D':
                y_position -= 1  # Move Down decreases y-coordinate
            elif move == 'L':
                x_position -= 1  # Move Left decreases x-coordinate
            elif move == 'R':
                x_position += 1  # Move Right increases x-coordinate
        
        # After all moves, check if the robot is back at the origin (0,0).
        return x_position == 0 and y_position == 0
