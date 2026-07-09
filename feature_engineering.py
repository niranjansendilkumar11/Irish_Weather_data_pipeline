import os
import random
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array

# Folder containing healthy images
input_dir = "D:\Msc Artifical Intelligence\Semester 2\Deep Leaning\PlantVillage\Potato___healthy"

# Save augmented images here (same folder in this example)
output_dir = input_dir

# Number of images you want after augmentation
target_count = 1000

# Current images
images = [f for f in os.listdir(input_dir)
          if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

current_count = len(images)
needed = target_count - current_count

print(f"Current images: {current_count}")
print(f"Need to generate: {needed}")

# Augmentation settings
datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.15,
    height_shift_range=0.15,
    zoom_range=0.2,
    shear_range=0.15,
    horizontal_flip=True,
    brightness_range=[0.8, 1.2],
    fill_mode='nearest'
)

generated = 0

while generated < needed:

    img_name = random.choice(images)
    img_path = os.path.join(input_dir, img_name)

    img = load_img(img_path)
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)

    for batch in datagen.flow(
            x,
            batch_size=1,
            save_to_dir=output_dir,
            save_prefix="aug",
            save_format="jpg"):

        generated += 1

        if generated >= needed:
            break

print("Done!")
print(f"Generated {generated} new images.")