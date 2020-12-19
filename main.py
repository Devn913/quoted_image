from edit_image import ImageEdit
from image_grab import ImageGrab
if __name__ == "__main__":
    print("welcome to Quote Image generator")
    print("Choose: \n 1 for random quote with image \n 2 for random image")
    user_input = int(input())
    if(user_input == 1):
        img = ImageEdit()
        img.run()
    elif(user_input == 2):
        no_of_image = 1
        no_of_image =  int(input("How many image you want to generate? (leave empty for default ) : "))
        if no_of_image > 20: no_of_image = 20
        for i in range(0 ,no_of_image):
            grabber = ImageGrab()
            grabber.random()
    else:
        print("please run again! Something went wrong....")

