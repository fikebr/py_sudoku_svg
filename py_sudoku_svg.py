import drawsvg as draw
from sudoku import Sudoku

def main():
    canvasSize = 300
    d = draw.Drawing(canvasSize+4, canvasSize+4, origin=(0,0))
    cubeSize = canvasSize/9
    puzzle = getPuzzle(0.5)
    drawPuzzle(d, puzzle, cubeSize)
    draw3x3(d, cubeSize)

    d.save_svg('grid_num.svg')

def drawPuzzle(d, puzzle, cubeSize):
    for col in range(0, 9, 1):
        for row in range(0, 9, 1):
            [x1, y1] = getCoords(row, col, cubeSize)
            #print('x{0}, y{1} = {2},{3}'.format(row, col, x1, y1))
            drawCube(d, x=x1, y=y1, size=cubeSize, strNumber=puzzle[row][col])

def draw3x3(d, cubeSize):
    for col in range(0, 3, 1):
        for row in range(0, 3, 1):
            [x1, y1] = getCoords(row, col, cubeSize*3)
            d.append(draw.Rectangle(x1, y1, cubeSize*3, cubeSize*3, fill='none', stroke='black', stroke_width=4))

def getCoords(row, col, cubeSize):
    x1 = int(col*cubeSize)
    y1 = int(row*cubeSize)
    return([x1, y1])

def getPuzzle(difficulty=0.5):
    puzzle = Sudoku(3).difficulty(difficulty)
    # puzzle.show()
    return(puzzle.board)

def drawCube(d, x=10, y=10, size=40, strNumber='0'):
    d.append(draw.Rectangle(x, y, size, size, fill='none', stroke='black'))

    if (strNumber == None):
        strNumber = ""

    cx=x+(size/2)
    cy=y+int(size/10)+(size/2)
    d.append(draw.Text(str(strNumber), font_size=size-10, x=cx, y=cy, text_anchor='middle', dominant_baseline='middle'))

if __name__ == "__main__":
	main()
