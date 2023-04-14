import cv2
from deepface import DeepFace
import os

arquivos = os.listdir()

for arquivo in arquivos:
    if "png" in arquivo:

        # ler a imagem
        imagem = cv2.imread(arquivo)

        # passar a imagem para DeepFace
        resultado = DeepFace.analyze(imagem, actions=("age", "gender", "race", "emotion"), enforce_detection=False)

        # ver os resultados finais da análise.

        print(resultado)