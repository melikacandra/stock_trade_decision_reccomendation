import os
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import math
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
sc = MinMaxScaler(feature_range=(0,1)) #normalisasi dari 0 - 1
path_dir = "data"
list_file = os.listdir(path_dir)
asii_data = path_dir+"/"+list_file[2]

def data_clean(path_data):
  df = pd.read_csv(path_data)
  df = df.drop('Unnamed: 0', axis=1)
  df = df.sort_values('date', ascending=True)
  df.set_index('date', inplace=True)
  return df

def view_data(df, nama):
  #Menampilkan data close price
  plt.figure(figsize=(16,8))
  sns.lineplot(x=df.index, y=df['close'])
  plt.xlabel('Tanggal', fontsize=20)
  plt.ylabel('Harga Penutupan dalam Rupiah (Rp)', fontsize=20)
  plt.title('Riwayat Harga Penutupan pada Emiten ' + nama)
  plt.savefig('result/'+nama+'_stockprice.png')

def split_data(df, timestep):
  from sklearn.preprocessing import MinMaxScaler
  close = df.iloc[: , 5:6]
  train_set = close.iloc[:485, :].values
  test_set = close.iloc[485:, :].values
  sc = MinMaxScaler(feature_range=(0,1)) #normalisasi dari 0 - 1
  train_set_scaled= sc.fit_transform(train_set)
  x_train = []
  y_train = []
  for i in range(timestep, 485):
    x_train.append(train_set_scaled[i-timestep:i,0])
    y_train.append(train_set_scaled[i,0])
  x_train, y_train = np.array(x_train), np.array(y_train)
  x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
  return x_train, y_train

def view_loss_accuracy_history(history,nama, num):
  #Melihat plot evaluasi model
  plt.figure(figsize=(15,6))
  plt.plot(history.history['loss'])
  plt.plot(history.history['accuracy'])
  plt.xlabel('Epochs')
  plt.ylabel('Loss')
  plt.title('Riwayat Train ' + nama + str(num))
  plt.savefig('result/'+nama+str(num)+'_train_history.png')
  plt.show()
  

def predict(df, timesteps, model):
  df_to_train = df[:485] #data train
  df_to_test = df[485:] #data test
  data_total= pd.concat([df_to_train['close'], df_to_test['close']],  axis=0) #digabungin
  #inputnya dimulai dari total data dikurang data test dikurang timestep (jadi dikurang 30 hari sebelum data terbaru dari data train)
  inputs= data_total[len(data_total)-len(df_to_test)-timesteps:].values
  inputs = inputs.reshape(-1,1)
  inputs = sc.fit_transform(inputs)

  x_test = [] #loop dari 30 dengan ukuran data yang 485 - 30 = 455 itu
  for i in range(timesteps, inputs.shape[0]):
    x_test.append(inputs[i-timesteps:i, 0])

  x_test = np.array(x_test)
  x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
  predict = model.predict(x_test)
  predict = sc.inverse_transform(predict)
  return predict

def view_result(pred_res, test_set, name, timestep):
  plt.figure(figsize=(15,8))
  plt.plot(test_set['close'], color='red', label='Harga Sebenarnya Saham '+ name)
  plt.plot(pred_res, color='blue', label='Harga Prediksi Saham '+ name)
  plt.title('Prediksi Harga Saham'+name+'Bergantung Pada '+timestep+'Hari Sebelumnya', fontsize=20)
  plt.xlabel('Waktu', fontsize=15)
  plt.ylabel('Harga Saham '+ name, fontsize=15)
  plt.legend()
  plt.show()

#Model 1 Polos: 1 Layer, 10 unit, 100 epochs, 32 Batch Size, Optimizer Adam

def train(df_, timestep, name, test_, num, n_layer, n_unit, rate_dropout, n_epoch):
    x_train_, y_train_ = split_data(df_, timestep)
    model = Sequential()
    model.add(LSTM(units=n_unit, return_sequences=True, input_shape=(timestep, 1))) #layer lstm dengan 1- unit
    for i in range(n_layer):
        model.add(LSTM(units=n_unit, return_sequences=True))
        model.add(Dropout(rate=rate_dropout))
    model.add(LSTM(units=n_unit))    
    model.add(Dense(units=1))
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    history_1 = model.fit(x_train_, y_train_, epochs=n_epoch, batch_size=32)
    view_loss_accuracy_history(history_1, name, str(num))
    predict_ = predict(df_, timestep, model)
    view_result(predict_, test_, name.upper(), str(timestep) )
    model_name = name+'_unit='+str(n_unit)+'_layer='+str(n_layer)+'_rate_dropout='+str(rate_dropout)
    model.save('model/'+model_name+'.h5')
    
    test_saved_1_model = load_model('model/'+model_name+'.h5')
    #predict_saved = predict(df_,timestep,test_saved_1_model)
    #view_result(predict_saved, test_, '' )
    mse_ = mean_squared_error(predict_, test_['close'])
    mae_ = mean_absolute_error(predict_, test_['close'])
    rmse_ = math.sqrt(mse_)
    r2_ = r2_score(predict_, test_['close'])
    eval_dic = {'mse' : mse_, 'mae' : mae_, 'rmse' : rmse_, 'accuracy_history':history_1.history['accuracy'], 'loss_history':history_1.history['loss']}
    print("Hasil Evaluasi Model " +name + str(num)+ ": \n mse: ", mse_,"\n mae: ", mae_, "\n rmse: ", rmse_, "\n r2: ", r2_ )
    return eval_dic

df_asii = data_clean(asii_data)
test_asii = df_asii[485:]

train(df_asii, 7, 'asii'.upper(), test_asii, 1, 1, 10, 0,250)