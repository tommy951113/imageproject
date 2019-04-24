import cv2
import numpy as np
from matplotlib import pyplot as plt
import pymeanshift as pms

def calSvf(img):

	# cal theta parameter in equation
	def theta(xf, yf):
		if xf < cx:	
			return np.pi / 2 + np.arctan((yf - cy) / (xf - cx))
		else:
			return 3 * np.pi / 2 + np.arctan((yf - cy) / (xf - cx))

	# image circle subset
	# return white pixel count divide whole pixel count
	def pt(i):
		circle_img = np.zeros((h, w), np.uint8)
		cv2.circle(
			circle_img, (int(h / 2), int(w / 2)),
			int(r0 - i * wr),
			1,
			thickness=-1)
		masked_data1 = cv2.bitwise_and(brightness, brightness, mask=circle_img)
		circle_img2 = np.zeros((h, w), np.uint8)
		cv2.circle(
			circle_img2, (int(h / 2), int(w / 2)),
			int(r0 - (i - 1) * wr),
			1,
			thickness=-1)
		masked_data2 = cv2.bitwise_and(brightness, brightness, mask=circle_img2)
   
		masked_data = cv2.bitwise_not(
			masked_data1, masked_data1, mask=masked_data2)

		unique, count = np.unique(masked_data, return_counts=True)
		t = np.pi * np.power(int(r0 - (i - 1) * wr), 2) - np.pi * np.power(int(r0 - i * wr), 2)
		return count[1] / int(t) if len(count) > 1 else 0

	# read image
	img1 = cv2.imread(img)[:,:,::-1]
	wc = img1.shape[1]
	hc = img1.shape[0]
	r0 = wc / (2 * np.pi)
	cx = cy = r0
	
	# histogram equalization
	# img_yuv = cv2.cvtColor(img1, cv2.COLOR_BGR2YUV)
	# img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
	# img1 = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

	img2 = np.empty([int(2 * r0) + 1, int(2 * r0) + 1, 3])

	# project to fisheye image
	for xf in range(img2.shape[1]):
		for yf in range(img2.shape[0]):
			xc = theta(xf, yf) / (2 * np.pi) * wc
			r = np.sqrt(np.power(xf - cx, 2) + np.power(yf - cy, 2))
			yc = r / r0 * hc
			if xc <= img1.shape[1] and yc <= img1.shape[0]:
				img2[yf][xf] = img1[int(yc)][int(xc)]

	img2 = np.uint8(img2)

	# meanshift segment
	(segmented_image, labels_image, number_regions) = pms.segment(
	img2, spatial_radius=6, range_radius=4.5, min_density=50)

	# threshold segment
	b, g, r = cv2.split(segmented_image)
	brightness = (0.5 * r + g + 1.5 * b) / 3
	brightness = np.uint8(brightness)
	ret, th = cv2.threshold(brightness, 0, 255,
							cv2.THRESH_BINARY + cv2.THRESH_OTSU)
	h = brightness.shape[0]
	w = brightness.shape[1]
	exg = 2 * g - b - r

	for y in range(0, h):
		for x in range(0, w):
			if brightness[y, x] >= ret:
				brightness[y, x] = 255
			elif brightness[y, x] >= exg[y, x]:
			    brightness[y, x] = 127
			else:
				brightness[y, x] = 0
	
	# cal sky view factor
	n = 37
	wr = r0 / n
	svf = 0
	c = 1 / (2 * np.pi) * np.sin(
	np.pi / (2 * n))  # constant in front of svf calculation equation
	fn = 0

	for i in range(1, n):
		fn = fn + np.sin(np.pi * (2 * i - 1) / (2 * n)) * pt(i)
		svf = np.pi / (2 * n) * fn
	return (img2, segmented_image, brightness, svf)

# show images in window
# img_list = ['01002500001405051327290575O','09002500121709191550389036G','09002500011603100854132478D',
# '09002500001504280917222851A']
img_list = ['09027900011607121435329675A','09000600121706201415155184A']
# img_list = ['10101003141207140925500_0 - 10101003141207140925500_315']
result_list = []
for img in img_list:
	result_list.append(calSvf('images/' + img + ".jpg"))

# 4*3
for (i,result) in enumerate(result_list):
	for j in range(len(result) - 1):
		plt.subplot(len(result_list),4,i*4+j+1),plt.imshow(result[j])
	plt.subplot(len(result_list),4,(i+1)*4),plt.hist(result[1].ravel(),256,[1,256])
	plt.title("SVF=" + str(result[3]))
	# plt.imshow(result[0]),plt.show()
	# plt.imshow(result[1]),plt.show()
	# plt.imshow(result[2]),plt.show()
# for (i,result) in enumerate(result_list):
	# for j in range(len(result) - 1):
		# plt.subplot(len(result_list),2,i*2+1),plt.imshow(result[1])
		# plt.subplot(len(result_list),2,i*2+2),plt.imshow(result[2])
	# plt.subplot(len(result_list),4,(i+1)*4),plt.hist(result[1].ravel(),256,[1,256])
	# plt.title("SVF=" + str(result[3]))
# plt.suptitle('threshold=' + str(ret))
plt.show()