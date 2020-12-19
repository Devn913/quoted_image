from os import error
import requests
import datetime

class ImageGrab:

    def unsplash(self):
        api = "https://source.unsplash.com/1000x1000/?random,workout,cars,scene,landscape"
        while True:
            try:
                req =  requests.get(api)
            except:
                print("Something went wrong!")
                pass
            else:
                break

        file = open("now.png", "wb")
        file.write(req.content)
        file.close()
        return True
    
    def random(self):
        api = "https://source.unsplash.com/1000x1000/?random"
        while True:
            try:
                req = requests.get(api)
            except:
                print("Something went wrong!! Trying Again")
                pass
            else:
                break
        now = datetime.datetime.now()
        now = now.strftime("%Y_%m_%d_%H_%M_%S_%f")
        file = open("generated_image/" + str(now) + ".png","wb")
        file.write(req.content)
        file.close()
        print("Generated")
        return True
        
        
