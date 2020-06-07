import cv2
def face_detect(picture):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Read the input image
    img = cv2.imread('static/'+picture.filename)
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    i=0
    face_list=[]
    for (x, y, w, h) in faces:
        detect = {}
        coordinates = {}
       
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
       
        detect["faceid"] = i
        coordinates["top"]=x
        coordinates["width"]=y
        coordinates["left"]=x+w
        coordinates["height"]=y+h
       
        detect["faceRectangle"]=coordinates
       
        face_list.append(detect)
       
        i+=1
    # Display the output
    cv2.imwrite('static/img.jpg', img)
    
    return str(face_list)