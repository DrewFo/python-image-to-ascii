import pathlib
from PIL import Image

def ask_for_input():
    file_directory = input("Enter the absolute directory of the photo or video that you wish to convert: ") ##file_directory is the input
    file_extension = pathlib.Path(file_directory).suffix ##grabs the extension from the file path
    file_name = pathlib.Path(file_directory).name ##grabs the file name from the path
    success_message = f"File selected: \"{file_name}\" with a file extension of \"{file_extension}\"" ##confirms to the user the "selected" file
    print(success_message) ##prints message
    return file_directory

def make_frame_monochrome(directory):
    selected_image = Image.open(directory) ##loads the selected file as selected_image
    bw_image = selected_image.convert('L') #L is the pillow mode for black and white
    return bw_image

def convert_frame(bw_image, ascii_height):
    width,height = bw_image.size
    new_size = int(ascii_height * width/height), int(ascii_height)   #resizes the image based on ration of height(given) times ratio of width to height. Bigger height = more detail.
    shrunk_image = bw_image.convert('RGB')
    return shrunk_image.resize(new_size)

def convert_to_ascii(pre_ascii_image):
    character_types = ["▓▓", "▒▒", "░░","  "] #the space character doesn't fit the same on all browsers, also, for more detail, maybe, add more character types.
    ascii_output = ""
    for y in range(pre_ascii_image.size[1]): #loops through every pixel, adds a character based on its brightness to the output
        for x in range(pre_ascii_image.size[0]):
            red,green,blue = pre_ascii_image.getpixel((x,y))
            average = int((red + green + blue)/3)
            average = average/255
            if(average <= 0.25):
                ascii_output = ascii_output + character_types[0]
            elif(average > 0.25 and average <= 0.50):
                ascii_output = ascii_output + character_types[1]
            elif(average > 0.50 and average <= 0.75):
                ascii_output = ascii_output + character_types[2]
            else:
                ascii_output = ascii_output + character_types[3]
        ascii_output = ascii_output + "\n"
    return ascii_output

def whole_shebang(): ##this is where I make sense of everything (think of it as a 'main' method)
    directory_of_image = ask_for_input()
    ascii_height = int(input("Height of the ascii output? (30 is usually fine): "))
    monochrome_frame = make_frame_monochrome(directory_of_image)
    shrunk_bw_image = convert_frame(monochrome_frame,ascii_height)
    ascii_image = convert_to_ascii(shrunk_bw_image)
    print(ascii_image)

whole_shebang()