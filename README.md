# IMPLEMENTASI ALGORITMA A* UNTUK MENENTUKAN LINTASAN TERPENDEK
> Algoritma A* (atau A star) dapat digunakan untuk menentukan lintasan terpendek dari suatu titik ke titik lain. Pada tugas kecil 3 ini, anda diminta menentukan lintasan terpendek berdasarakan peta Google Map jalan-jalan di kota Bandung. Dari ruas-ruas jalan di peta dibentuk graf. Simpul menyatakan persilangan jalan atau ujung jalan.
Project ini merupakan bagian dari Tugas Kecil 3
mata kuliah Strategi Algoritma IF2121 Semester 2 2020/2021.

## Table of contents
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Author](#author)
* [Contact](#contact)

## Setup
Describe how to install / setup your local environement / how to run main.py
* Pertama ada install tools-tools dan library berikut pada python anda :
* Python yang digunakan adalah Python versi 3 keatas
* install pip (if not already installed)
	* https://phoenixnap.com/kb/install-pip-windows
* install matplotlib (if not already installed)
	* https://matplotlib.org/stable/users/installing.html
* install networkx (if not already installed)
	* https://riptutorial.com/networkx/example/18973/installation-or-setup

berikutnya pastikan input file txt ada dalam format berikut:
'n jumlah node'
("KoordinatXTitik1","KoordinatYTitik1") "NamaTitik1"
("KoordinatXTitik2","KoordinatYTitik2") "NamaTitik2"
("KoordinatXTitikn>,"KoordinatYTitikn") "NamaTitikn"
[ Matriks ketetanggan berbobot dengan dimensi n         ]
[ dengan tiap baris diawali dan diakhiri dengan bracket ]
[                                                       ]

sebagai contoh

8
(-6.892616,107.610423) Gerbang_Depan_ITB
(-6.890464174304161,107.60724717865062) Kebun_Binatang_Bandung
(-6.887407,107.611507) Gerbang_Belakang_ITB
(-6.886107754151466,107.60814840083982) Sabuga_ITB
(-6.886011891139484,107.61040145641657) Saraga_ITB
(-6.884371565786224,107.61305147865777) McD_Dago
(-6.893819336137485,107.61446768497895) RS_Borromeus
(-6.890591990423812,107.60992938762139) Labtek5_ITB
[0 428.35 0 0 0 0 419.13 233.94]
[428.35 0 584.79 446.03 0 0 0 0]
[0 584.79 0 427.57 193.57 0 0 398.50]
[0 446.03 427.57 0 310.81 0 0 0]
[0 0 193.57 310.81 0 339.15 0 0]
[0 0 0 0 339.15 0 1000.00 0]
[419.13 0 0 0 0 1000.00 0 0]
[233.94 0 398.50 0 0 0 0 0]

Kesalahan dalam format file.txt akan membuat program tidak berjalan dengan benar.

* jika sudah memastikan format input text, maka bisa menjalankan main.py dengan command:
* python main.py

## Status
Project is:  _finished_

## Author
M. Ibnu Syah Hafizh - (13519177)
Rayhan Asadel - (13519196)



