import matplotlib.pyplot as plt
import time
import random

def BubbleSort(array):
    band = False
    while(band == False):
        band = True
        for i in range(len(array)-1):   
            if array[i] > array[i+1]:     
               aux = array[i]
               array[i] = array[i+1]
               array[i+1] = aux
               band = False      
    return array
  

def merge(array1, array2):
    result = []
    i, j = 0 , 0 
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[i]:
            result.append(array1[i])
            i+= 1 
        else:
            result.append(array2[j])
            j+= 1
    if i == len(array1):
        for k in range(j, len(array2)):
            result.append(array2[k])    
    else:
        for k in range(i, len(array1)):
            result.append(array1[k])
    return result

def MergeSort(array):
    if len(array) < 2:
        return array
    else:
        mitad = (len(array) // 2)
        arra1 = MergeSort(array[:mitad])
        arra2 = MergeSort(array[mitad:])
        return merge(arra1,arra2)



def generate_random_list(size):
    return [random.randint(0, 1000) for _ in range(size)]


def tiempo(algorithm, array):
    start_time = time.time()
    algorithm(array)
    end_time = time.time()
    return end_time - start_time


array_sizes = [100, 200, 300, 400, 500]
bubble_sort_times = []
merge_sort_times = []

for size in array_sizes:
    array = generate_random_list(size)
    bubble_sort_time = tiempo(BubbleSort, array.copy())
    merge_sort_time = tiempo(MergeSort, array.copy())
    bubble_sort_times.append(bubble_sort_time)
    merge_sort_times.append(merge_sort_time)

# Grafica
plt.plot(array_sizes, bubble_sort_times, color='orange', label='Bubble Sort')
plt.plot(array_sizes, merge_sort_times, color='green', label='Merge Sort')
plt.xlabel('Tamaño del arreglo')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de Bubble Sort y Merge Sort')
plt.legend()
plt.show()
