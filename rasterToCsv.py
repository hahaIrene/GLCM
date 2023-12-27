from PIL import Image
import numpy as np
import os

# 定義資料夾路徑
folder_path = './data'

# 獲取資料夾中所有的檔案
file_list = os.listdir(folder_path)

# 儲存所有圖片資料的列表
image_arrays = []

# 依次讀取並處理圖片檔案
for file_name in file_list:
    if file_name.endswith('.tiff'):
        # 讀取圖片並轉換成 NumPy 陣列
        img = Image.open(os.path.join(folder_path, file_name))
        img_array = np.array(img)
        
        # 將圖片陣列加入列表
        image_arrays.append(img_array.ravel())

# 將所有圖片陣列堆疊成一個二維陣列
stacked_array = np.column_stack(image_arrays)

# 儲存成 CSV 檔案
np.savetxt(folder_path + 'output.csv', stacked_array.T, delimiter=',', fmt='%d')

