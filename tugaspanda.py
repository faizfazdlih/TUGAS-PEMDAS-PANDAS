import pandas as pd

#1  Pastikan kolom-kolomnya menyertakan nama Kabupaten/Kota, jumlah produksi sampah (dalam ton), dan tahun pencatatan

df_csv = pd.read_csv('sampah_disperkim.csv')
df_disperkim = pd.DataFrame(df_csv, columns=['nama_kabupaten_kota','jumlah_produksi_sampah','satuan','tahun'])
df_disperkim
print(df_disperkim)

#2  Hitunglah total produksi sampah di seluruh Kabupaten/Kota di Jawa Barat untuk tahun tertentu
tahun = 2015

total = 0
for i,j in df_csv.iterrows():
    if j['tahun'] == tahun:
        total += j['jumlah_produksi_sampah']
print(f"Total produksi sampah di seluruh Kabupaten/Kota di Jawa Barat pada tahun {tahun} : {total} ton")


#3 Jumlahkan Data Pertahun
data = {}

for i, j in df_csv.iterrows():
    tahun = j['tahun']
    produksi = j['jumlah_produksi_sampah']
    if tahun in data:
        data[tahun] += produksi
    else:
        data[tahun] = produksi

for tahun,jumlah in data.items():
    print(f"Jumlah data tahun {tahun} : {jumlah} ton")

#4 Jumlahkan data per Kota/Kabupaten per tahun
data = {}

for i, j in df_csv.iterrows():
    kota = j['nama_kabupaten_kota']
    tahun = j['tahun']
    jumlah = j['jumlah_produksi_sampah']
    if kota not in data:
        data[kota] = {}
    if kota not in data[kota]:
        data[kota][tahun] = 0
    data[kota][tahun] += j['jumlah_produksi_sampah']

for kota, data_kota in data.items():
    print(f'{kota} : ')
    for tahun, banyak in data_kota.items():
        print(f'Jumah data per Kota/Kabupaten {tahun} per {banyak}')

#Export hasil akhir menjadi CSV dan Excel
df_csv.to_csv('hasil_akhir.csv', index=False)
df_csv.to_excel('hasil_akhir.xlsx', index=False)
print('Data sudah ditambahkan dalam bentuk csv dan xlsx')