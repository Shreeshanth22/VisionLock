from tkinter import *
from PIL import Image,ImageTk
import cv2
import os

# Import OpenCV2 for image processing
# Import os for file path
import cv2
import os

# Import numpy for matrix calculation
import numpy as np

# Import Python Image Library (PIL)
from PIL import Image

# Create Local Binary Patterns Histograms for face recognization
##recognizer = cv2.face.createLBPHFaceRecognizer()

recognizer = cv2.face.LBPHFaceRecognizer_create()

# Using prebuilt frontal face training model, for face detection
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

# Create method to get the images and label data
def getImagesAndLabels(path):

    # Get all file path
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
    
    # Initialize empty face sample
    faceSamples=[]
    
    # Initialize empty id
    ids = []
    ids_names = []
    # Loop all the file path
    for imagePath in imagePaths:

        # Get the image and convert it to grayscale
        PIL_img = Image.open(imagePath).convert('L')

        # PIL image to numpy array
        img_numpy = np.array(PIL_img,'uint8')

        # Get the image id
        name = os.path.split(imagePath)[-1].split(".")[0]
        id = int(os.path.split(imagePath)[-1].split(".")[1])

##            # Add the image to face samples
        faceSamples.append(img_numpy)#[y:y+h,x:x+w])

            # Add the ID to IDs
        ids.append(id)
        ids_names.append([id, name])
        
    # Pass the face array and IDs array
    return faceSamples,ids,ids_names



win=Tk()
win.title("FAC RECOGNITION SYSTEM")
win.geometry("1200x600")
win.resizable(0,0)

img=Image.open("bag.jpg")
img=img.resize((1200,600))

bgg=ImageTk.PhotoImage(img)

lbl=Label(win,image=bgg)
lbl.place(x=0,y=0)

label=Label(win,text="FACE RECOGNITION MODULE",bg="black",fg="white",font=("times",24,"bold"))
label.place(x=200,y=50)
def data():
    try:
        name=ent_name.get()
        idd=int(ent_id.get()) 
        vid_cam = cv2.VideoCapture(0)
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        count = 0
        while(True):
            _, image_frame = vid_cam.read()
            gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
                cv2.putText(image_frame, str(count), (x, y-40), cv2.FONT_HERSHEY_SIMPLEX,  
                   1, (0, 255, 0), 2, cv2.LINE_AA)
                count += 1
                cv2.imwrite("dataset/"+name+"." + str(idd) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
                
            cv2.imshow('frame', image_frame)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif count>100:
                break
        vid_cam.release()
        cv2.destroyAllWindows()
        status="DATASET STORED \n SUCCESSFULLY"
    except:
        status="CHEK THE INPUT"
    label=Label(win,text=status,bg="black",fg="white",font=("times",24,"bold"))
    label.place(x=900,y=150)
def dataset():
    global ent_id,ent_name
    label=Label(win,text="FACE ID",bg="black",fg="white",font=("times",24,"bold"))
    label.place(x=250,y=100)
    ent_id=Entry(win,text="",bg="black",fg="white",font=("times",24,"bold"),width=10)
    ent_id.place(x=250,y=150)

    label=Label(win,text="NAME",bg="black",fg="white",font=("times",24,"bold"))
    label.place(x=500,y=100)
    ent_name=Entry(win,text="",bg="black",fg="white",font=("times",24,"bold"),width=15)
    ent_name.place(x=500,y=150)
    label=Button(win,text="Capture",bg="black",fg="white",font=("times",24,"bold"),command=data)
    label.place(x=700,y=150)
def training():
    # Get the faces and IDs
    faces,ids,ids_names = getImagesAndLabels('dataset')

    # Train the model using the faces and IDs
    recognizer.train(faces, np.array(ids))

    # Save the model into trainer.yml
    recognizer.write('trainer/trainer.yml')

    import csv
    f = open("names.csv", 'w', newline="")
    writer = csv.writer(f)
    writer.writerow(["id", "name"])
    writer.writerows(ids_names)
    f.close()
    status="DATASET Trained \n SUCCESSFULLY"
    label=Label(win,text=status,bg="black",fg="white",font=("times",24,"bold"))
    label.place(x=900,y=250)



    
label=Button(win,text="Collect Dataset",bg="black",fg="white",font=("times",24,"bold"),command=dataset)
label.place(x=100,y=150)

label=Button(win,text="Training",bg="black",fg="white",font=("times",24,"bold"),command=training)
label.place(x=100,y=250)

win.mainloop()
