# Visio_Algo (Visio_Algorithm)
VisioAccelerAI is a capstone project. Its main goal is to inference a facial recognition system into an FPGA board to boost the computational capability of the model to have its application of real-time attendance monitoring system. There are two main branches for this repository. The following branches are used to process face cropping up to facial recognition.

# Inferencing this both of trained model in SBC (RPi, Jetson Nano, Linux OS)
- Install Anaconda Environment
- Instruction: https://phoenixnap.com/kb/install-anaconda-ubuntu

# Just follow the steps from the README section of each branches!

## Visio_Train
- This branch is a framework (files, scripts, dependencies) used to build and train a facial recognition model.

## Visio_Face
 - This branch contains a trained model to detect faces. Its main task is to extract faces from a frame, crop them, and save the cropped images into a folder named 'Visitor.' This ensures that the images fed to our trained model contain only faces, which increases the accuracy of facial recognition.

##### Working as of 02/06/24
