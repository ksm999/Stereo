import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
color_list = []
color_index = []
color_angle = []

df = pd.DataFrame(columns=range(1,4))

for n in range(0,256):
  for k in range(0,n+1):
    if n == 0 and k == 0:
      color_index.append([n, k, 0])
      angle = [0, 0]
      P = np.array([0,0,1])
      color_list.append([P])
      color_angle.append([angle])
    else:
      theta = n * np.pi / (255 * 2)
      phi = k * np.pi / (n * 3)
      x = np.sin(theta) * np.cos(phi)
      y = np.sin(theta) * np.sin(phi)
      z = np.cos(theta)
      color_index.append([n, k, 0])
      angle = [theta, phi]
      P = np.array([x,y,z])
      color_list.append([P])
      color_angle.append([angle])

for n in range(1,256):
  for k in range(0,n+1):
    theta = n * np.pi / (255 * 2)
    phi = k * np.pi / (n * 3) + np.pi/3
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    color_index.append([n-k, n, 0])
    angle = [theta, phi]
    P = np.array([x,y,z])
    color_list.append([P])
    color_angle.append([angle])

for n in range(1,256):
  for k in range(0,n+1):
    theta = n * np.pi / (255 * 2)
    phi = k * np.pi / (n * 3) + 2 * np.pi/3
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    color_index.append([0, n, k])
    angle = [theta, phi]
    P = np.array([x,y,z])
    color_list.append([P])
    color_angle.append([angle])

for n in range(1,256):
  for k in range(0,n+1):
    theta = n * np.pi / (255 * 2)
    phi = k * np.pi / (n * 3) + 3 * np.pi/3
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    color_index.append([0, n-k, n])
    angle = [theta, phi]
    P = np.array([x,y,z])
    color_list.append([P])
    color_angle.append([angle])

for n in range(1,256):
  for k in range(0,n+1):
    theta = n * np.pi / (255 * 2)
    phi = k * np.pi / (n * 3) + 4 * np.pi/3
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    color_index.append([k, 0, n])
    angle = [theta, phi]
    P = np.array([x,y,z])
    color_list.append([P])
    color_angle.append([angle])

for n in range(1,256):
  for k in range(0,n+1):
        theta = n * np.pi / (255 * 2)
        phi = k * np.pi / (n * 3) + 5 * np.pi/3
        x = np.sin(theta) * np.cos(phi)
        y = np.sin(theta) * np.sin(phi)
        z = np.cos(theta)
        color_index.append([n, 0, n-k])
        angle = [theta, phi]
        P = np.array([x,y,z])
        color_list.append([P])
        color_angle.append([angle])

class RGBMapping3D:
    def __init__(self, color_index, color_list):
        self.color_index = color_index
        self.color_list = color_list

    def plot_points(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # RGB 값에 해당하는 좌표를 점으로 플로팅
        for index, point in tqdm(zip(self.color_index, self.color_list)):
            ax.scatter(point[0][0], point[0][1], point[0][2], c=np.array(index) / 255, marker='o')
        ax.view_init(60,270)
        ax.set_xlabel('Red')
        ax.set_ylabel('Green')
        ax.set_zlabel('Blue')

        plt.show()


# RGBMapping3D 클래스 인스턴스 생성
rgb_mapping_3d = RGBMapping3D(color_index[:524288*12], color_list[:524288*12])

# 좌표를 플로팅
rgb_mapping_3d.plot_points()