import cv2
import img_sudoku as img
from sudoku_solver import Sudoku
import text_to_speech as tts

original = cv2.imread('screenshots/ss1.jpg', cv2.IMREAD_GRAYSCALE)

pre_processed = img.pre_process_image(original)

corners = img.find_corners(pre_processed)

cropped = original[corners[0][1]:corners[2][1], corners[0][0]:corners[2][0]]

final_image = img.get_final_image_from_cropped_image(cropped)

grid = img.extract_number(final_image)
#print(grid)
Sudoku().print_sudoku_from_list(grid)

yn = input('looks good? (y/n): ')
if yn == 'y':    
    solved = Sudoku().solve_sudoku(grid)
    solved = [str(n) for n in solved]
    joined = ' ... '.join(solved)
    print(joined)
    tts.speak_text(joined)
else:
    print('Back to the drawing board ..')