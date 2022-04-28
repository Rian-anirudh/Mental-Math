import numpy as np
import pandas as pd

# Function to add matrix
def quants_apt(y, m,n):
    # y: length of numbers 
    # m: lowest number start range, n: greatest number end range
    arr = np.random.randint(m,n, size=(2,y))
    ##
    # for not repitative arrays
    # arr = np.random.choice(range(m,n), size=(2,y), replace = False)
    ##
    sol = np.append(0,arr[0])
    sol = np.append(sol,0)
    ques= sol
    
    # Creating Solution dataset
    for i in range(y):
        inter = arr[1][i] + arr[0]
        add   = np.sum(inter)
        inter = np.append(arr[1][i],inter)
        inter = np.append(inter, add)
        sol = np.vstack([sol,inter])
    c_sum = np.sum(sol, axis=0)
    sol = np.vstack([sol,c_sum])
    
    # Creating Question dataset
    zrr = np.zeros(y**2).reshape(y,y)
    zrr = np.vstack([arr[0],zrr])
    arrT = arr[1][np.newaxis]
    arrT= arrT.transpose()
    arrT= np.vstack([0,arrT])
    arr = np.append(arrT, zrr, axis=1)
    
    return sol, arr



## STAG 
solution, array = quants_apt(10, 20, 90)

# Representing question dataset
data_q = pd.DataFrame(array, index = array[:,0], columns = array[0,:])
dataset_q = data_q.iloc[1:,1:]

# organising data into pandas data frame
data = pd.DataFrame(solution, index = solution[:,0], columns = solution[0,:])
dataset = data.iloc[1:,1:]

# Export tables to excel
from datetime import datetime
date = datetime.now().strftime("%Y_%m_%d-%I:%M:_%p")
writer = pd.ExcelWriter("./Questions/Quest"+date+".xlsx")

dataset_q.to_excel(writer, sheet_name = 'Question')
dataset.to_excel(writer, sheet_name = 'solution')
writer.save()
writer.close()

