import os
import numpy as np
from facenet_pytorch import InceptionResnetV1, MTCNN
import torch
import cv2
from scipy.spatial.distance import cosine
import pickle
MAGE_HEIGHT = 112
IMAGE_WIDTH = 92
mtcnn = MTCNN(keep_all=True)
model = InceptionResnetV1(pretrained='vggface2').eval()
def get_face_embeddings(image_tensor):
    faces= mtcnn(image_tensor)
    embeddings = []
    if faces is not None:
        for face in faces:
            face_embedding = model(face.unsqueeze(0))
            face_embedding_after_detach=face_embedding.detach()
            embeddings.append(face_embedding_after_detach.numpy().flatten()) #chuyen thanh numpy array co chieu (512,) roi add vao embeddings
    return embeddings

def load_embeddings(file_path):
    data = np.load(file_path)
    return data['embeddings'], data['labels']

def xulyanh(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_tensor = torch.from_numpy(image_rgb).float()
    return image_tensor
def identify_face(face_embedding, known_embeddings, known_labels, threshold=0.4):
    distances = [cosine(face_embedding, known_embedding) for known_embedding in known_embeddings]
    # distances luu do tuong tu giua 2 vector co chieu la 512
    mean_distance = np.mean(distances)
    return True if mean_distance < threshold else False
    

def recognize_faces(image, known_embeddings_file):
    # Tải embeddings đã lưu
    print
    known_embeddings, known_labels = load_embeddings(known_embeddings_file)
    if image is not None:
        image=xulyanh(image)
        faces_embedning = get_face_embeddings(image)
        if faces_embedning:
            return identify_face(faces_embedning[0],known_embeddings,known_labels)

    