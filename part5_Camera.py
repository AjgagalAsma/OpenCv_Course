import cv2
import sys

# Définir la source de la caméra (0 = webcam intégrée)
s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

source = cv2.VideoCapture(s)  # Ouvrir la caméra

win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)  # Créer une fenêtre redimensionnable

while cv2.waitKey(1) != 27:  # Boucle jusqu'à appui sur Échap
    has_frame, frame = source.read()  # Lire une image
    if not has_frame:
        break

    frame = cv2.flip(frame, 1)        # Miroir horizontal
    cv2.imshow(win_name, frame)       # Afficher l'image

source.release()  
cv2.destroyWindow(win_name)          # Fermer la fenêtre
