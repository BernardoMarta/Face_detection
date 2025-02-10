import cv2

def detect_faces(image_path):
    
    #Classifier for face dection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    #Image

    image= cv2.imread(image_path)
    if image is None:
        print('Error loading the image.')
    
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    #Face detection

    faces= face_cascade.detectMultiScale(image_gray, scaleFactor = 1.1, minNeighbors=5, minSize=(30,30))
    
    for (x, y ,w, h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0),2)
    
    #Show output

    cv2.imshow('Detect Faces', image)
    cv2.waitKey(0)
    cv2. destroyAllWindows()
    number_faces_detected = len(faces)

    #Show accuracy
    number_faces_detected = len(faces)
    while True:
        user_count_faces = int(input('How many faces do you see in the image? '))
        if user_count_faces>0:
            break
        else:
            print('Insert a positive integer.')
    accuracy = round(number_faces_detected/user_count_faces,2)*100

    print()
    print(f"Number of faces detected:{number_faces_detected}")
    print(f'Accuracy score: {accuracy}%')
    print()


file_path=input('Insert the path of the image you want to analyze: ')
detect_faces(file_path)
