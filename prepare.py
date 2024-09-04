import os
import numpy as np
from facenet_pytorch import InceptionResnetV1, MTCNN
import torch
import cv2
import os

mtcnn = MTCNN(keep_all=True)
model = InceptionResnetV1(pretrained='vggface2').eval()

def load_images_from_folder(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        img_path = os.path.join(folder_path, filename)
        img = cv2.imread(img_path)  # Đọc ảnh bằng OpenCV
        if img is not None:
            images.append(img)
    return images

def get_face_embeddings(image):
    # OpenCV đọc ảnh ở dạng BGR, chuyển đổi thành RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_tensor = torch.from_numpy(image_rgb).float()
    faces = mtcnn(image_tensor)
    embeddings = []
    if faces is not None:
        for face in faces:
            face_embedding = model(face.unsqueeze(0))
            face_embedding_after_detach=face_embedding.detach()
            embeddings.append(face_embedding_after_detach.numpy().flatten())
    return embeddings

def create_and_save_embeddings(base_folder, output_folder):
    print("running")
    all_embeddings = []
    labels = []
    for person_folder in os.listdir(base_folder):
        person_folder_path = os.path.join(base_folder, person_folder)
        if os.path.isdir(person_folder_path):
            images = load_images_from_folder(person_folder_path)
            output_file=os.path.join(output_folder, person_folder)+".npz"
            if not os.path.exists(output_file):
                print(output_file)
                all_embeddings = []
                labels = []
                for img in images:
                    face_embeddings = get_face_embeddings(img)
                    all_embeddings.extend(face_embeddings)
                    labels.extend([person_folder] * len(face_embeddings))
                np.savez(output_file, embeddings=np.array(all_embeddings), labels=labels)


    
if __name__ == "__main__":
    create_and_save_embeddings("Vggnet/Image_data/data_jpg","Vggnet/Out_put_embedding")
    
