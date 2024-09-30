# Permainan Python: Cops and Robber

## _Informasi_

Permainan ini proyek dirancang oleh kami yang merupakan game kejar-kejaran yang dikembangkan menggunakan bahasa pemrograman Python dengan modul Pygame. Pemain berperan sebagai seorang Robber yang harus menghindari kejaran Polisi yang dikendalikan oleh komputer. Di sepanjang permainan, pemain akan menghadapi berbagai tantangan berupa rintangan (obstacle) yang harus dihindari, serta objek-objek yang dapat dikumpulkan untuk mendapatkan tambahan poin. Seiring dengan bertambahnya poin, tingkat kesulitan permainan akan meningkat dengan mempercepat alur permainan, sehingga memberikan tantangan yang dinamis dan menghindari permainan yang monoton.

![alt text](https://github.com/Michs09/Permainan-Cops-Robbers/blob/main/Image_Readme/Permainan.png?raw=true)

## _Sistem Permainan_
#### a) Pergerakan antar piksel
Permainan ini bersifat 2 dimensi, di mana pemain mengendalikan karakter Robber menggunakan tombol arah atas, bawah, kiri, dan kanan untuk menggerakkan posisi karakter. Pemain harus menghindari rintangan (obstacle) dan Polisi, karena jika terkena, poin akan berkurang. Selain itu, pemain juga dapat mengumpulkan objek-objek seperti harta untuk menambah poin. Pemindahan posisi karakter menjadi kunci dalam bertahan dan meraih poin di sepanjang permainan.

![alt text](https://github.com/Michs09/Permainan-Cops-Robbers/blob/main/Image_Readme/Posisi_Pemain1.png?raw=true)

#### b)	Sistem penjumlahan poin
Sistem penjumlahan poin didasarkan pada jumlah poin yang berhasil dikumpulkan oleh pemain. Pemain dapat menambah poin dengan mengambil objek harta sebanyak-banyaknya. Namun, terdapat juga rintangan (obstacle) yang dapat mengurangi poin pemain. Selain itu, jika pemain tertangkap oleh Polisi, permainan akan berakhir. Tujuan utama adalah mengumpulkan poin sebanyak mungkin sambil menghindari rintangan dan Polisi.

![alt text](https://github.com/Michs09/Permainan-Cops-Robbers/blob/main/Image_Readme/rog2.png?raw=true)

#### c)	Percepatan Alur Permainan
Selain itu, sistem permainan ini dirancang dengan pengaturan kecepatan alur, sehingga pemain tidak merasa bosan karena permainan yang monoton. Kecepatan permainan diatur berdasarkan jumlah poin yang dimiliki oleh pemain — semakin banyak poin yang dikumpulkan, semakin cepat alur permainan. Objek-objek dalam permainan akan bergerak lebih cepat, memberikan tantangan baru bagi pemain. Permainan tidak akan berhenti meskipun pemain berhasil mengumpulkan poin terbanyak, dan hanya akan berakhir jika poin pemain mencapai angka 0 atau jika pemain tertangkap oleh Polisi, yang akan menyebabkan permainan berakhir.


### Module & Library Requirements:
- Python 3.10.5
- Pygame 2.1.2
