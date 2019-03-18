clear all; close all;

%Image Test Number User Input
Test = input([newline 'Which image will be used for testing? (1 - 5)' newline]);
croprec = [200 200 600 900];

% Reading Test Image
img = imread(['test_image' num2str(Test) '.jpeg']);
img = im2double(img);
img = imcrop(img,croprec);

% De-Blurring Image
Len = 6;
Theta = 10;
PSF = fspecial('motion', Len, Theta);
NoiseVar = 0.00001;
EstimatedNSR = NoiseVar/var(img(:));
DeBlur = deconvwnr(img, PSF, EstimatedNSR);

% Displaying De-Blurred and Hist Eq
figure;
subplot(1,4,1);
imshow(img);

subplot(1,4,2);
imshow(DeBlur);

subplot(1,4,3);
blurhist  = histeq(DeBlur);
imshow(blurhist);

subplot(1,4,4);
imghist  = histeq(img);
imshow(imghist);

% Applying Sobel Filter
figure;
imginv = imcomplement(imghist);
imshow(imginv);

figure;
subplot(1,2,1);
BW = imbinarize(imginv,'adaptive','ForegroundPolarity','bright','Sensitivity',0.48);
imshow(BW);

subplot(1,2,2);
BWOG = edge(imghist,'Sobel');
imshow(BWOG);

% Erode and Dilate
figure;
subplot(1,2,1);
SE1 = strel('disk',2);
EDimg = imerode(BW,SE1);
imshow(EDimg);
subplot(1,2,2);
SE2 = strel('rectangle',[10 6]);
EDimg = imdilate(EDimg,SE2);
imshow(EDimg);






