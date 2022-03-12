# non-uniform-lowpass-filter

This code was used in a research project mention in https://ashleetiw.github.io/portfolio/ titled Deep Learning-Based Eye Gaze Estimation using Deflectometry Information in VR/AR/MR Headsets

## Radial convolution
Different filters are applied to different pixels based on the radial distance from the center.Convolution was implemented from scratch because all the library based convolution method is based on FFT which applies the kenel to the entire image.

This image shows the how the convolution is applied radially.Note that the colors represent different kernel size gaussian filters.

![rad](https://github.com/ashleetiw/non-uniform-lowpass-filter/blob/main/discrete.png)
All pixels which lie in the same circles have same filter being applied 



The relation between the size of the low pass filter applied to a pixel and it't radial distance is following
![rr](https://github.com/ashleetiw/non-uniform-lowpass-filter/blob/main/rr.png)
        
    
####   Kernel_size=F(radial_distance)

the function F is determined using an algorithm
![final](https://github.com/ashleetiw/non-uniform-lowpass-filter/blob/main/final.gif)


I used the non-uniform filter(pattern) to project on the eye. 
![eye](https://github.com/ashleetiw/non-uniform-lowpass-filter/blob/main/my-eye.png)



