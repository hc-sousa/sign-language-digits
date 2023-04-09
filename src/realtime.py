# import the opencv library
import cv2
import pickle
import numpy as np

# Resize function
def resize(img):
    width = 50
    height = 50
    dim = (width, height)

    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return resized

# Convert image to grayscale
def grayscale(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray

# Flatten image
def flatten(img):
    data = np.array(img)

    flattened = data.flatten()
    return flattened
  
  
# define a video capture object
vid = cv2.VideoCapture(0)


logreg = pickle.load(open('models/logistic_regression.sav', 'rb'))
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    img = resize(frame)
    img = grayscale(img)
    img = flatten(img)

    print(logreg.predict(img.reshape(1, -1)))
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()