import cv2
import pytesseract
import re

# Caminho para o executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Inicializa a captura de vídeo
video_capture = cv2.VideoCapture(0)

# Conjunto para armazenar resultados já impressos
resultados_impressos = set()

while True:
    # Captura um quadro de vídeo
    ret, frame = video_capture.read()

    # Verifica se o quadro foi capturado corretamente
    if not ret:
        print("Erro ao capturar o quadro de vídeo")
        break

    # Converte o quadro para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplica OCR no quadro
    texto = pytesseract.image_to_string(gray)

    # Procura pelo padrão específico
    match = re.search(r'[A-Za-z]{3}\d[A-Za-z]\d{2}', texto)
    if match:
        resultado = match.group(0)
        if resultado not in resultados_impressos:
            print(f'Captura: {resultado}')
            resultados_impressos.add(resultado)

    # Exibe o quadro de vídeo (opcional)
    cv2.imshow('Video', frame)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera os recursos
video_capture.release()
cv2.destroyAllWindows()
