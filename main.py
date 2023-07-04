import os
import cv2
import face_recognition

def encode_image(path:str):
    img = cv2.imread(path)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_encoding = face_recognition.face_encodings(rgb_img)[0]
    return img,img_encoding,path

def encode_all_images(path:str):
    arr = os.listdir(path)
    paths = [path+'/'+x for x in arr]
    print(paths)
    result = []
    for p in paths:
        result.append(encode_image(p))
    #print(result)
    return result

def compare_faces(path_image:str):
    img,img_encoding,path_visitor = encode_image(path_image)
    knowlegs = encode_all_images('./images/know')
    for image, encode, path_know in knowlegs: 
        result = face_recognition.compare_faces([encode], img_encoding,tolerance=0.45)
        print("Result: /n", result)
        print(face_recognition.face_distance([encode], img_encoding))
        print(path_know,path_visitor)
        if result[0]:
            cv2.imshow("visitor",img)
            cv2.imshow("result", image)
    #input("Press Enter to continue...")
    cv2.waitKey(1000)


    

if __name__ == "__main__":
    compare_faces("visitor.webp")