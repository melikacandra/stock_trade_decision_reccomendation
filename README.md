# Pengembangan Sistem Rekomendasi Keputusan Dagang dengan Prediksi Harga Saham dan Laporan Keuangan Emiten

Proyek ini dibuat oleh Ni Luh Melika Candra Widyani Mas dalam rangka tugas akhir untuk meraih gelar sarjana di bidang Informatika dari Universitas Katolik Parahyangan. Direktori ini terdiri atas dokumen dan kode program dari proyek tersebut. Versi terupdate dari proyek ini dapat diakses melalui https://github.com/melikacandra/stock_trade_decision_reccomendation.
Aplikasi ini diberi nama FinanFreeVest yang merupakan kepanjangan dari "Financial Freedom Invest" yang menunjukkan makna dari kegiatan investasi yang bertujuan untuk mencapai kebebasan finansial (financial freedom)

## Deskripsi Fungsi

Aplikasi ini merupakan aplikasi berbasis web yang berfungsi untuk memberikan rekomendasi keputusan dalam hal kegiatan jual-beli saham. Rekomendasi yang diberikan berupa rekomendasi untuk membeli (buy) atau menahan untuk tidak membeli (hold) saham tertentu. Jenis rekomendasi yang diberikan terdapat 3 jenis yakni:
- Beli Kuat (Strong Buy)
- Beli Lemah (Weak Buy)
- Jangan Beli (Hold)
Hasil rekomendasi dihasilkan dari analisis fundamental dan analisis teknikal. Analisis fundamental dihasilkan dari rasio-rasio laporan keuangan, sedangkan analisis teknikal dihasilkan dari prediksi harga saham yang memanfaatkan deep learning dengan arsitektur LSTM (Long Short Term Memory). Kombinasi dari kedua analisis ini menghasikan rekomendasi harga saham. Pada aplikasi ini digunakan 10 sampel emiten dari bursa saham Indonesia berdasarkan Indeks LQ45 (bluechip). Emiten tersebut antara lain: ASII, AMRT, UNTR, UNVR, MAPI, INKP, INTP, ACES, SIDO, dan HRUM.

## Cara Instalasi
Aplikasi ini menggunakan framework Flask yang berbasis python dalam pengembangannya. Untuk memastikan aplikasi ini dapat berjalan dengan baik. Terdapat beberapa hal yang perlu di install terlebih dahulu. Hal yang perlu di install beserta cara install nya adalah sebagai berikut:
- Python versi
- Flask versi
- Tensorflow versi
- Pandas versi
- Matplotlib versi
- Seaborn versi

## Cara Menggunakan Aplikasi
Tutorial untuk menggunakan aplikasi adalah sebagai berikut.
1. Set Up Aplikasi
2. Penggunaan Aplikasi
a. Prediksi untuk Semua Emiten
b. Prediksi untuk Salah Satu Emiten