import numpy as np
from PIL import Image
import os

if not os.path.exists('./images'):
	os.makedirs('./images')  # Создание папки для обработанных картинок

for file in os.listdir('./lunar_images'):
	image = np.array(Image.open('./lunar_images/' + file), dtype='i')
	# Загрузка изображения в виде массива, приводя его к целочисленному типу данных

	dark = np.min(image)
	bright = np.max(image)
	# Наименьшее и наибольшее значение пикселя в изображении

	# Преобразование яркости по формуле без использования np.nditer
	image = 255 / (bright - dark) * (image - dark)

	# Ограничние значения в диапазоне от 0 до 255
	image = np.clip(image, 0, 255)

	# округление
	image = np.round(image).astype(np.uint8)
	
	Image.fromarray(image).convert('RGB').save('./images/new_{}'.format(file))
	# Преобразование измененного массива в изображение, конвертируем в RGB формат и сохраняем в созданную папку
