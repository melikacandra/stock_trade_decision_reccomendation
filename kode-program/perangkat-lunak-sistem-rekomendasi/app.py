from flask import Flask, render_template, request, redirect, url_for
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
sc = MinMaxScaler(feature_range=(0,1)) #normalisasi dari 0 - 1
app = Flask(__name__)

data_path = 'data'
model_path = 'model_final'
df_main = pd.read_csv(data_path+"/"+"base_data.csv")

asii_long = df_main['nama lengkap'].iloc[[0]].values[0]
amrt_long = df_main['nama lengkap'].iloc[[1]].values[0]
untr_long = df_main['nama lengkap'].iloc[[2]].values[0]
unvr_long = df_main['nama lengkap'].iloc[[3]].values[0]
mapi_long = df_main['nama lengkap'].iloc[[4]].values[0]
inkp_long = df_main['nama lengkap'].iloc[[5]].values[0]
intp_long = df_main['nama lengkap'].iloc[[6]].values[0]
aces_long = df_main['nama lengkap'].iloc[[7]].values[0]
sido_long = df_main['nama lengkap'].iloc[[8]].values[0]
hrum_long = df_main['nama lengkap'].iloc[[9]].values[0]

asii_price = df_main['harga'].iloc[[0]].values[0]
amrt_price = df_main['harga'].iloc[[1]].values[0]
untr_price = df_main['harga'].iloc[[2]].values[0]
unvr_price = df_main['harga'].iloc[[3]].values[0]
mapi_price = df_main['harga'].iloc[[4]].values[0]
inkp_price = df_main['harga'].iloc[[5]].values[0]
intp_price = df_main['harga'].iloc[[6]].values[0]
aces_price = df_main['harga'].iloc[[7]].values[0]
sido_price = df_main['harga'].iloc[[8]].values[0]
hrum_price = df_main['harga'].iloc[[9]].values[0]

asii_fun = df_main['fun'].iloc[[0]].values[0]
amrt_fun = df_main['fun'].iloc[[1]].values[0]
untr_fun = df_main['fun'].iloc[[2]].values[0]
unvr_fun = df_main['fun'].iloc[[3]].values[0]
mapi_fun = df_main['fun'].iloc[[4]].values[0]
inkp_fun = df_main['fun'].iloc[[5]].values[0]
intp_fun = df_main['fun'].iloc[[6]].values[0]
aces_fun = df_main['fun'].iloc[[7]].values[0]
sido_fun = df_main['fun'].iloc[[8]].values[0]
hrum_fun = df_main['fun'].iloc[[9]].values[0]

asii_growth = df_main['growth'].iloc[[0]].values[0]
amrt_growth = df_main['growth'].iloc[[1]].values[0]
untr_growth = df_main['growth'].iloc[[2]].values[0]
unvr_growth = df_main['growth'].iloc[[3]].values[0]
mapi_growth = df_main['growth'].iloc[[4]].values[0]
inkp_growth = df_main['growth'].iloc[[5]].values[0]
intp_growth = df_main['growth'].iloc[[6]].values[0]
aces_growth = df_main['growth'].iloc[[7]].values[0]
sido_growth = df_main['growth'].iloc[[8]].values[0]
hrum_growth = df_main['growth'].iloc[[9]].values[0]

asii_point = 0
amrt_point = 0
untr_point = 0
unvr_point = 0
mapi_point = 0
inkp_point = 0
intp_point = 0
aces_point = 0
sido_point = 0
hrum_point = 0

asii_total = 0
amrt_total = 0
untr_total = 0
unvr_total = 0
mapi_total = 0
inkp_total = 0
intp_total = 0
aces_total = 0
sido_total = 0
hrum_total = 0



#list_price = [asii_price, amrt_price, untr_price, unvr_price, mapi_price, inkp_price, intp_price, aces_price, sido_price]
def data_clean(path_data):
  df = pd.read_csv(path_data)
  df = df.drop('Unnamed: 0', axis=1)
  df = df.sort_values('date', ascending=True)
  df.set_index('date', inplace=True)
  return df


def predict(df,  model, num_predict):
  #test_len = len(df[485:])
  curr_model = load_model(model)
  len_total = len(df)
  timesteps = curr_model.get_config()['layers'][0]['config']['batch_input_shape'][1]
  #inputnya dimulai dari total data dikurang data test dikurang timestep (jadi dikurang 30 hari sebelum data terbaru dari data train)
  #print(df.head())
  #print(len_total, num_predict, timesteps)
  start = int(len_total)-int(num_predict)-int(timesteps)
  #print(start)
  inputs= df[start:]
  inputs = inputs.values
  inputs = inputs.reshape(-1,1)
  inputs = sc.fit_transform(inputs)
  x_test = [] #loop dari 30 dengan ukuran data yang 485 - 30 = 455 itu
  for i in range(timesteps, inputs.shape[0]):
    x_test.append(inputs[i-timesteps:i, 0])
  x_test = np.array(x_test)
  x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
  predict = curr_model.predict(x_test)
  predict = sc.inverse_transform(predict)
  #print(predict)
  return predict

