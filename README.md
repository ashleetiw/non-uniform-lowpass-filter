# non-uniform-lowpass-filter

This code was used in a research project mention in https://ashleetiw.github.io/portfolio/ titled Deep Learning-Based Eye Gaze Estimation using Deflectometry Information in VR/AR/MR Headsets

## Radial convolution
Different filters are applied to different pixels based on the radial distance from the center.Convolution was implemented from scratch because all the library based convolution method is based on FFT which applies the kenel to the entire image.

This image shows the how the convolution is applied radially.Note that the colors represent different kernel size gaussian filters.

![rad](https://github.com/ashleetiw/non-uniform-lowpass-filter/blob/main/discrete.png)
All pixels which lie in the same circles have same filter being applied 


The relation between the size of the low pass filter applied to a pixel and it't radjial distance is following
![rr](https://github.com/ashleetiw/non-uniform-lowpass-filter/blob/main/rr.png){: width="600"}

*https://www.researchgate.net/figure/When-computing-a-subpixel-Gaussian-the-continuous-distance-between-Gaussian-center-and_fig1_221415389*

the function F is determined using an algorithm
![final](https://github.com/ashleetiw/non-uniform-lowpass-filter/blob/main/final.gif)
        
    
####   Kernel_size=F(radial_distance)

![pp](https://github.com/ashleetiw/non-uniform-lowpass-filter/blob/main/pattern.png)


I used the non-uniform filter(pattern) to project on the eye
![eye](https://github.com/ashleetiw/non-uniform-lowpass-filter/blob/main/my-eye.png)


## References

1:[https://www.sciencedirect.com/science/article/abs/pii/S0143816618300599](https://www.sciencedirect.com/science/article/abs/pii/S0143816618300599)
2:[https://3dim.northwestern.edu/JWang_COSI_2021.pdf](https://3dim.northwestern.edu/JWang_COSI_2021.pdf)



