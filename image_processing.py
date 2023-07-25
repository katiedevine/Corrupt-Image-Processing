# Author: Katie Devine
# McGill ID: 260833077
# Assignment 4

import random
import numpy as np
import skimage.io as io

def denoise(filename):
#defining 'denoise()' as a function of one parameter.
    
    image_list = []
    #creating an empty list.
    
    for i in range(0, 20):
    #iterating over every image and appending it to the empty list.
        image = io.imread("{}_{}.png".format(filename[:-4], i))
        image_list.append(image)
    
    image_size = image_list[0].shape
    n_rows = image_size[0]
    n_cols = image_size[1]
    #getting the size of the image using '.shape'. and creating a variable for the height and width.
    
    blank_image = np.copy(image)
    #making a copy of the image to be edited.
    
    for i in range(0, n_rows):
        for j in range(0, n_cols):
            current_pixel = []
            #creating an empty list and adding each pixel in the same location for all images in the list 'image_list'. 
            #this list will be set back to empty before moving on to the next pixel.
            for each_image in image_list:
                current_pixel.append(each_image[i, j])
             
            red_list = [] 
            green_list = []
            blue_list = []
            #creating three empty lists for each color.
            
            for k in range(0, len(current_pixel)):
            #iterating over the pixel of each image and only adding it to the colou lists if it is not white.     
                
                if (current_pixel[k][0] == 255) and (current_pixel[k][1] == 255) and (current_pixel[k][2] == 255):
                    continue
                
                else:
                    red_list.append(current_pixel[k][0])
                    green_list.append(current_pixel[k][1])
                    blue_list.append(current_pixel[k][2])
                    #adding the RGB intensity value for each color to the corresponding list.
            
            if len(red_list) != 0:
            #getting the average of the red intensity value.
                avg_red = sum(red_list) / len(red_list)
            else:
            #done to prevent zero division (if red_list is empty).
                avg_red = sum(red_list) / 1
                
            if len(green_list) != 0:
            #getting the average of the green intensity value.
                avg_green = sum(green_list) / len(green_list)
            else:
            #done to prevent zero division (if green_list is empty).
                avg_green = sum(green_list) / 1
            
            if len(blue_list) != 0:
            #getting the average of the blue intensity value.
                avg_blue = sum(blue_list) / len(blue_list)
            else:
            #done to prevent zero division (if blue_list is empty).
                avg_blue = sum(blue_list) / 1
                     
            blank_image[i][j] = (avg_red, avg_green, avg_blue)
            #assigning each pixel of blank_image to the average of its RGB intensity values.
            
    return blank_image
    #returning the completed image, free of any noise.

def add_random_white_pixels(filename, whiteout_prob):
#defining 'add_random_white_pixels()' as a function of two parameters.
    
    image = io.imread(filename)
    blank_image = np.copy(image)
    #reading the file and creating a copy to be edited.
    
    image_size = image.shape
    n_rows = image_size[0] 
    n_cols = image_size[1]
    #getting the size of the image using '.shape'. and creating a variable for the height and width.
    
    random_array = np.random.random((n_rows, n_cols))
    #creating an array with the same dimensions as the image.
    
    for i in range(0, n_rows):    
         for j in range(0, n_cols):
            if random_array[i][j] <= whiteout_prob: 
                blank_image[i][j] = (255, 255, 255)
                #iterating over 'random_array' and comparing each value to 'whiteout_prob' (the probability value).
                #if the 'random_array' value is less than or equal to the 'whiteout_prob', it will be replaced with a white pixel.
                
            else:
                continue
                #if the 'random_array' value is greater than the 'whiteout_prob', it will remain as is. 
        
    return blank_image
    #returning the completed image, with white pixels added.
  
def add_white_regions(filename, num_regions):
#defining 'add_white_regions()' as a function of two parameters.
    
    image = io.imread(filename)
    blank_image = np.copy(image)
    #reading the file and creating a copy to be edited.
    
    image_size = image.shape
    n_rows = image_size[0] 
    n_cols = image_size[1]
    #getting the size of the image using '.shape'. and creating a variable for the height and width.
    
    max_region_size = [(n_rows/4), (n_cols/4)]
    max_region_rows = max_region_size[0] 
    max_region_cols = max_region_size[1]
    #creating variables maximum region dimensions, dependent on the height and width of the image.
    
    row_starts = []
    row_ends = []
    col_starts = []
    col_ends = []
    #creating empty lists for the start and end location for the rows and columns.
    
    for i in range(0, num_regions):
    
        random_row_start = int(random.randint(0, n_rows))
        random_col_start = int(random.randint(0, n_cols))
        #creating variables for the starting positions of each region, which will be randomized for any pixel of the image.
        
        random_row_end = int(random_row_start + random.randint(1, int(max_region_rows)))
        random_col_end = int(random_col_start + random.randint(1, int(max_region_cols)))
        #creating variables for the ending positions of each region (the starting positions plus a random value equal to or less than the maximum.
        
        row_starts.append(random_row_start)
        col_starts.append(random_col_start)
        #appending the starting positions to each list.
        
        if random_row_end < n_rows:
        #appending the ending positions to a list only if it does not exceed the bounds of the image.
            row_ends.append(random_row_end)
        else:
        #if the ending position does exceed the bounds of the image, we will append the end-most row position.
            row_ends.append(n_rows)
              
        if random_col_end < n_cols:
        #appending the ending positions to a list only if it does not exceed the bounds of the image.
            col_ends.append(random_col_end)
        else:
        #if the ending position does exceed the bounds of the image, we will append the end-most column position.
            col_ends.append(n_cols)
            
    for j in range(0, num_regions):
    #iterating over each region,
        blank_image[(row_starts[j]):(row_ends[j]), (col_starts[j]):(col_ends[j])] = (255, 255, 255)
        #replacing all of the pixels within the bounds of the region with white pixels.
        
    return blank_image
    #returning the completed image, with white regions added.
