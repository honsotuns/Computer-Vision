


import random 

class RockPaper:

    def __init__(self,get_prediction):
        self.get_prediction = get_prediction

    def get_computer_choice(self):
        self.computer_choice = random.choice(self.get_prediction)
        self.get_user_choice()


    def get_prediction(self):
        print(' Kindly choose rock, paper or scissors')
        #from keras.model.h5 import load_model
        #import numpy as np
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()