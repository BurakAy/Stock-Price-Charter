import os
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import gui

def main():
  select_files = gui.sel_files

  if select_files:
    data_extraction(select_files)
  else:
    print('no files selected')
  
def data_extraction(file_list):
  column = gui.columns
  
  close = []
  tr_date = []

  if not column == ['']:
    for data_file in file_list:
      with open(data_file, encoding='utf-8-sig') as datafile:
        data = csv.DictReader(datafile)

        close_arr = []
        date_arr = []
        
        for row in data:
          close_arr.append(float(row[column[0]]))
          trade_date = datetime.strptime(row[column[1]], '%Y-%m-%d').date()
          date_arr.append(trade_date)
        
        close.append(close_arr)
        tr_date.append(date_arr)

    plotting(close, tr_date, file_list)
  else:
    print('enter column names')

def strip_file_names(files):
  file_names = []
  for file in files:
    file_names.append(os.path.basename(file).strip('.csv'))
  return file_names

def plotting(close, tr_date, files):
  stock_name = gui.stock_name
  file_names = strip_file_names(files)

  plt.figure(figsize=(16,8))
  plt.suptitle("PERFORMANCE BY YEAR")

  for x in range(len(tr_date)):
    plt.plot(close[x], linewidth=1)
    plt.legend(file_names, fontsize="12")

  plt.xlabel("TRADING DAYS (1 YR | Jan-Dec)")
  plt.xticks(range(1, len(tr_date[0]) + 15, 10))
  plt.ylabel("ADJ CLOSE (USD)")
  plt.title(stock_name)

  plt.savefig('Data_Graph.png')
  plt.show()

main()