import numpy as np

def calculate(list):
  if(len(list) !=9):
    raise ValueError("List must contain nine numbers.")
  
  list = np.array(list)
  print(list)
  mean_rows = [list[[0,1,2]].mean(), list[[3,4,5]].mean(), list[[6,7,8]].mean()]
  mean_columns = ([list[[0,3,6]].mean(), list[[1,4,7]].mean(), list[[2,5,8]].mean()])
  
  var_rows = [list[[0,1,2]].var(), list[[3,4,5]].var(), list[[6,7,8]].var()]
  var_columns = ([list[[0,3,6]].var(), list[[1,4,7]].var(), list[[2,5,8]].var()])
  
  std_rows = [list[[0,1,2]].std(), list[[3,4,5]].std(), list[[6,7,8]].std()]
  std_columns = ([list[[0,3,6]].std(), list[[1,4,7]].std(), list[[2,5,8]].std()])
  
  max_rows = [list[[0,1,2]].max(), list[[3,4,5]].max(), list[[6,7,8]].max()]
  max_columns = ([list[[0,3,6]].max(), list[[1,4,7]].max(), list[[2,5,8]].max()])
  
  min_rows = [list[[0,1,2]].min(), list[[3,4,5]].min(), list[[6,7,8]].min()]
  min_columns = ([list[[0,3,6]].min(), list[[1,4,7]].min(), list[[2,5,8]].min()])
  
  min_rows = [list[[0,1,2]].min(), list[[3,4,5]].min(), list[[6,7,8]].min()]
  min_columns = ([list[[0,3,6]].min(), list[[1,4,7]].min(), list[[2,5,8]].min()])
  
  sum_rows = [list[[0,1,2]].sum(), list[[3,4,5]].sum(), list[[6,7,8]].sum()]
  sum_columns = ([list[[0,3,6]].sum(), list[[1,4,7]].sum(), list[[2,5,8]].sum()])
  

  
  
  return {
    'mean': [mean_columns, mean_rows, list.mean()],
    'variance': [var_columns, var_rows, list.var()],
    'standard deviation': [std_columns, std_rows, list.std()],
    'max': [max_columns, max_rows, list.max()],
    'min': [min_columns, min_rows, list.min()],
    'sum': [sum_columns, sum_rows, list.sum()]
  }