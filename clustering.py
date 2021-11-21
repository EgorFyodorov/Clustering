import random
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import copy

max_cluster_value = 100

def array_input(y, x):
	array = [[0 for i in range(x)] for q in range(y)]
	for i in range(y):
		m = list(map(int, input().split()))
		for q in range(x):
			array[i][q] = m[q]
	return array

def array_output(array):
	for i in range(len(array)):
		for q in range(len(array[0])):
			print(array[i][q], end = ' ')
		print()


def data_distribution(array, cluster): #распределение точек по имеющимся кластерам
	cluster_content = [[] for i in range(k)]

	for i in range(n):
		min_distance = 999999999
		situable_cluster = -1
		for j in range(k):
			distance = 0
			for q in range(dim):
				distance += (array[i][q]-cluster[j][q])**2
						
			distance = distance**(1/2)
			if distance < min_distance:
				min_distance = distance
				situable_cluster = j

		cluster_content[situable_cluster].append(array[i])
		
	return cluster_content

def cluster_update(cluster, cluster_content, dim): #новый кластер вычисляется на основании прилежных ему точек

	#d  количеств параметров
	k = len(cluster)

	for i in range(k): #кластер
		for q in range(dim): #параметр
			updated_parameter = 0
			for j in range(len(cluster_content[i])): 
				updated_parameter += cluster_content[i][j][q]
				
			if len(cluster_content[i]) != 0:
				updated_parameter = updated_parameter / len(cluster_content[i])
			cluster[i][q] = updated_parameter
	return cluster

def clusterization(array, k):
	n = len(array)  # количество объектов
	dim = len(array[0])  # количеств параметров

	cluster = [[0 for i in range(dim)] for q in range(k)] #параметры каждого кластера
	cluster_content = [[] for i in range(k)] #объекты входящие в каждый из кластеров

	for i in range(dim):
		for q in range(k):
			cluster[q][i] = random.randint(0, max_cluster_value) 

	cluster_content = data_distribution(array, cluster)

	#visualisation_3d(cluster_content, cluster)

	privious_cluster = copy.deepcopy(cluster_content)
	while 1:
		cluster = cluster_update(cluster, cluster_content, dim)
		#visualisation_3d(cluster_content, cluster)
		cluster_content = data_distribution(array, cluster)
		#visualisation_3d(cluster_content, cluster)
		if cluster_content == privious_cluster:
			break
		privious_cluster = copy.deepcopy(cluster_content)


	#print(cluster)
	#for i in range(k):
	#	print('Кластер', i + 1)
	#	print(cluster_content[i])

	if dim == 2:
		print('end')
		visualisation_2d(cluster_content, cluster)

	if dim == 3:
		print('end')
		visualisation_3d(cluster_content, cluster)

def visualisation_2d(cluster_content, cluster):

	k = len(cluster_content)
	plt.grid() 
	plt.xlabel("x")    
	plt.ylabel("y")
	
	#clusterx = []
	#clustery = []
	for i in range(k): #кластер
		x_coordinates = []
		y_coordinates = []
		#clusterx.append(cluster[i][0])
		#clustery.append(cluster[i][1])
		for q in range(len(cluster_content[i])):
			x_coordinates.append(cluster_content[i][q][0])
			y_coordinates.append(cluster_content[i][q][1])
		plt.scatter(x_coordinates, y_coordinates)
	#plt.scatter(clusterx, clustery, color = "black")
	plt.show()

def visualisation_3d(cluster_content, cluster):

	ax = plt.axes(projection="3d")
	plt.xlabel("x")    
	plt.ylabel("y")

	'''clusterx = []
	clustery = []
	clusterz = []'''

	k = len(cluster_content)
		
	for i in range(k):
		x_coordinates = []
		y_coordinates = []
		z_coordinates = []
		'''clusterx.append(cluster[i][0])
		clustery.append(cluster[i][1])
		clusterz.append(cluster[i][2])'''
		for q in range(len(cluster_content[i])):
			x_coordinates.append(cluster_content[i][q][0])
			y_coordinates.append(cluster_content[i][q][1])
			z_coordinates.append(cluster_content[i][q][2])
		ax.scatter(x_coordinates, y_coordinates, z_coordinates)
	#ax.scatter(clusterx, clustery, clusterz, color = "black")
	plt.show()


k = int(input('Количество кластеров: '))
n, dim = map(int, input('Количество строк и параметров: ').split())
array = array_input(n, dim)
clusterization(array, k)
