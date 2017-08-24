#importing from image library
from PIL import Image
#RGB values for recoloring oncoe we know the intensity.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)
#import image.
my_image = Image.open ("babka.jpg") #finds image on comp
image_list = my_image.getdata() #finds the rgb value of every picture--> basically get data means it will get the rgb values
image_list = list(image_list) #takes the rgb values and makes it a list

recolored = [] #list that will hold the pixel data for the new image
    #a pixel is a list
for pixel in (image_list):
    #find the intensity
    intensity = pixel[0] + pixel[1] + pixel[2] #do this because using the index to take the value of each place holder in the list and the r is in the zero index green is in the 1 index and blue is in the 2 index
    #compare intensity to the values in student pormpt
    if intensity <= 182:
        pixel = darkBlue
    if intensity > 182 and intensity <= 364:
        pixel = red
    if intensity > 364 and intensity <= 546:
        pixel = lightBlue
    if intensity > 546:
        pixel = yellow

    #assign a new color to the pixel based on intensity
    recolored.append(pixel)

#create a new image using the recolored list. Display and save the image
new_image = Image.new ("RGB", my_image.size) #creates a new image that will be the same size as the original image
new_image.putdata(recolored) #adds the data from the recolored list to the image
new_image.show() #show the new image on the screen
new_image.save ("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
