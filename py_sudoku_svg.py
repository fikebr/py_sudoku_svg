import drawsvg as draw
from sudoku import Sudoku
import argparse
import os

def main():
    args = getArgs()
    print('folder = {0}, file = {1}, cwd = {2}'.format(args.folder, args.file, os.path.split(__file__)[0]))

    canvasSize = args.size
    cubeSize = canvasSize/9

    puzzle = getPuzzle(args.difficulty)

    d = draw.Drawing(canvasSize, canvasSize, origin=(0,0))
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

def getArgs():

    parser = argparse.ArgumentParser(
                    prog='Sudoku Builder',
                    description="Build Sudoku puzzle files in bulk.",
                    epilog='Thank you.')

    parser.add_argument('-o', '--output', type=str, help='Output filename. The name will be given a prefix of "001_"', required=True)
    parser.add_argument('-n', '--number', type=int, help='The Number of files to create.', default=1)
    parser.add_argument('-z', '--size', type=int, help='The size in pixels of the puzzle.', default=200)
    parser.add_argument('-d', '--difficulty', type=int, help='The diffuculty of the puzzle. 1=easy, 2=med, 3=hard.', default=2, choices=[1, 2, 3])
    parser.add_argument('-t', '--template', type=str, help='The png file to use as a template to place your puzzle in.')
    parser.add_argument('-c', '--coords', type=str, help='Coordinates where to place the puzzle in the template image. Format 20x20.', default='20x20')

    args = parser.parse_args()

    DIFFICULTIES = [0, 0.3, 0.5, 0.8]
    args.difficulty = DIFFICULTIES[args.difficulty]

    (args.folder, args.file) = getOutput(args.output)

    return(args)

def getOutput(output):
    (folder, file) = os.path.split(os.path.abspath(output))
    # print('folder = {0}, file = {1}, cwd = {2}'.format(folder, file, os.path.split(__file__)[0]))
    os.makedirs(folder)
    return(folder, file)

if __name__ == "__main__":
	main()
