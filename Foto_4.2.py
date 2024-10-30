import cv2
import os
# Функция для обнаружения лиц на изображении
def detect_faces(image_path, output_path):
    # Загрузка каскада Хаара для распознавания лиц
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Загрузка изображения
    image_path = '/home/sva/Документы/New_project/image.jpg'
    image = cv2.imread(image_path)

    # Преобразование изображения в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Обнаружение лиц на изображении
    faces = face_cascade.detectMultiScale(
        gray_image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Подсчет количества обнаруженных лиц
    num_faces = len(faces)
    print(f"Количество обнаруженных лиц на {image_path}: {num_faces}")

    # Рисование прямоугольников вокруг обнаруженных лиц
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Сохранение результата
    cv2.imwrite(output_path, image)
    print(f"Результат сохранен в {output_path}")

# Основная функция
def main():
    # Путь к директории с изображениями
    input_directory = '/home/sva/Документы/New_project'  # Замените на путь к вашей директории с изображениями
    output_directory = '/home/sva/Документы/New_project'  # Замените на путь к директории для сохранения результатов
    # Обработка всех изображений в директории
    for filename in os.listdir(input_directory):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Поддерживаемые форматы изображений
            image_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, f'detected_{filename}')
            detect_faces(image_path, output_path)

if __name__ == '__main__':
    main()