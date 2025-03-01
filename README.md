| Nama           | NRP        | 
| ---            | ---        | 
| Alvin Zanua Putra | 5025231064 |
| Pramudtya Faiz Ardiansyah | 5025231108 |
| Christoforus Indra Bagus Pratama | 5025231124 |
| Mohammad Azhar Aziz | 5025231131 |

# Daftar Isi
1. Binary checker
## :sparkles: Arithmetic Expression Checker
- [Arithmetic Expression Checker](https://github.com/alvinzanuaputra/W1_Otomata-E/edit/main/README.md#star-arithmetic-expression-checker)
- [Rules](https://github.com/alvinzanuaputra/W1_Otomata-E/edit/main/README.md#herb-rules)
- [Contoh](https://github.com/alvinzanuaputra/W1_Otomata-E/edit/main/README.md#herb-contoh)
- [Kode Python](https://github.com/alvinzanuaputra/W1_Otomata-E/edit/main/README.md#herb-kode-python-)
- [Penjelasan Program](https://github.com/alvinzanuaputra/W1_Otomata-E/edit/main/README.md#herb-penjelasan-program)
  


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

## :herb: Kode Python :

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
