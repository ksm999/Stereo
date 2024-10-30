import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
color_list = []
color_index = []
color_angle = []

for i in tqdm(range(1,256)):
  for m in range(i,256):
      for k in range(i, m+1):
        if i == m:
          theta = i * np.pi / 510
          phi = i * np.pi / 510
          x = np.cos(theta)
          y = 0
          z = -np.sin(phi)
          color_index.append([i,i,i])
          angle = [theta, phi]
          P = np.array([x,y,z])
          color_list.append([P])
          color_angle.append([angle])
        else:
          theta = (i-1) * np.pi/ 510 +  np.pi  * (m-i+1) / ((255 * 2) * (255-i+1))
          phi =(k  - i) * np.pi / (3 * (m - i ))
          x = np.cos(theta) * np.cos(phi)
          y = np.cos(theta) * np.sin(phi)
          z = -np.sin(theta)
          color_index.append([m,k,i])
          angle = [theta, phi]
          P = np.array([x,y,z])
          color_list.append([P])
          color_angle.append([angle])

for i in tqdm(range(1,256)):
  for m in range(i,256):
      for k in range(1, m-i+1):
        if i == m:
          theta = i * np.pi / 510
          phi = i * np.pi / 510
          x = np.cos(theta)
          y = 0
          z = -np.sin(phi)
          color_index.append([i,i,i])
          angle = [theta, phi]
          P = np.array([x,y,z])
          color_list.append([P])
          color_angle.append([angle])
        else:
          theta = (i-1) * np.pi/ 510 +  np.pi  * (m-i+1) / ((255 * 2) * (255-i+1))
          phi = k* np.pi / (3 * (m - i )) +  np.pi/3
          x = np.cos(theta) * np.cos(phi)
          y = np.cos(theta) * np.sin(phi)
          z = -np.sin(theta)
          color_index.append([m-k,m,i])
          angle = [theta, phi]
          P = np.array([x,y,z])
          color_list.append([P])
          color_angle.append([angle])

for i in tqdm(range(1,256)):
  for m in range(i,256):
      for k in range(i, m+1):
        if i == m:
          theta = i * np.pi / 510
          phi = i * np.pi / 510
          x = np.cos(theta)
          y = 0
          z = -np.sin(phi)
          color_index.append([i,m,k])
          angle = [theta, phi]
          P = np.array([x,y,z])
          color_list.append([P])
          color_angle.append([angle])
        else:
          theta = (i-1) * np.pi/ 510 +  np.pi  * (m-i+1) / ((255 * 2) * (255-i+1))
          phi =(k  - i) * np.pi / (3 * (m - i )) + 2 * np.pi/3
          x = np.cos(theta) * np.cos(phi)
          y = np.cos(theta) * np.sin(phi)
          z = -np.sin(theta)
          color_index.append([i,m,k])
          angle = [theta, phi]
          P = np.array([x,y,z])
          color_list.append([P])
          color_angle.append([angle])

for i in tqdm(range(1,256)):
  for m in range(i,256):
      for k in range(1, m-i+1):
        if i == m:
          theta = i * np.pi / 510
          phi = i * np.pi / 510
          x = np.cos(theta)
          y = 0
          z = np.sin(phi)
          color_index.append([i,i,i])
          angle = [theta, phi]
          P = np.array([x,y,z])
          color_list.append([P])
          color_angle.append([angle])
        else:
          theta = (i-1) * np.pi/ 510 +  np.pi  * (m-i+1) / ((255 * 2) * (255-i+1))
          phi = k  * np.pi / (3 * (m - i )) + 3 * np.pi/3
          x = np.cos(theta) * np.cos(phi)
          y = np.cos(theta) * np.sin(phi)
          z = -np.sin(theta)
          color_index.append([i,m-k,m])
          angle = [theta, phi]
          P = np.array([x,y,z])
          color_list.append([P])
          color_angle.append([angle])

for i in tqdm(range(1,256)):
  for m in range(i,256):
      for k in range(i, m+1):
        if i == m:
          theta = i * np.pi / 510
          phi = i * np.pi / 510
          x = np.cos(theta)
          y = 0
          z = -np.sin(phi)
          color_index.append([k,i,m])
          angle = [theta, phi]
          P = np.array([x,y,z])
          color_list.append([P])
          color_angle.append([angle])
        else:
          theta = (i-1) * np.pi/ 510 +  np.pi  * (m-i+1) / ((255 * 2) * (255-i+1))
          phi =(k  - i) * np.pi / (3 * (m - i )) +  4 * np.pi/3
          x = np.cos(theta) * np.cos(phi)
          y = np.cos(theta) * np.sin(phi)
          z = -np.sin(theta)
          color_index.append([k,i,m])
          angle = [theta, phi]
          P = np.array([x,y,z])
          color_list.append([P])
          color_angle.append([angle])

for i in tqdm(range(1,256)):
  for m in range(i,256):
      for k in range(1, m-i+1):
        if i == m:
          theta = i * np.pi / 510
          phi = i * np.pi / 510
          x = np.cos(theta)
          y = 0
          z = -np.sin(phi)
          color_index.append([i,i,i])
          angle = [theta, phi]
          P = np.array([x,y,z])
          color_list.append([P])
          color_angle.append([angle])
        else:
          theta = (i-1) * np.pi/ 510 +  np.pi  * (m-i+1) / ((255 * 2) * (255-i+1))
          phi = k  * np.pi / (3 * (m - i )) + 5 * np.pi/3
          x = np.cos(theta) * np.cos(phi)
          y = np.cos(theta) * np.sin(phi)
          z = -np.sin(theta)
          color_index.append([m,i,m-k])
          angle = [theta, phi]
          P = np.array([x,y,z])
          color_list.append([P])
          color_angle.append([angle])

class RGBMapping3DS:
    def __init__(self, color_index, color_list):
        self.color_index = np.array(color_index)
        self.color_list = np.array(color_list)

    def plot_points(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # RGB 값에 해당하는 좌표를 점으로 플로팅
        points = np.array([point[0] for point in self.color_list])
        colors = self.color_index / 255

        ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=colors, marker='o')
        ax.view_init(270,60)
        ax.set_xlabel('Red')
        ax.set_ylabel('Green')
        ax.set_zlabel('Blue')

        plt.show()

color_index_unique = []
color_angle_unique = []
color_list_unique = []
for idx, item in enumerate(color_index):
    if item not in color_index_unique:
        color_list_unique.append(color_list)
        color_index_unique.append(color_index[idx])
        color_angle_unique.append(color_angle[idx])

rgb_mapping_3d_south = RGBMapping3DS(color_index_unique[:], color_list_unique[:])

# 좌표를 플로팅
rgb_mapping_3d_south.plot_points()
