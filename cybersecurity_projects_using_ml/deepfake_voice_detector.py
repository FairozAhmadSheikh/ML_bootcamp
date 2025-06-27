# pip install librosa numpy matplotlib scikit-learn tensorflow
import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, TimeDistributed, LSTM, Dense, Flatten, Dropout


def extract_features(file_path, max_len=128):
    try:
        y, sr = librosa.load(file_path, sr=16000)
        mel_spec = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=64)
        log_mel_spec = librosa.power_to_db(mel_spec, ref=np.max)
        if log_mel_spec.shape[1] < max_len:
            pad_width = max_len - log_mel_spec.shape[1]
            log_mel_spec = np.pad(log_mel_spec, ((0, 0), (0, pad_width)), mode='constant')
        else:
            log_mel_spec = log_mel_spec[:, :max_len]
        return log_mel_spec
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None
def load_dataset(fake_dir, real_dir, max_files=100):
    X, y = [], []
    for file in os.listdir(fake_dir)[:max_files]:
        features = extract_features(os.path.join(fake_dir, file))
        if features is not None:
            X.append(features)
            y.append(1)  # fake
     for file in os.listdir(real_dir)[:max_files]:
        features = extract_features(os.path.join(real_dir, file))
        if features is not None:
            X.append(features)
            y.append(0)  # real

    return np.array(X), np.array(y)
def build_model(input_shape):
    model = Sequential([
        tf.keras.layers.Reshape((input_shape[1], input_shape[0], 1), input_shape=input_shape),
        Conv2D(32, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        tf.keras.layers.Reshape((-1, 64)),  # flatten spatial into time steps
        LSTM(64),
        Dense(64, activation='relu'),
        Dropout(0.3),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train(fake_dir, real_dir):
    print("Loading dataset...")
    X, y = load_dataset(fake_dir, real_dir)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = build_model(input_shape=X_train.shape[1:])
    model.fit(X_train, y_train, epochs=10, batch_size=16, validation_split=0.1)

    preds = (model.predict(X_test) > 0.5).astype(int)
    print("\nClassification Report:\n", classification_report(y_test, preds))

if __name__ == "__main__":
    # Replace with actual folders
    FAKE_AUDIO_DIR = "fake_audio/"
    REAL_AUDIO_DIR = "real_audio/"
    
    train(FAKE_AUDIO_DIR, REAL_AUDIO_DIR)