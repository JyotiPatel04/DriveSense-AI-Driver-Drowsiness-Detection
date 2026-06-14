import tensorflow as tf
import os

print(" Script started...")

# Absolute path (VERY IMPORTANT FIX)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_PATH = os.path.join(BASE_DIR, "datasets")

print("Dataset path:", DATASET_PATH)
print("Exists:", os.path.exists(DATASET_PATH))

if not os.path.exists(DATASET_PATH):
    print(" DATASET FOLDER NOT FOUND")
    exit()

print("Folders inside dataset:", os.listdir(DATASET_PATH))

# Load dataset
train_data = tf.keras.preprocessing.image_dataset_from_directory(
    DATASET_PATH,
    image_size=(64,64),
    batch_size=32
)

print(" Dataset loaded successfully")

# Model
model = tf.keras.Sequential([
    tf.keras.layers.Rescaling(1./255),
    tf.keras.layers.Conv2D(32,3,activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64,activation='relu'),
    tf.keras.layers.Dense(2,activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print(" Starting training...")

model.fit(train_data, epochs=5)

print(" Saving model...")

model.save(os.path.join(os.path.dirname(__file__), "drowsiness_model.h5"))

print(" DONE")