import numpy as np
from tensorflow import keras
from keras_preprocessing import image
import cv2
import os
from tensorflow.keras.models import load_model
import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.efficientnet import EfficientNetB0, preprocess_input

class LeafDiseaseDetector:
    def __init__(self, root, model, class_labels):
        self.root = root
        self.model = model
        self.class_labels = class_labels
        self.imported_image_path = None
        self.add_import_button()

    def add_import_button(self):
        # Adds an Import Image button to the UI
        import_button = tk.Button(
            self.root, 
            text="Import Image", 
            command=self.import_image,
            bg='#ADD8E6',
            font=("Arial", 12)
        )
        import_button.pack(pady=30)

    def import_image(self):
        # Allows the user to select an image file and stores its path
        self.imported_image_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.jfif")]

        )
        if self.imported_image_path:
            messagebox.showinfo("Image Imported", f"Image imported successfully: {self.imported_image_path}")
            # Call detect_leaf_disease function after importing image
            self.detect_leaf_disease(self.imported_image_path, self.model, self.class_labels)
        else:
            messagebox.showinfo("Import Cancelled", "No image selected.")

    def detect_leaf_disease(self, filepath, model, class_labels):
        """
        Detect leaf disease from an image file using a pretrained EfficientNetB0 model.
        """
        try:
            # Load and display the image in PIL format
            original = load_img(filepath, target_size=(224, 224))
            print('PIL image size:', original.size)
            plt.imshow(original)

            # Convert the image to a numpy array
            numpy_image = img_to_array(original)
            print('Numpy array size:', numpy_image.shape)
            plt.imshow(np.uint8(numpy_image))

            # Expand the dimensions of the image to batch format
            image_batch = np.expand_dims(numpy_image, axis=0)
            print('Image batch size:', image_batch.shape)
            plt.imshow(np.uint8(image_batch[0]))

            # Preprocess the image for the model
            processed_image = preprocess_input(image_batch.copy())

            # Get the predicted probabilities for each class
            predictions = model.predict(processed_image)

            # Get the top 5 predictions
            top_indices = np.argsort(predictions[0])[::-1][:5]
            top_labels = [(class_labels[i], predictions[0][i]) for i in top_indices]

            # Display the top predicted label with probability
            full_label = top_labels[0][0]  # e.g., 'Corn_(maize)___Common_rust'
            probability = top_labels[0][1]  # Probability (e.g., 0.85)

            leaf_label, disease_label = full_label.split('___')

            title = f"Leaf: {leaf_label}, Diseased: {disease_label}, Probability: {probability:.4f}"

            # Create the Matplotlib plot
            plt.imshow(original)
            plt.title(title)
            plt.show()

        except Exception as e:
            print(f"Error processing the image: {e}")

    def run(self):
        # Runs the main Tkinter loop
        self.root.mainloop()

# Example usage
if __name__ == "__main__":
    root = tk.Tk()

    # Assume you have a trained model and class labels available
    model = load_model('model_plant_disease.h5')  # Replace the file path of the model to your file location
    class_labels = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']
    # Replace with your class labels

    app = LeafDiseaseDetector(root, model, class_labels)
    app.run()
