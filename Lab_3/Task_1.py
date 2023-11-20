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

	with np.nditer(image, op_flags = ['readwrite']) as it:
		# op_flags = ['readwrite'] = итерация будет выполняться как для чтения, так и для записи значений пикселей
		for pixel in it:
			pixel[...] = 255 / (bright - dark) * (pixel - dark)  # преобразование яркости по формуле
	Image.fromarray(image).convert('RGB').save('./images/new_{}'.format(file))
	# Преобразование измененного массива в изображение, конвертируем в RGB формат и сохраняем в созданную папку
