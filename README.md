# Corrupt-Image-Processing

# Prolouge:
During a recent routine security audit of the network access logs of the MacGill University 
Astro- physics Group, an unusual remote access was found. Someone using the handle ‘Dr M. Artian’ 
had telnetted to the servers in the middle of the night, used the lab’s VPN to connect to the 
Hubble Space Telescope, and directed the telescope to take twenty (20) photographs of regions at 
three different spatial coordinates.

Investigators were able to retrieve the photographs, which were heavily corrupted, as shown in 
Figure 1. Denoising algorithms were run to restore the images (see Figure 2). Our task is to confirm 
that the denoising algorithms were correct by writing our own implementation of denoising algorithms, 
in addition to writing algorithms to add noise to an image.

# Types of Noise:
The images retrieved by the investigators had three different types of noise or corruption.

  - First, due to the distance of the spatial regions from the Earth, the photographs are grainy and 
    noisy (the light from distant stars, nebula and other objects in the sky is very dim when it finally 
    arrives here on Earth). This phenomenon results in various color components of various pixels being 
    distorted.
    
  - Secondly, in some images, random pixels have turned completely white. See Figure 1b.
    
  - Finally, some images could only be partially retrieved, with many regions of white pixels
    obscuring different areas of the image.

# Task (Part One)
Our first task in this question is to take the batch of 20 photographs for each of the three spatial 
regions and reconstitute the original photograph from that batch, removing the noise and regions of 
white pixels. To do so, we will use a technique called image stacking.

Image stacking is a process where we take the average over a batch of images. Specifically, we will 
create a new image where each pixel at a position (x, y) in the image is the average of all pixels at 
the same position (x, y) in each of the N images of the batch:

<img width="257" alt="Screenshot 2023-07-25 at 5 10 17 PM" src="https://github.com/katiedevine/Corrupt-Image-Processing/assets/140209312/c39b5a3a-fe00-47a5-9cad-5fa4a8f89746">

The (xstacked,ystacked) in the formula refers to a list of three color components, since as discussed in 
class each pixel is represented by three components. By applying this image stacking process, we can reduce 
the noise in our images. For example, by combining the photograph seen in Figure 1a with the 19 other versions 
of the same image, we can obtain a result as seen in Figure 2a. However, we must go further in order to reduce 
the impact of the white pixels and regions seen in Figures 1b and 1c. We can do so by making the assumption that 
any fully-white pixel (a pixel of 255 in all color components) is a noisy pixel, and thus should not be included 
when calculating the average of a pixel. That is, while iterating over each of the 20 versions of a photo and 
taking the average of each pixel, we will skip a pixel if it has the intensity (255, 255, 255). We must also 
take care when dividing by N to decrease the value of N for every white pixel for that location (x, y) 

(e.g., if 5 of the 20 versions had a fully-white pixel for a location (x, y), then when calculating the average 
pixel for that location, we must divide by 15 instead of 20). By extending our image stacking process in this way, 
the white pixels and regions seen in Figures 1b and 1c can be removed, and we will be able to recover the original 
images, as seen in Figures 2b and 2c.

You will write this image stacking process in a function as follows:

Name: denoise

Parameters: A filename corresponding to an image (e.g., bubble nebula.png). Note: The batches for each photo have 
the filename image name N.png, where N is a number in the range [0, 19] (inclusive). You will have to modify the 
filename variable to insert one at a time each value in the range, so that you can load in the 20 different files 
of the batch. (Depending on how you implement your image stacking process, you can load one file at a time, or load 
all files at once.)

Return value: A NumPy array corresponding to the denoised image as per the instructions above (i.e., using the image 
stacking process to average out noisy pixels and white regions).

# Task (Part Two)
In this part of the question, we will write code that does the reverse of the above, i.e., add noise to an image, in 
the form of white pixels and white regions. We will define two functions to do this.

1. add random white pixels

Parameters: A filename corresponding to an image (e.g., bubble nebula final.png), and a floating point number whiteout 
prob corresponding to the probability of a pixel being turned white. (Note: The image filename given in the testing code
will not exist until you finish your denoise function and produce the final, denoised image.)

Return value: A NumPy array of the image with random pixels turned white (255, 255, 255), with the probability of any 
pixel turning white given by the function parameter. The randomization must be done using np.random.random function. 

2. add white regions

Parameters: A filename corresponding to an image (e.g., bubble nebula final.png) and an integer num regions specifying 
how many random white regions should be created.

Return value: A NumPy array of the image with the given number of white regions created. Each region should have a 
random height and width and start at a random position in the image. The minimum height and width of a region is 1. 
The maximum height and width of a region is the size of the image’s length in that dimension divided by 4. 

E.g., if the image has shape [1000, 800], then the region’s height should be in the range [1, 1000//4], and the region’s 
width should be in the range [1, 800//4]. All pixels in a region must be turned white. Note: It’s OK if a region has a 
starting coordinate that places some of the region out of the bounds of the image (as long as it doesn’t cause an error). 
It’s also OK if regions overlap each other.
