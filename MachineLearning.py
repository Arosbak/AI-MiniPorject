from PIL import Image
import numpy as np
"""
an_Image = Image.open("Images/Charmander/Charmander.png")

imageS = an_Image.getdata()
image_Array = np.array(imageS)

print(len(image_Array))
print(image_Array[39005])
"""
len = 4                                                                                                                 #The number of pictures that will be put into the database

charmander = np.empty(shape=[len, 3, 1])                                                                                             #The array containing all the images with Carmander
mewtwo = np.array([])                                                                                                   #The array containing all the images with Mewtwo
pikachu = np.array([])                                                                                                  #The array containing all the images with Pikachu

for i in range(len):                                                                                                    #Loop one, going the through the number of images needed to be putted into the database
    top_folder = "Images/"                                                                                              #The name of the top folder that we importing the images from.
    sup_folder = ["Charmander", "MewTwo", "Pikachu"]                                                                    #The names of the subfolders we are importing the images from
    images = ["Charmander", "MewTwo", "Pikachu"]                                                                        #The namaes of the images we importing to the database
    types = ".png"                                                                                                      #The type the images is (jpg)
    for j in sup_folder:                                                                                                #Loop two, goinf through the subfolders
        if j == "Charmander":                                                                                           #If the subfolder is charmander
            if i == 0:                                                                                                  #If it is the first image in the foolder
                temp_path = top_folder + j + "/" + images[0] + types                                                    #Constructing the path to the folder
                temp_img = Image.open(temp_path)                                                                        #Opens the image at the constructed path
                temp_img_seq = temp_img.getdata()                                                                       #Getting the data from the image
                temp_img_array = np.array(temp_img_seq)                                                                 #Puts the data into an array
                charmander = np.append(charmander, temp_img_array[0])


                print(temp_img_array[0, 0])                                                                             #
                print(charmander[0,0])
                print(temp_img_array)
                print(temp_path)

                """
            else:
                temp_path = top_folder + j + "/" + images[0] + str(i) + types
                temp_img = Image.open(temp_path)
                temp_img_seq = temp_img.getdata()
                temp_img_array = np.array(temp_img_seq)
                charmander = np.append( charmander, temp_img_array, axis=0)
                print(charmander[1])
                print (temp_img_array)
                print(temp_path)
        elif (j == "MewTwo"):
            if i == 0:
                print(top_folder + j + "/" + images[1]+types)
            else:
                print(top_folder + j + "/" + images[1] + str(i) + types)
        elif (j == "Pikachu"):
            if i == 0:
                print(top_folder + j + "/" + images[2]+types)
            else:
                print(top_folder + j + "/" + images[2] + str(i) + types)
"""