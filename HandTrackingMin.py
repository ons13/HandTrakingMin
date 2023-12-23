import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils #this method hia ella ellaa taamlena kel dots ella fel yed

pTime = 0 #previous time =0
cTime = 0 # current time = 0


while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            #baad meaamlna el land mark o kol chaay taw lezem kol hand nekhthou el infos menhaa el landmark infos bch taatina el x o y o el id num ell bch nal9awouha
            for id , lm in enumerate(handLms.landmark):
                #print(id,lm) #hethoum bien sur bch nchoufouhom fel console
                h,w,c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print (id ,cx,cy)
                if id == 4:
                    cv2.circle(img,(cx,cy),20,(255,0,255),cv2.FILLED)


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS )
            #hatina img khater nhebouch aal rgbimg khater we are desplaing el ing mch el rgbimg /
            # tawa bch norssmou el hand khaw //
            # mpHands.hand_connection torssmelna el hands connection and we got all the 21 land marks
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    #donc el fct ella lota taatina el fps 9adech wa9tha 9adech men tasswira 9aaed el prog mte3na ykapti fel second (bien sur kol meyabda ykapti akthar kol mekhir )
    cv2.putText(img, str(int(fps)), (10,70) , cv2.FONT_HERSHEY_PLAIN , 3,
                (255,0,255),3)  #we want to convert el fps to string o baad aatineha values

    cv2.imshow("Image" , img)
    cv2.waitKey(1)
