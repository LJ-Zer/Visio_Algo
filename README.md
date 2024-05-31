# Visio_Algo (Visio_Algorithm)

## The followiung branches are used to do a process of face cropped up to facial recognition.
VisioAccelerAI is a capstone project. Its main goal is to inference a facial recognition system into an FPGA board to boost the computational capability of the model to have its application of real-time attendance monitoring system. There are two main branches for this repository.

## Just follow the stepsfrom the README section of each branches

# Visio_Train
- This branch is a framework (files, scripts, dependencies) used to build and train a facial recognition model.

# Visio_Face
 - This branch is already a trained model to detect a face. It's main task is to extract faces in a frame and crop and save the cropped images in to a folder named "Visitor". This ensure the images we feed to our trained model is a face only. This process increase the accuracy of detecting facial recognition.
