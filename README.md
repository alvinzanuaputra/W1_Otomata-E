| Nama           | NRP        | 
| ---            | ---        | 
| Alvin Zanua Putra | 5025231064 |
| Pramudtya Faiz Ardiansyah | 5025231108 |
| Christoforus Indra Bagus Pratama | 5025231124 |
| Mohammad Azhar Aziz | 5025231131 |


INI PUNYA CRISTO

Rule-Rule
	Rule 1 (Base Case – Bilangan Dasar):
-	Bilangan tunggal: Setiap angka tunggal (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) adalah ekspresi aritmatika yang valid.
-	Bilangan negatif tunggal: Setiap angka dengan tanda minus di depannya (misalnya, -1, -2, …, -9) juga valid.
	Rule 2 (Pembungkusan dengan Tanda Kurung dan Negasi):
-	Jika x adalah ekspresi aritmatika valid, maka (x) juga valid.
-	Jika x adalah ekspresi aritmatika valid, maka -(x) juga valid.
	Rule 3 (Penggabungan dengan Operator Biner):
Jika x dan y adalah ekspresi aritmatika valid, maka ekspresi yang menggabungkan keduanya dengan operator berikut adalah valid:
•	x + y (dengan syarat: operand kanan y tidak diawali dengan tanda minus, untuk membedakan dengan negasi)
•	x - y (dengan syarat yang sama: operand kanan tidak dimulai dengan tanda minus)
•	x * y
•	x / y

Contoh 
a.) ( 4 - 3 ) + (( 9 * 2 ) / 3)
 
	Iterasi 1 : Pengecekan Bilangan (Base Case)
 
Angka-angka : 4, 3, 9, 2, dan 3
Semua angka tersebut termasuk dalam base (bilangan tunggal valid).
	Iterasi 2 : Pembentukan Ekspresi Sederhana
Subekspresi (4-3) :
-	Langkah 1: Ambil 4 dan 3 yang sudah valid.
-	Langkah 2: Gabungkan dengan operator - menggunakan Rule 3 (x – y adalah valid)
 
Catatan: Pastikan operand kanan (3) tidak diawali dengan tanda - (syarat terpenuhi).
-	Langkah 3: Hasil 4-3 valid sebagai AE.
-	Langkah 4: Karena ada tanda kurung di sekelilingnya, gunakan Rule 2 (x valid, maka (x) juga valid) untuk mendapatkan (4-3) yang juga valid.
 
Subekspresi (9*2):
-	Langkah 1: Ambil 9 dan 2 yang valid.
-	Langkah 2: Gabungkan dengan operator * menggunakan Rule 3 sehingga 9*2 valid (x * y adalah valid).
 
-	Langkah 3: Bungkus dengan tanda kurung sesuai Rule 2 (x valid, maka (x) juga valid) untuk mendapatkan (9*2) yang valid.
 
	Iterasi 3: Pembentukan Ekspresi Kompleks
Subekspresi ((9*2) / 3):
-	Langkah 1: Gunakan hasil (9*2) yang sudah valid sebagai x operand kiri.
-	Langkah 2: Operand kanan adalah 3 sebagai y (valid sebagai base).
-	Langkah 3: Gabungkan dengan operator / menggunakan Rule 3 sehingga (9*2)/3 valid. (x / y adalah valid).
 
-	Langkah 4: Bungkus hasil tersebut dengan tanda kurung menggunakan Rule 2 untuk mendapatkan ((9*2)/3) yang valid. (x valid, maka (x) juga valid)
 
	Iterasi 4: Penggabungan Akhir
Gabungkan kedua subekspresi:
-	Operand kiri: (4-3) sebagai x (valid) 
-	Operand kanan: ((9*2)/3) sebagai y (valid)
-	Operator : +
Rule 3: Untuk operator +, pastikan operand kanan tidak dimulai dengan - (syarat terpenuhi). (x + y adalah valid).
 
-	Hasil : (4-3)+((9*2)/3) merupakan ekspresi aritmatika yang valid.
 
Kesimpulan
(4-3)+((9*2)/3) → Valid
(Dikarenakan setiap subekspresi berhasil diverifikasi mulai dari bilangan dasar, pembentukan ekspresi sederhana, pembungkus dengan tanda kurung, hingga penggabungan menggunakan operator biner sesuai dengan rules.)


Contoh
b.) 3 - ( 9 + ) + 5 - 3
	Iterasi 1: Pengecekan Struktur Dasar dan Bilangan (Base Case)
Angka-angka yang muncul : 3, 9, 5, dan 3
Secara individu, angka-angka tersebut valid.
	Iterasi 2: Pengecekan Penggunaan Tanda Kurung
Observasi:
-	Ekspresi diawali dengan tanda kurung buka ( pada posisi awal.
-	Masalah: Tidak terdapat tanda kurung tutup yang menyelesaikan seluruh ekspresi.
Kesimpulan Sementara: Kekurangan tanda kurung menandakan struktur tidak lengkap.
	Iterasi 3: Pengecekan Subekspresi Internal
Subekspresi (9+):
-	Langkah 1: Terdapat tanda kurung yang membuka dengan (9+ dan diikuti oleh tanda ).
-	Langkah 2: Di dalam tanda kurung, terdapat 9+.
-	Langkah 3: Menggunakan Rule 3, operator + membutuhkan dua operand:
Operand kiri: 9 (valid).
Operand kanan: Tidak ada angka atau ekspresi yang mengikuti operator +.
Kesimpulan: Karena tidak terdapat operand kedua untuk operator +, subekspresi (9+) tidak valid.
	Iterasi 4: Kesimpulan Akhir
Karena terdapat masalah struktur tanda kurung (kurang tanda kurung tutup) dan subekspresi (9+) yang tidak valid (tidak memenuhi Rule 3), maka keseluruhan kalimat aritmatika (3-(9+)+5-3 dinyatakan tidak valid.
Kode Python :


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
