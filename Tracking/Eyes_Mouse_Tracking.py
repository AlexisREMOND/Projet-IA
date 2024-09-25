import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

if not cam.isOpened():
    print("Erreur: Impossible d'ouvrir la caméra.")
    exit()

while True:
    ret, frame = cam.read()
    if not ret:
        print("Erreur: Impossible de lire l'image de la caméra.")
        break
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)

    if output.multi_face_landmarks:
        landemark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landemark_points:
            landemarks = landemark_points[0].landmark
            for id, landmark in enumerate(landemarks[474:478]):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x,y), 3, (0, 255, 0))
                if id == 1:
                    screen_x = screen_w / frame_w * x  #int(landmark.x * screen_w)
                    screen_y = screen_h / frame_h * y#int(landmark.y * screen_h)
                    pyautogui.moveTo(screen_x, screen_y)
            left = [landemarks[145], landemarks[159]]
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x,y), 3, (0, 255, 255))
            if (left[0].y - left[1].y) < 0.004:
                pyautogui.click()
                pyautogui.sleep(1)

    cv2.imshow('Eye Controlled Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

