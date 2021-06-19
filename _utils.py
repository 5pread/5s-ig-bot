from instabot import Bot
import pathlib, os, glob
import shutil

path = os.getcwd()
images_path = os.getcwd() + "\images"

def CheckImagesFile():  #check images dir exists or not
    if not os.path.exists("images"):
        os.makedirs("images")
        print('Cannot find images directory, so created one')
        return False
    else:
        return True

def clean_up():
    dir = "config"
    # checking whether config folder exists or not
    if os.path.exists(dir):
        try:
            # removing it so we can upload new image
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

def UploadPhoto(text_caption):
    for file in os.listdir(images_path):    #get image from /images directory
        pass
        clean_up()
        bot = Bot()
        bot.login(username="aipostingmemeslikeaboss", password="bruhmomentonumerodos")
        bot.upload_photo(images_path + f"/{file}", caption=f'{text_caption}')

def clean_imagesdir():
    for f in os.listdir(images_path):   #list all files in directory and return it
        os.remove(images_path+f"\{f}")