def get_last(data_test, curr_model, num):
    res = predict(data_test, curr_model,num)
    return res[-1][0]

def get_pred_stock(stock, num):
    model, data, long_name = get_data_model(stock)
    model_use = load_model(model)
    df = data_clean(data)
    pred = int(get_last(df['close'], model, num))
    return pred

def get_data_model(stock_name):
    if stock_name == 'asii':
        curr_model = model_path +'/'+  "asii_1_100_0.2_100_8_30.h5"
        curr_data = data_path +'/' + "ASII2201-2405.csv"
        long_name = asii_long
    elif stock_name == 'amrt':
        curr_model = model_path +'/'+  "amrt_1_300_0_100_8_7.h5"
        curr_data = data_path +'/' + "AMRT2201-2405.csv"
        long_name = amrt_long
    elif stock_name == 'untr':
        curr_model = model_path +'/'+  "untr_1_100_0.2_100_8_30.h5"
        curr_data = data_path +'/' + "UNTR2201-2405.csv"
        long_name = untr_long
    elif stock_name == 'unvr':
        curr_model = model_path +'/'+  "unvr_1_100_0.2_100_8_30.h5"
        curr_data = data_path +'/' + "UNVR2201-2405.csv"
        long_name = unvr_long
    elif stock_name == 'mapi':
        curr_model = model_path +'/'+  "mapi_1_100_0_200_8_30.h5"
        curr_data = data_path +'/' + "MAPI2201-2405.csv"
        long_name = mapi_long
    elif stock_name == 'inkp':
        curr_model = model_path +'/'+  "inkp_1_100_0_200_32_7.h5"
        curr_data = data_path +'/' + "INKP2201-2405.csv"
        long_name = inkp_long
    elif stock_name == 'intp':
        curr_model = model_path +'/'+  "intp_1_100_0.2_100_32_30.h5"
        curr_data = data_path +'/' + "INTP2201-2405.csv"
        long_name = intp_long
    elif stock_name == 'aces':
        curr_model = model_path +'/'+  "aces_5_100_0_100_8_30.h5"
        curr_data = data_path +'/' + "ACES2201-2405.csv"
        long_name = aces_long
    elif stock_name == 'sido':
        curr_model = model_path +'/'+  "sido_1_300_0_100_8_7.h5"
        curr_data = data_path +'/' + "SIDO2201-2405.csv"
        long_name = sido_long
    elif stock_name == 'hrum':
        curr_model = model_path +'/'+  "hrum_1_100_0_100_8_7.h5"
        curr_data = data_path +'/' + "HRUM2201-2405.csv"
        long_name = hrum_long
    return curr_model, curr_data, long_name





@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == "POST":
        stock = request.form.get("stock")
        num = request.form.get("num")
        if(stock == "all"):
            return redirect(url_for('predict_all', num=num))
        else:
            return redirect(url_for('predict_one', stock=stock, num=num))
    return render_template('index.html', asii_price=asii_price, amrt_price=amrt_price, 
                           untr_price=untr_price, unvr_price=unvr_price, mapi_price=mapi_price, 
                           inkp_price=inkp_price, intp_price=intp_price, sido_price=sido_price, 
                           hrum_price=hrum_price, aces_price=aces_price)



