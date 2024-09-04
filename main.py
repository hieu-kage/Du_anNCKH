import cv2
import predict
import os

def main():
    if __name__ == "__main__":
        path="Vggnet/Out_put_embedding"
        masv=(input("Nhap vao ma sinh vien de so sanh"))+".npz"
        path=os.path.join(path,masv)
        cap = cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)
        while True:
            success, img = cap.read()
            imgS = cv2.resize(img, (192, 0), None, 0.25, 0.25)
            # cvzone.cornerRect(imgBackground,(270, 300, 190, 250), rt=0)  # vẽ boxq
            print(predict.recognize_faces(imgS,path))
            # if predict.recognize_faces(path,imgS):
            #     print("Chinh Xac")
            # else :
            #     print("Khong chinh xac")
                
                    # cv2.putText(imgBackground,results, (x1 + 55, y2 + 172), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
                            
            cv2.imshow("Face Attendance", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
if __name__=="__main__":
    main()