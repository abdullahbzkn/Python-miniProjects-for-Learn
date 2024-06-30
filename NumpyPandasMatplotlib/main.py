import numpy as np
import matplotlib.pyplot as plt

age_list = [20,25,30,35,40,45,50,55,60]
weight_list = [70,75,73,85,89,90,75,84,90]
age_list = np.array(age_list)
weight_list = np.array(weight_list)
# plt.plot(age_list,weight_list,"y")
# plt.xlabel('Age')
# plt.ylabel('Weight')
# plt.title('Age - Weight Graph')
my_numpy1 = np.linspace(0,15,20)
my_numpy2 = my_numpy1**3
# plt.plot(my_numpy1,my_numpy2,"g*")
# plt.plot(my_numpy1,my_numpy2,"g-")
# plt.plot(my_numpy1,my_numpy2,"g+")
# plt.plot(my_numpy1,my_numpy2,"g--")
# plt.subplot(1,2,1)
# plt.plot(my_numpy1,my_numpy2,"g--")
# plt.subplot(1,2,2)
# plt.plot(my_numpy1,my_numpy2,"g*")
'''
my_figure = plt.figure()
my_axes = my_figure.add_axes([0.25, 0.25, 0.5, 0.5])
my_axes.plot(my_numpy1,my_numpy2,'g*')
my_axes.set_xlabel('X DATA')
my_axes.set_ylabel('Y DATA')
my_axes.set_title('Graph')
plt.show()
'''
my_figure = plt.figure()

my_axes = my_figure.add_axes([0.12, 0.1, 0.85, 0.85])
my_axes.plot(my_numpy1,my_numpy2,'g*')
my_axes.set_xlabel('X DATA')
my_axes.set_ylabel('Y DATA')
my_axes.set_title('Graph')

my_axes2 = my_figure.add_axes([0.25, 0.5, 0.3, 0.3])
my_axes2.plot(my_numpy1,my_numpy2,'g*')
my_axes2.set_xlabel('X DATA SMALL')
my_axes2.set_ylabel('Y DATA SMALL')
my_axes2.set_title('Small Graph')


(my_fig, my_axe) = plt.subplots()
my_numpy3 = np.linspace(0,15,20)
my_numpy4 = my_numpy3 ** 2
my_axe.plot(my_numpy3,my_numpy4, color="#CD621D", alpha=1)
my_axe.plot(my_numpy4,my_numpy3, color="#B81DCD", alpha=0.9)


(new_fig, new_axe) = plt.subplots()
new_axe.plot(my_numpy3, my_numpy3 + 2, color="#B81DCD", linewidth = 2.4)
new_axe.plot(my_numpy3, my_numpy3 + 3, color="#1DCDCA", linewidth = 1.4)
new_axe.plot(my_numpy3, my_numpy3 + 4, color="blue", linewidth = 1.4, linestyle="-.")
new_axe.plot(my_numpy3, my_numpy3 + 5, color="green", linewidth = 1.4, linestyle=":")
new_axe.plot(my_numpy3, my_numpy3 + 5, color="red", linewidth = 1.4, linestyle="--", marker="o")
new_axe.plot(my_numpy3, my_numpy3 + 6, color="black", linewidth = 1.4, linestyle="--", marker="+", markersize=8)

(new_fig2, new_axe2) = plt.subplots()
plt.scatter(my_numpy3, my_numpy4)

(new_fig3, new_axe3) = plt.subplots()
new_numpy = np.random.randint(0,100,40)
plt.hist(new_numpy)

new_fig.savefig("myfig.png",dpi=200)

plt.show()

'''
import numpy as np
#numpy array
my_list = [10,20,30,40]
type(my_list)
np.array(my_list)
my_numpy_array = np.array(my_list)
type(my_numpy_array)
my_numpy_array[0] = 100
my_numpy_array.max()
my_numpy_array.min()
my_numpy_array.mean()
matrix_list = [[1,0,0],[0,1,0],[0,0,1],[0,0,0]]
type(matrix_list)
numpy_matrix_list = np.array(matrix_list)
# array([[1, 0, 0],
#       [0, 1, 0],
#       [0, 0, 1],
#       [0, 0, 0]])
numpy_matrix_list[0][0]
numpy_matrix_list.shape
#arange
range(0,10)
range(0, 10)
list(range(0,10))
np.arange(0,10)
np.arange(0,30,2)
np.zeros(10)
np.zeros((10,10))
np.ones((10,10))
#linspace
np.linspace(0,10,100)
#random
np.random.randint(1,10,3)
np.random.randint(1,100)
np.random.randint(1,100,10)
#numpy arrays methods
my_numpy_list = np.arange(0,20)
my_list = list(range(0,20))
#my_list[4:9] = -10
my_numpy_list[4:9] = -10
other_list = np.arange(0,15)
slicing_list = other_list[4:10]
slicing_list[:] = 100
slicing_my_list = my_list[4:9]
slicing_my_list[0] = -100
slicing_my_list[1] = -100
numpy_list_3 = np.arange(0,20)
numpy_list_3_copy = numpy_list_3.copy()
slicing_3 = numpy_list_3_copy[4:9]
slicing_3[:] = -100
#numpy operations with numpy arrays
new_array = np.random.randint(1,150,25)
result_array = new_array > 50
np.max(result_array)
np.mean(result_array)
np.sqrt(result_array)


import pandas as pd

#series
my_dict = {"James" : 50, "Lars": 60, "Kirk" : 55, "Rob" : 65}
pd.Series(my_dict)
age_list = [50,60,55,65]
name_list = ["James","Lars","Kirk","Rob"]
pd.Series(age_list, name_list)
pd.Series(data=age_list,index=name_list)
numpy_array = np.arange(0,8)
numpy_array
pd.Series(numpy_array)
new_numpy_array = np.array([10,20,30,40])
pd.Series(new_numpy_array)
new_numpy_array
name_list
['James', 'Lars', 'Kirk', 'Rob']
pd.Series(data=new_numpy_array,index=name_list)
my_series = pd.Series(data=new_numpy_array,index=name_list)
my_series
type(my_series)
quiz_results1 = pd.Series(data=[70,60,100],index=["A","B","C"])
quiz_results2 = pd.Series(data=[80,30,50],index=["A","B","C"])
quiz_results1
quiz_results2
exam_results1 = pd.Series(data=[70,60,100],index=["A","B","C"])
exam_results2 = pd.Series(data=[80,30,50],index=["A","D","C"])
exam_results1 + exam_results2
'''