@app.route("/predict-one" ,methods = ['GET', 'POST'] )
def predict_one():
    if request.method == "POST":
        stock = request.form.get("stock")
        num = request.form.get("num")
        if(stock == "all"):
            return redirect(url_for('predict_all', num=num))
        else:
            return redirect(url_for('predict_one', stock=stock, num=num))
    stock = request.args.get('stock', None)
    num = request.args.get('num', None)
    model, data, long_name = get_data_model(stock)
    model_use = load_model(model)
    df = data_clean(data)
    pred = int(get_last(df['close'], model, num))
    if(stock == 'asii'):
        harga = asii_price
        fun = asii_fun
        growth = asii_growth
    elif(stock == 'amrt'):
        harga = amrt_price
        fun = amrt_fun
        growth = amrt_growth
    elif(stock == 'untr'):
        harga = untr_price
        fun = untr_fun
        growth = untr_growth
    elif(stock == 'unvr'):
        harga = unvr_price
        fun = unvr_fun
        growth = unvr_growth
    elif(stock == 'mapi'):
        harga = mapi_price
        fun = mapi_fun
        growth = mapi_growth
    elif(stock == 'intp'):
        harga = intp_price
        fun = intp_fun
        growth = intp_growth
    elif(stock == 'inkp'):
        harga = inkp_price
        fun = inkp_fun
        growth = inkp_growth
    elif(stock == 'aces'):
        harga = aces_price
        fun = aces_fun
        growth = aces_growth
    elif(stock == 'sido'):
        harga = sido_price
        fun = sido_fun
        growth = sido_growth
    elif(stock == 'hrum'):
        harga = hrum_price
        fun = hrum_fun
        growth = hrum_growth
    #pred = test_pred(pred)
    selisih = pred-harga
    if(selisih>0):
        point =1
    else:
        point = 0
    total = fun + growth + point
    if(total == 3):
        rec = "Beli Kuat (Strong Buy)"
        rec_desc = "Saham ini cocok untuk di beli dalam waktu jangka panjang maupun jangka pendek. Cocok untuk investor maupun trader"
    elif(total == 2):
        rec = "Beli Lemah (Weak Buy)"
        if(fun == 1 and growth == 1 and point == 0):
            rec_desc = "Saham ini cocok untuk di beli dalam jangka waktu panjang. Tetapi, kurang cocok untuk dibeli dalam jangka pendek. Cocok untuk investor"
        elif(fun == 0 and growth == 1 and point == 1):
            rec_desc = "Saham ini cocok untuk di beli dalam jangka waku panjang maupun pendek. Tetapi perusahan ini belum memiliki fundamental yang cukup. Cocok untuk investor dan trader yang berani menanggung risiko"
        elif(fun == 1 and growth == 0 and point == 1):
            rec_desc = "Saham ini cocok untuk dibeli dalam jangka waktu panjang yang terbatas dan waktu pendek. Hal ini karena pertumbuhan perusahan masih kurang baik. Cocok untuk investor dan trader yang berani menanggung risiko"
 
    else:
        rec = "Jangan Beli (Hold)"
        rec_desc ="Saham ini tidak direkomendasikan untuk dibeli, risiko yang ada cukup tinggi. Silahkan pilih saham lain atau menunggu di lain waktu untuk membeli saham ini"
    if(fun == 1):
        rec_fun = "Baik"
    else:
        rec_fun = "Kurang Baik"
    
    if(growth == 1):
        rec_growth = "Naik"
    else:
        rec_growth = "Turun"
    
    if(point == 1):
        rec_point = "Naik"
    else:
        rec_point = "Turun"
    
       
    
    return render_template('one_stock_rec_page.html',stock=stock, num=num, 
                           pred=pred, harga=harga, selisih=selisih, rec=rec, rec_fun = rec_fun,
                           rec_growth=rec_growth, rec_point=rec_point, long_name=long_name, rec_desc=rec_desc)



