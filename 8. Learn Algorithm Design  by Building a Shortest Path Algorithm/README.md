

# Pencari Jalur Terpendek 🛤️

Selamat datang di proyek **Pencari Jalur Terpendek**! Proyek ini menyediakan implementasi algoritma **Dijkstra** dalam Python, sebuah algoritma klasik yang digunakan untuk menemukan jalur terpendek antara node-node dalam sebuah graf. Baik Anda sedang mengerjakan jaringan transportasi, peta permainan, atau sekadar menjelajahi teori graf, alat ini akan membantu Anda menemukan rute terpendek dengan mudah.

## 🚀 Eksekusi Kode

Untuk mengeksekusi Program anda bisa meng-clone repository ini atau anda juga bisa menyalin kode di bawah ini dan jalankan di Python Environment Anda.

```bash
$ git clone https://github.com/HaikalAkbar13/Scientific_Computing_with_Python_fCC/tree/main/8.%20Learn%20Algorithm%20Design%20%20by%20Building%20a%20Shortest%20Path%20Algorithm
```

```python
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target=''):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)
    
    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)
    
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} jarak: {distances[node]}\nJalur: {" -> ".join(paths[node])}')
    
    return distances, paths
    
shortest_path(my_graph, 'A', 'F')
```

## 💡 How it works?

### Input:
- **Representasi Graf**: Graf direpresentasikan sebagai dictionary di mana setiap kunci adalah node, dan nilainya adalah daftar tuple. Setiap tuple berisi node tetangga dan jarak (atau bobot) ke tetangga tersebut.
  
  Contoh:
  ```python
  my_graph = {
      'A': [('B', 5), ('C', 3), ('E', 11)],
      'B': [('A', 5), ('C', 1), ('F', 2)],
      'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
      'D': [('C', 1), ('E', 9), ('F', 3)],
      'E': [('A', 11), ('C', 5), ('D', 9)],
      'F': [('B', 2), ('D', 3)]
  }
  ```

- **Node Awal**: Algoritma memulai pencarian dari node ini.
  
- **Node Tujuan (Opsional)**: Jika diberikan, fungsi akan mencetak jalur terpendek dan jarak ke node ini secara spesifik. Jika tidak diberikan, fungsi akan menghitung jalur terpendek ke semua node.

### Output:
- **Distances**: Sebuah dictionary di mana setiap kunci adalah node, dan nilainya adalah jarak terpendek dari node awal.
  
- **Paths**: Sebuah dictionary di mana setiap kunci adalah node, dan nilainya adalah daftar yang merepresentasikan jalur terpendek dari node awal.

### Contoh Output:
Jika Anda menjalankan fungsi dengan graf contoh dan menentukan node awal sebagai `A` dan node tujuan sebagai `F`, hasilnya mungkin seperti ini:

```
A-F jarak: 7
Jalur: A -> B -> F
```

Artinya, jalur terpendek dari `A` ke `F` adalah sejauh `7` unit, melalui jalur `A -> B -> F`.

## 🔍 Penjelasan Detail

### Langkah 1: Inisialisasi
- **Unvisited Nodes**: Semua node dalam graf awalnya dianggap belum dikunjungi.
- **Distances Dictionary**: Dimulai dengan jarak `0` untuk node awal dan `infinity` untuk semua node lainnya.
- **Paths Dictionary**: Dimulai dengan jalur kosong untuk setiap node, lalu menambahkan node awal ke jalurnya sendiri.

### Langkah 2: Loop Utama (Mencari Jalur Terpendek)
- **Pilih Node Saat Ini**: Pilih node yang belum dikunjungi dengan jarak terpendek yang diketahui.
- **Perbarui Jarak**: Untuk setiap node tetangga, hitung jarak baru yang mungkin melalui node saat ini. Jika jarak baru ini lebih pendek, perbarui jarak dan jalur untuk tetangga tersebut.
- **Tandai Node sebagai Telah Dikunjungi**: Setelah node diproses, hapus node tersebut dari daftar node yang belum dikunjungi.

### Langkah 3: Cetak Hasil
- **Cetak Jalur Tujuan**: Jika node tujuan ditentukan, cetak jalur terpendek dan jarak ke node tersebut.
- **Kembalikan Jarak dan Jalur**: Fungsi ini mengembalikan dua dictionary: satu berisi jarak terpendek dan satu lagi berisi jalur dari node awal ke semua node.

## ✨ Fitur

- **Efisien**: Menggunakan algoritma Dijkstra untuk memastikan Anda mendapatkan jalur terpendek dalam waktu tercepat.
- **Fleksibel**: Mendukung graf berarah atau tak berarah dengan bobot non-negatif.
- **Informative**: Menyediakan baik jalur terpendek maupun jarak ke tujuan Anda.

## 🛠️ Persyaratan

Anda memerlukan Python 3.x untuk menjalankan kode ini. Tidak ada dependensi eksternal yang diperlukan, sehingga Anda dapat menjalankannya langsung setelah menginstal Python.

---

Selamat mencoba! 🚀
```

### **Penjelasan:**
- **Pengenalan Menarik**: Bagian awal README menjelaskan secara singkat fungsi dan kegunaan proyek, menarik minat pembaca untuk melihat lebih lanjut.
- **Panduan Cepat**: Contoh kode disertakan langsung di bagian atas sehingga pengguna bisa langsung mencobanya tanpa harus membaca seluruh penjelasan.
- **Penjelasan Detail**: Setiap bagian dari fungsi `shortest_path` dijelaskan secara rinci, mulai dari input, output, hingga proses di dalam loop.
- **Fitur dan Persyaratan**: Menyebutkan fitur utama dan persyaratan yang dibutuhkan untuk menjalankan kode, membantu pengguna mengetahui apa yang diperlukan dan apa yang bisa diharapkan dari proyek ini.

Dengan struktur ini, pembaca yang mungkin baru mengenal algoritma Dijkstra atau pemrograman graf akan lebih mudah memahami bagaimana fungsi bekerja dan bagaimana mereka bisa menggunakannya dalam proyek mereka sendiri.
