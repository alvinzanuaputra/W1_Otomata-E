| Nama           | NRP        | 
| ---            | ---        | 
| Alvin Zanua Putra | 5025231064 |
| Pramudtya Faiz Ardiansyah | 5025231108 |
| Christoforus Indra Bagus Pratama | 5025231124 |
| Muhammad Azhar Aziz | 5025231131 |

# Daftar Isi
## :sparkles: Binary checker
- [Binary checker](https://github.com/alvinzanuaputra/W1_Otomata-E/blob/main/README.md#star-binary-checker)
- [Rules](https://github.com/alvinzanuaputra/W1_Otomata-E/blob/main/README.md#herb-rules)
- [Contoh](https://github.com/alvinzanuaputra/W1_Otomata-E/blob/main/README.md#herb-contoh)
- [Kode Python](https://github.com/alvinzanuaputra/W1_Otomata-E/blob/main/README.md#herb-kode-python)
- [Penjelasan Program](https://github.com/alvinzanuaputra/W1_Otomata-E/blob/main/README.md#herb-penjelasan-program)
## :sparkles: Arithmetic Expression Checker
- [Arithmetic Expression Checker](https://github.com/alvinzanuaputra/W1_Otomata-E/blob/main/README.md#star-arithmetic-expression-checker)
- [Rules](https://github.com/alvinzanuaputra/W1_Otomata-E/blob/main/README.md#herb-rules)
- [Contoh](https://github.com/alvinzanuaputra/W1_Otomata-E/blob/main/README.md#herb-contoh)
- [Kode Python](https://github.com/alvinzanuaputra/W1_Otomata-E/blob/main/README.md#herb-kode-python-1)
- [Penjelasan Program](https://github.com/alvinzanuaputra/W1_Otomata-E/blob/main/README.md#herb-penjelasan-program)
  
# :star: Binary Checker
Anda adalah seorang IT engineer yang ditugasi untuk mereview algoritma rekan anda. <br>
Fungsi algoritma ini adalah mengevaluasi sekumpulan bit biner. <br>
Apabila bit tersebut termasuk dalam S*, maka bit dianggap valid. Jika tidak, maka bit tidak valid. <br>
Diketahui bahwa S didefinisikan sebagai S = {00, 10, 010, 01001} <br>
Algoritma rekan anda sebagai berikut : <br>
 1. Cek satu persatu bit dari paling kiri. Coret deretan bit tersebut jika merupakan bagian dari S <br>
 2. Ulangi nomor (1) sampai bit habis atau sampai bit bukan bagian dari S <br>
 3. Jika yang tersisa adalah λ, maka bit valid. Jika tersisa selain λ, bit tidak valid <br>
Apakah algoritma rekan anda ini sudah benar ??? <br>

# :herb: Rules
### **1. Definisi Himpunan Valid :** 
  </t> Himpunan pola yang valid didefinisikan sebagai S = {00, 10, 010, 01001}. Artinya, hanya deretan bit yang sesuai dengan salah satu pola ini yang dianggap valid.
### **2. Pembacaan dari Kiri ke Kanan :** 
  Algoritma memproses string biner dari bagian paling kiri ke kanan. Pada setiap langkah, algoritma memeriksa apakah bagian awal (prefix) dari string sesuai dengan salah satu pola di S.
###  **3. Prioritas pada Pola Terpanjang :** 
  Saat mencocokkan, algoritma memeriksa pola-pola valid dengan urutan _dari yang terpanjang ke yang terpendek_. Pendekatan ini menghindari pencocokan awal dengan pola yang lebih pendek yang mungkin mengakibatkan sisa string tidak dapat diproses dengan benar.
###  **4. Penghapusan Pola yang Cocok :**
  Jika ditemukan bahwa awalan string sesuai dengan salah satu pola yang valid, maka bagian tersebut_ "dicoret" (dihapus)_ dari string. Proses ini diulangi untuk sisa string.
###  **5. Kondisi Validitas :**
   - Jika _seluruh string dapat dihapus_ secara berurutan menggunakan pola-pola dari S, maka string tersebut dianggap _**valid**_ (berarti string adalah bagian dari S*).
   - Jika pada suatu titik tidak ada pola yang cocok dengan awalan string, maka string dianggap _**tidak valid**_.

# :herb: Contoh
## Contoh 1 : 010010010
### Langkah 1 :
- String : 010010010
- Cek prefix : <br>
  - 01001: Apakah string diawali dengan 01001? → Ya, karena 5 bit pertama adalah 01001.
- Aksi : Hapus 01001.
- Sisa string: 0010
### Langkah 2 :
- String sisa : 0010
- Cek prefix : <br>
  - 01001 : Tidak cocok (karena string sisa hanya 4 bit).
  - 010 : Apakah 0010 diawali dengan 010? → Tidak, karena 3 bit pertama adalah 001.
  - 10 : Apakah 0010 diawali dengan 10? → Tidak, karena 2 bit pertama adalah 00.
  - 00 : Apakah 0010 diawali dengan 00? → Ya, 2 bit pertama adalah 00.
- Aksi : Hapus 00.
- Sisa string : 10
### Langkah 3 :
- String sisa: 10
- Cek prefix :
  - 01001, 010 : Tidak mungkin karena string hanya 2 bit.
  - 10 : Apakah 10 sama dengan 10? → Ya.
- Aksi : Hapus 10.
- Sisa string  λ (kosong)
### Kesimpulan
Karena seluruh string dapat dihapus menggunakan pola yang valid, maka 010010010 adalah **Valid**.

## Contoh 2 : 1010110
### Langkah 1 :
- String : 01010110
- Cek prefix :
  - 01001 : Apakah string diawali dengan 01001? → Tidak, karena 5 bit pertama adalah 01010, bukan 01001.
  - 010 : Apakah string diawali dengan 010? → Ya, 3 bit pertama adalah 010.
- Aksi : Hapus 010
- Sisa string : 10110
### Langkah 2 :
- String sisa : 10110
- Cek prefix 
  - 01001 & 010 : Tidak cocok, karena string sisa diawali dengan 1.
  - 10 : Apakah 10110 diawali dengan 10? → Ya, 2 bit pertama adalah 10.
- Aksi : Hapus 10.
- Sisa string : 110
### Langkah 3 :
- String sisa : 110
- Cek prefix :
  - 01001 & 010 : Tidak cocok karena dimulai dengan 1.
  - 10 : Apakah 110 diawali dengan 10? → Tidak, karena 2 bit pertama adalah 11.
  - 00 : Tidak cocok karena 11 tidak sama dengan 00.
- Aksi : Tidak ditemukan pola yang sesuai.
### Kesimpulan
Karena ada sisa string (110) yang tidak dapat dipotong dengan pola yang valid, maka 01010110 adalah **Tidak valid.**

# :herb: Kode Python
```
def binary_checker(s):
    # Daftar pola valid diurutkan berdasarkan panjang menurun agar pola terpanjang diutamakan
    valid_patterns = ["01001", "010", "10", "00"]
    
    # Selama string s belum kosong
    while s:
        matched = False
        # Cek setiap pola apakah menjadi prefix dari s
        for pattern in valid_patterns:
            if s.startswith(pattern):
                # Hapus pola tersebut dari s
                s = s[len(pattern):]
                matched = True
                break  # Keluar dari loop pola jika ada kecocokan
        # Jika tidak ada pola yang cocok, maka string tidak valid
        if not matched:
            return "Tidak valid"
    
    # Jika seluruh string telah terhapus (kosong), maka valid
    return "Valid"


def main():
    # User memasukkan angka biner
    binary_input = input("Masukkan bilangan biner: ")
    # Panggil fungsi binary_checker dan tampilkan hasilnya
    result = binary_checker(binary_input)
    print(result)


if __name__ == "__main__":
    main()
```
# Penjelasan Program
Berikut penjelasan alur kerja program ketika user menginputkan bilangan **010010010** :
### **1. Input dan Inisialisasi**
- User memasukkan string "010010010".
- Fungsi _binary_checker(s)_ dipanggil dengan s = "010010010".
- Daftar pola valid didefinisikan sebagai _valid_patterns_ = ["01001", "010", "10", "00"] (diurutkan dari yang terpanjang ke terpendek).
### Iterasi Pertama (s = "010010010") :
- Program memasuki loop while karena string belum kosong.
- Mulai iterasi untuk mencocokkan pola valid :
  - Pola _"01001"_ : <br>
    Cek apakah "010010010" diawali dengan "01001". <br>
    → Cocok, karena 5 karakter pertama adalah "01001".
   - Pola _"01001"_ cocok, maka dihapus dari awal string. <br>
     Sisa string menjadi: _"010010010"[5:] = "0010"_.
- Variabel matched diset ke **True** dan loop for dihentikan dengan break.
### Iterasi Kedua (s = "0010") :
- String s sekarang adalah _"0010"_.
- Masuk lagi ke dalam loop while.
- Mulai iterasi untuk mencocokkan pola : 
  - Pola _"01001"_ : <br>
    Tidak cocok, karena "0010" tidak diawali dengan _"01001"_ (terlalu pendek).
  - Pola _"010"_ : <br>
    Tidak cocok, karena "0010" diawali dengan _"00"_, bukan _"010"_.
  - Pola _"10"_ : <br>
    Tidak cocok, karena "0010" diawali dengan _"00"_, bukan _"10"_.
  - Pola _"00"_ : <br>
    Cek apakah "0010" diawali dengan _"00"_. <br>
    → Cocok.
- Pola _"00"_ cocok, maka dihapus dari awal string. <br>
  Sisa string menjadi : _"0010"[2:]_ = _"10"_.
- Variabel matched diset ke **True** dan loop for dihentikan.
### Iterasi Ketiga (s = "10") :
- String s sekarang adalah _"10"_.
- Masuk lagi ke dalam loop while.
- Mulai iterasi untuk mencocokkan pola:
  - Pola _"01001"_ : <br>
    Tidak cocok karena string hanya 2 karakter.
  - Pola _"010"_ : <br>
    Tidak cocok.
  - Pola _"10"_ : <br>
    Cek apakah "10" diawali dengan _"10"_. <br>
    → Cocok.
- Pola _"10"_ cocok, maka dihapus dari string.
- Sisa string menjadi : _"10"[2:] = ""_ (string kosong).
- Variabel matched diset ke **True** dan loop for dihentikan.
### Penyelesaian
Loop while berhenti karena string s sudah kosong. <br>
Fungsi _binary_checker_ mengembalikan **"Valid"** karena seluruh string berhasil dipotong sesuai dengan pola-pola yang ada.

# :star: Arithmetic Expression Checker
Sebagai seorang intern di software house, anda diminta membuat sebuah aturan rekursif untuk
mendefinisikan Kalimat Aritmatika. <br>
Σ = { 0 1 2 3 4 5 6 7 8 9 + - / * ( ) } <br>
Cth kalimat artimatika : ( 1 + 9 ) - ( 4 + 5 ) <br>
Cth kalimat aritmatika invalid : ( 3 + ( 4 - ) 8 ) <br> 

## :herb: Rules
###	Rule 1 (Base Case – Bilangan Dasar) :
-	Bilangan tunggal: Setiap angka tunggal (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) adalah ekspresi aritmatika yang valid.
-	Bilangan negatif tunggal: Setiap angka dengan tanda minus di depannya (misalnya, -1, -2, …, -9) juga valid.
###	Rule 2 (Pembungkusan dengan Tanda Kurung dan Negasi) :
-	Jika x adalah ekspresi aritmatika valid, maka (x) juga valid.
-	Jika x adalah ekspresi aritmatika valid, maka -(x) juga valid.
###	Rule 3 (Penggabungan dengan Operator Biner) :
Jika x dan y adalah ekspresi aritmatika valid, maka ekspresi yang menggabungkan keduanya dengan operator berikut adalah valid :
- x + y (dengan syarat: operand kanan y tidak diawali dengan tanda minus, untuk membedakan dengan negasi)
- x - y (dengan syarat yang sama: operand kanan tidak dimulai dengan tanda minus)
- x * y
- x / y

## :herb: Contoh 
### ( 4 - 3 ) + (( 9 * 2 ) / 3)
- **Iterasi 1** : Pengecekan Bilangan (Base Case) <br>
  ![( 4 - 3 ) + (( 9  2 )  3 )](https://github.com/user-attachments/assets/2722cd60-9d14-4ae2-b980-abe8a220f697) <br>
  Angka-angka : 4, 3, 9, 2, dan 3 <br>
  Semua angka tersebut termasuk dalam base (bilangan tunggal valid).
- **Iterasi 2** : Pembentukan Ekspresi Sederhana <br>
   _**Subekspresi (4-3) :**_ 
  -	Langkah 1 : Ambil 4 dan 3 yang sudah valid.
  -	Langkah 2 : Gabungkan dengan operator - menggunakan Rule 3 (x – y adalah valid) <br>
    ![( 4 - 3 ) + (( 9  2 )  3 ) (1)](https://github.com/user-attachments/assets/917b3d95-906c-4b29-8cb4-89f7792c2563) <br>
    Catatan: Pastikan operand kanan (3) tidak diawali dengan tanda - (syarat terpenuhi).
  -	Langkah 3 : Hasil 4-3 valid sebagai AE.
  -	Langkah 4 : Karena ada tanda kurung di sekelilingnya, gunakan Rule 2 (x valid, maka (x) juga valid) untuk mendapatkan (4-3) yang juga valid.<br>
  ![( 4 - 3 ) + (( 9  2 )  3 ) (2)](https://github.com/user-attachments/assets/9aa1b422-726e-41d2-928e-cfce4b68d172) <br>
   _**Subekspresi (9*2) :**_ 
  -	Langkah 1 : Ambil 9 dan 2 yang valid.
  -	Langkah 2 : Gabungkan dengan operator * menggunakan Rule 3 sehingga 9*2 valid (x * y adalah valid). <br>
    ![( 4 - 3 ) + (( 9  2 )  3 ) (3)](https://github.com/user-attachments/assets/264b486f-1bef-401c-9118-5a2c31fbdbff)
  - Langkah 3 : Bungkus dengan tanda kurung sesuai Rule 2 (x valid, maka (x) juga valid) untuk mendapatkan (9*2) yang valid. <br>
    ![( 4 - 3 ) + (( 9  2 )  3 ) (4)](https://github.com/user-attachments/assets/5566b243-1573-4938-b6c7-6dd4dff435e3)
- **Iterasi 3** : Pembentukan Ekspresi Kompleks <br>
  _**Subekspresi ((9*2) / 3) :**_
  -	Langkah 1 : Gunakan hasil (9*2) yang sudah valid sebagai x operand kiri.
  -	Langkah 2 : Operand kanan adalah 3 sebagai y (valid sebagai base).
  -	Langkah 3 : Gabungkan dengan operator / menggunakan Rule 3 sehingga (9*2)/3 valid. (x / y adalah valid). <br> 
   ![( 4 - 3 ) + (( 9  2 )  3 ) (5)](https://github.com/user-attachments/assets/f47a0438-7fb5-4b1a-8fcb-dfd262ef1f40)
  -	Langkah 4 : Bungkus hasil tersebut dengan tanda kurung menggunakan Rule 2 untuk mendapatkan ((9*2)/3) yang valid. (x valid, maka (x) juga valid) <br>
    ![( 4 - 3 ) + (( 9  2 )  3 ) (6)](https://github.com/user-attachments/assets/1404c8af-4cb1-4aa0-9ff0-2bf6f9543f17)
- **Iterasi 4** : Penggabungan Akhir <br>
  Gabungkan kedua subekspresi :
  -	Operand kiri : (4-3) sebagai x (valid) 
  -	Operand kanan : ((9*2)/3) sebagai y (valid)
  -	Operator : + <br>
    Rule 3 : Untuk operator +, pastikan operand kanan tidak dimulai dengan - (syarat terpenuhi). (x + y adalah valid). <br>
    ![( 4 - 3 ) + (( 9  2 )  3 ) (7)](https://github.com/user-attachments/assets/1ba6961c-fcbb-4e75-bf4b-1c26c9e23d9e)
-	**Hasil** : (4-3)+((9*2)/3) merupakan ekspresi aritmatika yang **valid**.
  ![( 4 - 3 ) + (( 9  2 )  3 ) (8)](https://github.com/user-attachments/assets/d943bee1-2801-4917-bddb-4edc7da89d5d)

**Kesimpulan** <br>
(4 - 3) + (( 9 * 2 ) / 3) → Valid <br>
Dikarenakan setiap subekspresi berhasil diverifikasi mulai dari bilangan dasar, pembentukan ekspresi sederhana, pembungkus dengan tanda kurung, hingga penggabungan menggunakan operator biner sesuai dengan rules.

## :herb: Kode Python

```
# Fungsi untuk mengecek apakah string s merupakan bilangan dasar (base)
# Base: bilangan tunggal (0-9) atau bilangan negatif tunggal (-1 sampai -9)
def is_base_number(s):
    s = s.strip()
    # Jika hanya 1 karakter dan merupakan digit, maka valid
    if len(s) == 1 and s.isdigit():
        return True
    # Jika ada tanda minus di depan dan 1 digit setelahnya, maka valid
    if len(s) == 2 and s[0] == '-' and s[1].isdigit():
        return True
    return False

# Fungsi untuk menghapus tanda kurung paling luar jika memang mengelilingi seluruh ekspresi.
def strip_outer_parentheses(expr):
    expr = expr.strip()
    # Jika diawali '(' dan diakhiri ')'
    if expr.startswith('(') and expr.endswith(')'):
        count = 0
        # Cek apakah tanda kurung paling luar mencakup seluruh ekspresi
        for i, char in enumerate(expr):
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
            # Jika count menjadi 0 sebelum akhir, berarti tanda kurung luar tidak mencakup seluruh ekspresi
            if count == 0 and i < len(expr) - 1:
                return expr
        # Jika sampai akhir count==0, maka hapus tanda kurung paling luar
        return expr[1:-1].strip()
    return expr

# Fungsi untuk mencari posisi operator 'op' yang berada di level tanda kurung 0 (top level)
def split_by_operator(expr, op):
    positions = []
    depth = 0  # untuk melacak kedalaman tanda kurung
    i = 0
    while i < len(expr):
        if expr[i] == '(':
            depth += 1
        elif expr[i] == ')':
            depth -= 1
        # Jika berada di level 0, periksa apakah substring dari posisi i merupakan operator op
        if depth == 0:
            if expr[i:i+len(op)] == op:
                positions.append(i)
                # Lewati karakter yang sudah dicek sebagai bagian operator
                i += len(op) - 1
        i += 1
    return positions

# Fungsi rekursif untuk mengecek validitas ekspresi aritmatika
def valid_expr(expr):
    expr = expr.strip()
    if not expr:
        return False

    # --- Iterasi 1: Pengecekan Bilangan (Base Case) ---
    if is_base_number(expr):
        # Jika ekspresi merupakan bilangan dasar (misal "4" atau "-3"), maka valid
        return True

    # --- Iterasi 2: Pengecekan Penggunaan Tanda Kurung ---
    # Jika ekspresi diawali dan diakhiri dengan tanda kurung, hapus tanda kurung tersebut
    new_expr = strip_outer_parentheses(expr)
    if new_expr != expr:
        # Lanjutkan pengecekan pada ekspresi di dalam tanda kurung
        return valid_expr(new_expr)

    # --- Iterasi 3: Pengecekan Unary Minus ---
    # Jika ekspresi diawali dengan '-' namun bukan bilangan dasar, periksa ekspresi setelah '-'
    if expr.startswith('-'):
        return valid_expr(expr[1:])

    # --- Iterasi 4: Pembentukan Ekspresi dengan Operator Biner ---
    # Daftar operator yang diperbolehkan (perhatikan '**' harus diperiksa terlebih dahulu)
    operators = ['**', '+', '-', '*', '/']
    # Lakukan iterasi untuk masing-masing operator
    for op in operators:
        # Cari posisi operator op pada level 0 (di luar tanda kurung)
        positions = split_by_operator(expr, op)
        for pos in positions:
            left = expr[:pos].strip()       # Ekspresi sebelum operator
            right = expr[pos+len(op):].strip()  # Ekspresi setelah operator

            # Untuk operator '+' dan '-', pastikan operand kanan tidak diawali tanda minus
            if op in ['+', '-'] and right.startswith('-'):
                continue

            # Jika kedua sisi (x dan y) valid, maka x op y valid sesuai Rule 3
            if valid_expr(left) and valid_expr(right):
                return True

    # Jika tidak ada aturan yang terpenuhi, ekspresi dianggap tidak valid
    return False

# Main program: meminta input dari user dan menampilkan hasil valid atau tidak valid.
if __name__ == '__main__':
    # User dapat memasukkan kalimat aritmatika (misalnya: (4-3)+((9*2)/3) atau 3-(9+)+5-3)
    expr_input = input("Masukkan kalimat aritmatika: ")
    if valid_expr(expr_input):
        print("Valid")
    else:
        print("Tidak Valid")
```
## :herb: Penjelasan Program
### 1. Panggilan Awal
- Fungsi yang dipanggil : _valid_expr(expr)_
- Input : "(4 - 3) + (( 9 * 2 ) / 3 )" <br>
- Langkah awal :
  - Ekspresi di-strip (menghilangkan spasi awal/akhir).
  - Fungsi _is_base_number(expr)_ dipanggil, tetapi karena ekspresi lebih kompleks (tidak hanya satu angka), ia mengembalikan _False_.
### 2. Pengecekan Tanda Kurung Paling Luar
- Fungsi yang dipakai : _strip_outer_parentheses(expr)_
- Proses :
  - Program mengecek apakah seluruh ekspresi diawali dan diakhiri oleh tanda kurung yang benar.
  - Karena operator + berada di luar tanda kurung, fungsi mendeteksi bahwa tanda kurung paling luar tidak mencakup seluruh ekspresi, sehingga tidak mengubah string.
- Hasil : Ekspresi tetap "(4 - 3) + (( 9 * 2 ) / 3 )".
### 3. Pengecekan Unary Minus
- Proses :
  - Program memeriksa apakah ekspresi diawali dengan tanda '-' untuk menangani kasus negasi unary.
  - Pada input ini, tidak ada unary minus di awal sehingga lanjut ke langkah berikutnya.
### 4. Pengecekan Operator Biner
- Daftar Operator : ['**', '+', '-', '*', '/']
- Iterasi atas operator :
  - Operator '**' : Tidak ditemukan pada level terluar.
  - Operator '+' :
    - Fungsi yang dipakai : _split_by_operator(expr, '+')_
    - Program melakukan scanning dari awal ke akhir dengan variabel depth untuk melacak level tanda kurung.
    - Saat depth == 0, operator + terdeteksi di antara dua subekspresi.
    - Hasil Split :
      - Operand kiri (left) : "(4 - 3)"
      - Operand kanan (right) : "(( 9 * 2 ) / 3 )"
    - Untuk operator +, dicek juga bahwa operand kanan tidak diawali tanda '-', yang terpenuhi.
### 5. Validasi Subekspresi Kiri: "(4 - 3)"
- Panggilan : _valid_expr("(4 - 3)")_
- Proses :
  - Penggunaan _strip_outer_parentheses_ :
    - Karena ekspresi diawali dan diakhiri tanda kurung yang mencakup seluruhnya, fungsi menghapus tanda kurung dan mengembalikan "4 - 3".
  - Pengecekan Operator :
    - Ekspresi "4 - 3" bukan bilangan dasar.
   - Saat iterasi operator, operator '-' terdeteksi dengan bantuan _split_by_operator("4 - 3", '-')_.
   - Split :
     - Operand kiri : "4"
     - Operand kanan : "3"
   - Validasi Base :
     - _is_base_number("4")_ dan _is_base_number("3")_ mengembalikan _True_.
   - Hasil : Subekspresi "(4 - 3)" valid.
### 6. Validasi Subekspresi Kanan: "(( 9 * 2 ) / 3 )"
- Panggilan : _valid_expr("(( 9 * 2 ) / 3 )")_
- Proses Awal :
  - Penggunaan strip_outer_parentheses : <br>
    Karena seluruh ekspresi diawali dan diakhiri tanda kurung yang mencakup seluruh string, fungsi menghapus tanda kurung paling luar dan mengembalikan :<br>
    ( 9 * 2 )  / 3
- Validasi Ekspresi "( 9 * 2 ) / 3" :
  - Ekspresi ini tidak lagi dibungkus keseluruhan oleh tanda kurung sehingga dilanjutkan ke pengecekan operator.
  - Iterasi Operator :
    - Pada iterasi operator, operator '/' ditemukan pada level 0 dengan bantuan _split_by_operator("( 9 * 2 ) / 3", '/')_.
    - Split :
      - Operand kiri : "( 9 * 2 )"
      - Operand kanan : "3"
  - Validasi Operand Kiri : "( 9 * 2 )":
    - Strip tanda kurung :
      - Panggilan strip_outer_parentheses("( 9 * 2 )") menghapus tanda kurung, menghasilkan "9 * 2".
    - Pengecekan Operator :
      - Pada "9 * 2", operator '*' ditemukan melalui _split_by_operator("9 * 2", '*')_.
      - Split :
        - Operand kiri : "9"
        - Operand kanan : "2"
      - Validasi Base :
        - _is_base_number("9")_ dan _is_base_number("2")_ mengembalikan _True_.
  - Hasil : "( 9 * 2 )" valid.
- Validasi Operand Kanan :
  - "3" merupakan bilangan dasar sehingga valid melalui _is_base_number("3")_.
- Hasil : Ekspresi "( 9 * 2 ) / 3" valid, dan dengan tanda kurung awal ("(( 9 * 2 ) / 3 )") juga valid.
### 7. Penggabungan Akhir
- Kembali ke panggilan _awal valid_expr_ :
  - Karena kedua subekspresi kiri ("(4 - 3)") dan kanan ("(( 9 * 2 ) / 3 )") valid, operator + menggabungkannya sesuai Rule 3.
- Hasil Akhir :
  - Ekspresi **"(4 - 3) + (( 9 * 2 ) / 3 )" valid**.
### Ringkasan Fungsi dan Peranannya
- _**is_base_number(s) :**_ <br>
  Mengecek apakah string s merupakan bilangan tunggal (baik digit tunggal maupun digit dengan tanda minus).
- _**strip_outer_parentheses(expr) :**_ <br>
  Menghapus tanda kurung paling luar jika seluruh ekspresi terbungkus oleh tanda kurung, sehingga pengecekan lebih dalam dapat dilakukan.
- _**split_by_operator(expr, op) :**_  <br>
  Melakukan scanning terhadap expr dan mencari posisi operator op yang berada di level tanda kurung 0 (di luar tanda kurung), untuk kemudian membagi ekspresi menjadi dua bagian (operand kiri dan kanan).
- _**valid_expr(expr) :**_ <br>
  Fungsi rekursif utama yang menggunakan langkah-langkah di atas untuk memverifikasi apakah ekspresi aritmatika valid atau tidak berdasarkan aturan (base case, penggunaan tanda kurung, penanganan unary minus, dan pembentukan ekspresi dengan operator biner).
### Kesimpulan :
Melalui iterasi-iterasi tersebut, program memecah ekspresi "(4 - 3) + (( 9 * 2 ) / 3 )" menjadi subekspresi yang lebih kecil, memvalidasi setiap bagian (baik sebagai bilangan dasar, ekspresi dalam tanda kurung, atau ekspresi operator biner), dan akhirnya memastikan bahwa seluruh kalimat aritmatika memenuhi aturan yang telah ditetapkan. Sehingga, output yang diberikan oleh program adalah "**Valid**".
