import base64
from PIL import Image
from io import BytesIO
import glob

# TAKE PATH THAT WANT TO SAVE IMAGES
Convert_path = input('where you wanna SAVE it? ')
Save_path = Convert_path + '\\'

# E:\IMAGES

# TAKE PATH THAT IMAGES IN THERE
img_path = input('where is your images? ')

# E:\CONVERTTOBS64

# RECOGNIZE THAT LIST IS EMPTY OR NOT AND CHECK PNG FORMAT
image_list = img_path + '/*.PNG'
Final_list = glob.glob(image_list)



for filename in Final_list:

    with open(filename, "rb") as image_file:
        data = base64.b64encode(image_file.read())
    
    filenames = filename.replace(img_path, ' ')
    Final_Names_Change = filenames.replace(' \\', '')
    # print(Final_Names_Change)

    im = Image.open(BytesIO(base64.b64decode(data)))
 
    im.save(Save_path+Final_Names_Change, 'PNG')
    print(Save_path+Final_Names_Change, 'it\'s done')
    



