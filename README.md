# Pengembangan Sistem Rekomendasi Keputusan Dagang dengan Prediksi Harga Saham dan Laporan Keuangan Emiten
Aplikasi ini diberi nama FinanFreeVest yang merupakan kepanjangan dari "Financial Freedom Invest" yang menunjukkan makna dari kegiatan investasi yang bertujuan untuk mencapai kebebasan finansial. Aplikasi ini merupakan aplikasi yang dapat memberikan rekomendasi keputusan dalam hal kegiatan jual-beli saham. <br>
Tampilan awal dari aplikasi tersebut adalah sebagai berikut.
![alt text](https://raw.githubusercontent.com/melikacandra/stock_trade_decision_reccomendation/refs/heads/main/gambar/halaman-utama.png)



## Deskripsi Fungsi

Aplikasi ini merupakan aplikasi berbasis web yang berfungsi untuk memberikan rekomendasi keputusan dalam hal kegiatan jual-beli saham. Rekomendasi yang diberikan berupa rekomendasi untuk membeli (buy) atau menahan untuk tidak membeli (hold) saham tertentu. Jenis rekomendasi yang diberikan terdapat 3 jenis yakni:
* Beli Kuat (Strong Buy)
* Beli Lemah (Weak Buy)
* Jangan Beli (Hold) <br>
<p> Hasil rekomendasi dihasilkan dari analisis fundamental dan analisis teknikal. Analisis fundamental dihasilkan dari rasio-rasio laporan keuangan, sedangkan analisis teknikal dihasilkan dari prediksi harga saham yang memanfaatkan deep learning dengan arsitektur LSTM (Long Short Term Memory). Kombinasi dari kedua analisis ini menghasikan rekomendasi harga saham. Pada aplikasi ini digunakan 10 sampel emiten dari bursa saham Indonesia berdasarkan Indeks LQ45 (bluechip). Emiten tersebut antara lain: ASII, AMRT, UNTR, UNVR, MAPI, INKP, INTP, ACES, SIDO, dan HRUM. </p>

## Cara Instalasi
Aplikasi ini menggunakan framework Flask yang berbasis python dalam pengembangannya. Untuk memastikan aplikasi ini dapat berjalan dengan baik. Terdapat beberapa hal yang perlu di install terlebih dahulu. Hal yang perlu di install beserta cara install nya adalah sebagai berikut:
* Python versi 3.8.9 <br>
Download versi python ini di link [berikut](https://www.python.org/downloads/release/python-389/)
* Flask versi 3.0.3 <br>
masukkan command ini di terminal:
```
pip install flask==3.0.3
```
* Tensorflow versi 2.13.0 <br>
masukkan command ini di terminal:
```
pip install tensorflow==2.13.0
```
* Pandas versi 2.0.3 <br>
masukkan command ini di terminal:
```
pip install pandas==2.0.3
```
* Matplotlib versi 3.7.5 <br>
masukkan command ini di terminal:
```
pip install matplotlib==3.7.5
```
* Seaborn versi 0.13.2 <br>
masukkan command ini di terminal:
```
pip install seaborn==0.13.2
```
* Scikit-learn versi 1.3.2 <br>
masukkan command ini di terminal:
```
pip install scikit-learn==1.3.2
```
## Cara Menggunakan Aplikasi
Tutorial untuk menggunakan aplikasi adalah sebagai berikut.
1. Set Up Aplikasi <br>
Hal yang perlu dilakukan pertama kali adalah mengubah posisi direktori. Dengan asumsi awal pengguna berada di direktori awal, maka perlu dilakukan perpindahan ke direktori yang berisi program aplikasi web. Cara masuk ke dalam direktori program aplikasi web dengan memanfaatkan terminal adalah dengan memasukkan command berikut pada terminal:
```
cd .\kode-program\perangkat-lunak-sistem-rekomendasi\
```
Setelah masuk ke direktori `perangkat-lunak-sistem-rekomendasi` maka aplikasi web dapat dijalankan. Aplikasi web ini dijalankan dengan memasukkan command berikut pada terminal:
```
flask run
```
tunggu sebentar, maka akan menghasilkan keterangan berikut pada terminal
```
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
Aplikasi web dapat dilihat di alamat `http://127.0.0.1:5000`. Salin atau klik link tersebut sehingga browser terbuka. Maka aplikasi web yang ditampilkan adalah sebagai berikut.
![alt text](https://raw.githubusercontent.com/melikacandra/stock_trade_decision_reccomendation/refs/heads/main/gambar/halaman-utama.png)
Jika anda ingin mematikan aplikasi, masuk ke terminal dan tekal tombol `Ctrl + C` pada keyboard. Maka aplikasi akan mati dan alamat `http://127.0.0.1:5000` tidak dapat diakses.
![alt text](https://raw.githubusercontent.com/melikacandra/stock_trade_decision_reccomendation/refs/heads/main/gambar/halaman-tak-dapat-akses.png)
2. Penggunaan Aplikasi <br>
Bagian ini menjelaskan tentang penggunaan aplikasi web. Terdapat dua hal yang dapat dilakukan yakni melakukan rekomendasi untuk semua emiten, dan prediksi untuk salah satu emiten.
* Prediksi untuk Semua Emiten <br>
Hal yang perlu dilakukan adalah mengisi formulir yang berada di sebelah kiri halaman utama. maka pada isian dengan judul `Saham mana yang ingin anda lihat rekomendasinya?` pilih `Semua`. Lalu, pada isian dengan judul `Ànda ingin memprediksi harga saham ini untuk berapa hari kedepan?` pilih jumlah hari yang ingin anda prediksi. Setelah itu tekan tombol `Rekomendasikan Sekarang`. <br>
 Misalnya pada contoh di bawah, pengguna ingin melihat rekomendasi saham pada 3 hari kedepan. Maka isian yang dilakukan pada formulir adalah sebagai berikut.
yang ditampilkan adalah sebagai berikut.
![alt text](https://raw.githubusercontent.com/melikacandra/stock_trade_decision_reccomendation/refs/heads/main/gambar/prediksi-semua.png)
<br> Lalu, pengguna perlu menunggu terlebih dahulu. Hasil yang akan ditampilkan akan seperti pada gambar berikut.
![alt text](https://raw.githubusercontent.com/melikacandra/stock_trade_decision_reccomendation/refs/heads/main/gambar/hasil-prediksi-semua.png)

* Prediksi untuk Salah Satu Emiten <br>
Hal yang perlu dilakukan adalah mengisi formulir yang berada di sebelah kiri halaman utama. maka pada isian dengan judul `Saham mana yang ingin anda lihat rekomendasinya?` pilih salah satu kode saham yang tersedia. Lalu, pada isian dengan judul `Ànda ingin memprediksi harga saham ini untuk berapa hari kedepan?` pilih jumlah hari yang ingin anda prediksi. Setelah itu tekan tombol `Rekomendasikan Sekarang`. <br>
Misalnya pada contoh di bawah, pengguna ingin melihat rekomendasi saham `UNVR` pada 5 hari kedepan. Maka isian yang dilakukan pada formulir adalah sebagai berikut.
yang ditampilkan adalah sebagai berikut.
![alt text](https://raw.githubusercontent.com/melikacandra/stock_trade_decision_reccomendation/refs/heads/main/gambar/prediksi-salah-satu.png)
<br>
<p> Lalu, pengguna perlu menunggu terlebih dahulu. Hasil yang akan ditampilkan akan seperti pada gambar berikut.</p>

![alt text](https://raw.githubusercontent.com/melikacandra/stock_trade_decision_reccomendation/refs/heads/main/gambar/hasil-prediksi-salah-satu.png)


## Credit
Proyek ini dibuat oleh Ni Luh Melika Candra Widyani Mas dalam rangka tugas akhir untuk meraih gelar sarjana di bidang Informatika dari Universitas Katolik Parahyangan. Direktori ini terdiri atas dokumen dan kode program dari proyek tersebut. Versi terupdate dari proyek ini dapat diakses melalui https://github.com/melikacandra/stock_trade_decision_reccomendation. 