@app.route("/predict-all",methods = ['GET', 'POST'])
def predict_all():
    if request.method == "POST":
        stock = request.form.get("stock")
        num = request.form.get("num")
        if(stock == "all"):
            return redirect(url_for('predict_all', num=num))
        else:
            return redirect(url_for('predict_one', stock=stock, num=num))
    num = request.args.get('num', None)
    pred_asii = get_pred_stock('asii', num)
    pred_amrt = get_pred_stock('amrt', num)
    pred_untr = get_pred_stock('untr', num)
    pred_unvr = get_pred_stock('unvr', num)
    pred_mapi = get_pred_stock('mapi', num)
    pred_inkp = get_pred_stock('inkp', num)
    pred_intp = get_pred_stock('intp', num)
    pred_aces = get_pred_stock('aces', num)
    pred_sido = get_pred_stock('sido', num)
    pred_hrum = get_pred_stock('hrum', num)
    selisih_asii = pred_asii - asii_price
    selisih_amrt = pred_amrt - amrt_price
    selisih_unvr = pred_unvr - unvr_price
    selisih_untr = pred_untr - untr_price
    selisih_mapi = pred_mapi - mapi_price
    selisih_inkp = pred_inkp - inkp_price
    selisih_intp = pred_intp - intp_price
    selisih_aces = pred_aces - aces_price
    selisih_sido = pred_sido - sido_price
    selisih_hrum = pred_hrum - hrum_price
    if(selisih_asii> 0):
        point_asii = 1
    if(selisih_amrt> 0):
        point_amrt = 1
    if(selisih_unvr> 0):
        point_unvr = 1
    if(selisih_untr> 0):
        point_untr = 1
    if(selisih_mapi> 0):
        point_mapi = 1
    if(selisih_inkp> 0):
        point_inkp = 1
    if(selisih_intp> 0):
        point_intp = 1
    if(selisih_aces> 0):
        point_aces = 1
    if(selisih_sido> 0):
        point_sido = 1
    if(selisih_hrum> 0):
        point_hrum = 1
    asii_total = asii_fun + asii_growth + asii_point
    amrt_total = amrt_fun + amrt_growth + amrt_point
    unvr_total = unvr_fun + unvr_growth + unvr_point
    untr_total = untr_fun + untr_growth + untr_point
    mapi_total = mapi_fun + mapi_growth + mapi_point
    inkp_total = inkp_fun + inkp_growth + inkp_point
    intp_total = intp_fun + intp_growth + intp_point
    aces_total = aces_fun + aces_growth + aces_point
    sido_total = sido_fun + sido_growth + sido_point
    hrum_total = hrum_fun + hrum_growth + hrum_point
    if(asii_total == 3):
        rec_asii = "Beli Kuat (Strong Buy)"
    elif(asii_total == 2):
        rec_asii = "Beli Lemah (Weak Buy)"
    else:
        rec_asii = "Jangan Beli (Hold)"

    if(amrt_total == 3):
        rec_amrt = "Beli Kuat (Strong Buy)"
    elif(amrt_total == 2):
        rec_amrt = "Beli Lemah (Weak Buy)"
    else:
        rec_amrt = "Jangan Beli (Hold)"

    if(unvr_total == 3):
        rec_unvr = "Beli Kuat (Strong Buy)"
    elif(unvr_total == 2):
        rec_unvr = "Beli Lemah (Weak Buy)"
    else:
        rec_unvr = "Jangan Beli (Hold)"

    if(untr_total == 3):
        rec_untr = "Beli Kuat (Strong Buy)"
    elif(untr_total == 2):
        rec_untr = "Beli Lemah (Weak Buy)"
    else:
        rec_untr = "Jangan Beli (Hold)"

    if(unvr_total == 3):
        rec_unvr = "Beli Kuat (Strong Buy)"
    elif(unvr_total == 2):
        rec_unvr = "Beli Lemah (Weak Buy)"
    else:
        rec_unvr = "Jangan Beli (Hold)"

    if(mapi_total == 3):
        rec_mapi = "Beli Kuat (Strong Buy)"
    elif(mapi_total == 2):
        rec_mapi = "Beli Lemah (Weak Buy)"
    else:
        rec_mapi = "Jangan Beli (Hold)"

    if(inkp_total == 3):
        rec_inkp = "Beli Kuat (Strong Buy)"
    elif(inkp_total == 2):
        rec_inkp = "Beli Lemah (Weak Buy)"
    else:
        rec_inkp = "Jangan Beli (Hold)"

    if(intp_total == 3):
        rec_intp = "Beli Kuat (Strong Buy)"
    elif(intp_total == 2):
        rec_intp = "Beli Lemah (Weak Buy)"
    else:
        rec_intp = "Jangan Beli (Hold)"

    if(aces_total == 3):
        rec_aces = "Beli Kuat (Strong Buy)"
    elif(aces_total == 2):
        rec_aces = "Beli Lemah (Weak Buy)"
    else:
        rec_aces = "Jangan Beli (Hold)"

    if(sido_total == 3):
        rec_sido = "Beli Kuat (Strong Buy)"
    elif(sido_total == 2):
        rec_sido = "Beli Lemah (Weak Buy)"
    else:
        rec_sido = "Jangan Beli (Hold)"

    if(hrum_total == 3):
        rec_hrum = "Beli Kuat (Strong Buy)"
    elif(hrum_total == 2):
        rec_hrum = "Beli Lemah (Weak Buy)"
    else:
        rec_hrum = "Jangan Beli (Hold)"

    return render_template('all_stock_rec_page.html', num=num,
    asii_price = asii_price, pred_asii = pred_asii, selisih_asii= selisih_asii,  rec_asii = rec_asii,
    amrt_price = amrt_price, pred_amrt = pred_amrt, selisih_amrt= selisih_amrt,  rec_amrt = rec_amrt,
    untr_price = untr_price, pred_untr = pred_untr, selisih_untr= selisih_untr,  rec_untr = rec_untr,
    unvr_price = unvr_price, pred_unvr = pred_unvr, selisih_unvr= selisih_unvr,  rec_unvr = rec_unvr,
    mapi_price = mapi_price, pred_mapi = pred_mapi, selisih_mapi= selisih_mapi,  rec_mapi = rec_mapi,
    inkp_price = inkp_price, pred_inkp = pred_inkp, selisih_inkp= selisih_inkp,  rec_inkp = rec_inkp,
    intp_price = intp_price, pred_intp = pred_intp, selisih_intp= selisih_intp,  rec_intp = rec_intp,
    aces_price = aces_price, pred_aces = pred_aces, selisih_aces= selisih_aces,  rec_aces = rec_aces,
    sido_price = sido_price, pred_sido = pred_sido, selisih_sido= selisih_sido,  rec_sido = rec_sido,
    hrum_price = hrum_price, pred_hrum = pred_hrum, selisih_hrum= selisih_hrum,  rec_hrum = rec_hrum                    
                        )


if __name__ == "__main__":
    app.run(debug=True)