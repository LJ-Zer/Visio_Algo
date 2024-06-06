# Visio_Train 
Credits to all the owners of the Scripts and Files especially to Google (TensorFlow). This document is only used for educational purposes. This folder will be used in Capstone Design for a Facial Recognition application. This repository contains the modified and easy access and execution of the documents, scripts, and file segregation, owner of this repository does not own any of the Python codes. If there are any, they are only used to automate the copying of files, and it is modified to fix the versioning of the Python libraries.

Still, I recommend to refer to the open source documentations of the TensorFlow for fix the errors based on your machine.

For this branch, VisioAccelerAI prepare this tutorial step by step using TensorFlow framework to train their facial recognition model. The following steps are crucial in development of a trained model from dependencies installation, datasets preparation, training and fine-tuning the model.

# SYSTEM REQUIREMENTS
	- Windows 10
	- Memory Space minimum of 100GB
	- Minimum 8GB RAM
	- Minimum 4GB VRAM

# Important! Dependencies of this Visio_Train repo, check for all compatabilities.
- python==3.9
- tensorflow==2.9
- conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
- pip install tensorflow-addons==0.19

# 1. Application Needed
	- VsCode 2017
	- Git for Windows
	- Nvidia Driver *if applicable
	- Miniconda
	- Cuda
	- Cudnn
	- Git Bash in VSCode

# 1.1. Installation of Cuda ToolKit and Cudnn
- https://developer.nvidia.com/cuda-11.2.0-download-archive
- https://developer.nvidia.com/rdp/cudnn-archive

# 1.2 Installation of Wget
- Download the latest wget.exe 
- Drag the wget.exe in C:\Windows\System32


***** REFERENCE: https://www.youtube.com/watch?v=-DurpWa3cGE&t=1s ***** 

# 2. Integrate Anaconda and VSCode
- Navigate the anaconda directory using
- *conda env list
- Copy the directory, in the terminal of VsCode
- *C:\Users\AI\miniconda3\Scripts\conda init
- *C:\Users\AI\miniconda3\Scripts\conda init powershell

***** REFERENCE: https://www.tensorflow.org/install/pip#windows-native ***** 

# 3. Create Virtual Environment in Anaconda (Git Terminal) 
- You can use Anaconda terminal or Vscode terminal if you already integrate Conda and VSCode
- *conda create --name Visio_Train python=3.9
- *conda activate Visio_Train

# 3.1 *NOT NEEDED as of 02/06/2024* Download Protobuf  
- Google drive link: 
- Unzip and put it in the Visio_Train directory

# 3.2 *NOT NEEDED as of 02/06/2024* Download the models folder 
- Google drive link:
- Unzip and put it in the Visio_Train directory

# 4. Installation of Cuda ToolKit and Cudnn 
- You can use Anaconda terminal or Vscode terminal if you already integrate Conda and VSCode
- *conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0

# 5. Installation of TensorFlow by using Pip
- You can use Anaconda terminal or Vscode terminal if you already integrate Conda and VSCode
- Update your pip first in latest version before installing tensorflow
- *pip install tensorflow==2.9

# 3. Run the 1_gpu-test.py
- Open VSCode Terminal. This code will confirm if the GPU can train your model.
- *python 1_gpu-test.py

# 4. *NOT NEEDED as of 02/06/2024* Edit the Compatible TensorFlow Version
- *python 2_tensorflow-ver.py

# 5. INSTALL ALL DEPENDENCIES
- Open VSCode Terminal. This script will run dependencies. Check the scripts for proper compatability "https://github.com/tensorflow/addons".
- Change the directory of the protoc 
- *source A_dependencies.sh

# 6. Dependencies Checker
- This script will check the dependencies, expect output must print "OK".
- *source B_dependencies-checker.sh

# 7. DATASETS PREPARATION
- Edit the content of this script.
- This script prepare datasets such as, directories, copying of the images, labelmap.txt, creation of csv, tfrecord.
- FIRST! you must input your datasets in a folder named "images" in main home folder. Datasets must augmented and labeled already.
- Edit the class name.
- *source C_datasets-prep.sh

# 8. Model File Configuration
- This script will download the tar.gz file of the chosen model, just uncomment the model you wanted to.
- *source D_model-config.sh

# 9. Configuration Script
- This is very important to execute, this will dictate everything before the training process.
- Go to models/mymodels
- Open the 4_custom-config.py
- Edit the parameters needed (num_steps, chosen_model, num_classes, batch_size)
- Save the 4_custom-config.py
- Go back to the main directory
- Execute the script
- *source E_configuration-file.sh

# 10. Training
- Run the training in outside terminal or in VSCode Terminal using one line code
- Reduce the actual batch_size in pipeline_file.config into "4" to prevent OOM ("Out of Memory"). This is only optional reduce the batch_size from "132" to "64". 
- go to models/mymodel 
- open 4_custom-config.py
- edit the parameters (num_steps, chosen_model, num_classes, batch_size)
- in pipeline_file.config change the fine_tune_checkpoint to "models/mymodel/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/checkpoint/ckpt-0"
- I suggest to run the python command inside the F_training.sh in the conda terminal.
- *source F_training.sh

# 11. Conversion into TF-Lite 
- This script will create folder "custom_model_lite", this folder will be use for the repository of the converted files and for inferencing.
- just open the script, and edit the "python 3_tflite-converter.py" which is located at the main directory.
- Edit the directories needed for the files.
- Also, this will download the python code for inferencing video, image, stream and webcam.
- Now it is ready for inferencing. Check the READme.txt for inferencing.
- Optional, you can check the mAP calculation, proceed to the next step.
- *source G_convert-tflite.sh

# 12. MAP (Mean Average Precision) Calculation
- Google mo nalang meaning at yung results
- This script will allow to calculate the precision of your Unquantized trained model yung mAP.
- In your 'images/train' directory to prevent an error, choose atleast get 40% of the images in that folder and delete the 60%. 
- If this script prints 'Error. File not found: =name.txt', lessen your test images.
- Check 4_mAP.py for directories.
- *source H_map.sh

# 13. (OPTIONAL !!) Quantization and Calculation of MAP of the Quantized Model
- Since our model save into 32 bits, we can quantize it to run it more faster in small edge devices and convert it into 8 bits. 
- Keep your custom_model_lite in your main directory.
- Edit the 5_quantization.py file to correct its directories.	
- Check the images/test-quan directory if the same the number of the images from datasets.
- This script will test the quantized model first before calculating the mAP values.
- Check the '5_quantization-mAP.py' for the directories.
- *source I_quantization-map.sh

# 14. FROM STEP 11, YOU CAN NOW INFERENCE FROM THAT, YOU CAN SKIP STEPS 12-13
- NOW, you're ready for inferencing.
- For inferencing, refer to your main directory and go to the "custom_model_lite" folder.
- From that you can open conda terminal, git bash, or CMD with conda enable.
- Activate the conda environment you use.
- For inferencing your QUANTIZED MODEL, just change the all of the variables 'detect.tflite' into 'detect_quant.tflite' inside the 'TFLite_detection_webcam.py'. 

- *To use you quantize model* From the main directory of Visio_Train run:
- *conda activate Visio_Train
- *python custom_model_lite/TFLite_detection_webcam.py --modeldir=custom_model_lite
- *FOR QUANTIZED MODEL ITS FINE NOT TO DO THE INSTRUCTION ABOVE* 
- *python custom_model_lite/quan_TFLite_detection_webcam.py --modeldir=custom_model_lite
  
# 15. Measuring the GOPS of the trained model
- *python 3_tflite-converter.py
