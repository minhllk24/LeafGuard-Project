****** What is the purpose of each file? ******
TestImages: Images for testing model
AppShowcase.mp4: Show how the app work
LeafGuard.py: Create the UI for the app and run programn
Part1_LeafGuard_Preprocessing_Transfer-learning.ipynb: Transfer learning code, demonstrate how to train, and develop a predictive model
Part2_LeafGuard_Predict-Test-Evaluate Model.ipynb: For Model Testing and Prediction
model_plants_disease.h: The trained model that use for predicting
and other images files for the UI of the app

****** Instructions on how to install and run the software. *******
Firstly, download the LeafGuard-Project-main.zip file on Github: https://github.com/minhllk24/LeafGuard-Project

Secondly, extract the zip file to the location of your choice, the folder “AppCodesAndImages will appear there
Thirdly, open “AppCodesAndImages” folder, right click and choose Open in Terminal
Fourthly, type in command: 

	pip install Pillow numpy tensorflow keras_preprocessing opencv-python matplotlib

Finally, after the previous code has completed, open the “LeafGuard.py” and press F5 to launch the app. 

******   HOW TO RUN THE "LEAF NAME AND DISEASE IDENTYFYING APP"    ******

Step 1: Open the python file "LeafGuard.py" first, then press F5 or choose Start Debugging manually

Step 2: When the UI appear, Press the button "Start", wait for a few second, the "Upload Images" button will pop up

Step 3: Press "Upload Image" button, then choose your leaf image from your computer (the app can read *.jpg;*.jpeg;*.png; *.jfif image files)

Step 4: The notification will appear, meaning that you have successfully upload image, Press "OK" and the App will show you leaf name along with its disease and the accuracy percentage

Step 5: To choose another image, simply press the "Upload Image" button
