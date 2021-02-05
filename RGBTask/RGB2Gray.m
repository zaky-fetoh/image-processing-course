%RGB to gray task 
im1 = imread('onion.png');

gray = MyRGB2Gray(im1 );
subplot(1,2,1) 
imshow( gray )
subplot(1,2,2) 
imshow(im1) 



function gray = MyRGB2Gray(im)
    red = im(:,:,1);
    green=im(:,:,2);
    blue =im(:,:,3);
    gray  = .29* red + .58*green + .11*blue; 
end

