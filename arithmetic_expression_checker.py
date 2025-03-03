# Fungsi untuk mengecek apakah string s merupakan bilangan dasar (base)
# Base: bilangan (dapat berupa multi-digit) atau bilangan negatif
def is_base_number(s):
    s = s.strip()
    if not s:
        return False

    # Menghapus tanda minus untuk pengecekan
    if s.startswith("-"):
        s = s[1:]  # Menghapus tanda minus untuk pengecekan
        if not s:  # Jika hanya tanda minus
            return False

    return True


# Fungsi untuk menghapus tanda kurung paling luar jika memang mengelilingi seluruh ekspresi.
def strip_outer_parentheses(expr):
    expr = expr.strip()
    # Jika diawali '(' dan diakhiri ')'
    if expr.startswith("(") and expr.endswith(")"):
        count = 0
        # Cek apakah tanda kurung paling luar mencakup seluruh ekspresi
        for i, char in enumerate(expr):
            if char == "(":
                count += 1
            elif char == ")":
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
        if expr[i] == "(":
            depth += 1
        elif expr[i] == ")":
            depth -= 1
        # Jika berada di level 0, periksa apakah substring dari posisi i merupakan operator op
        if depth == 0:
            if expr[i : i + len(op)] == op:
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
        # Jika ekspresi merupakan bilangan (termasuk multi-digit dan desimal), maka valid
        return True

    # --- Iterasi 2: Pengecekan Penggunaan Tanda Kurung ---
    # Jika ekspresi diawali dan diakhiri dengan tanda kurung, hapus tanda kurung tersebut
    new_expr = strip_outer_parentheses(expr)
    if new_expr != expr:
        # Lanjutkan pengecekan pada ekspresi di dalam tanda kurung
        return valid_expr(new_expr)

    # --- Iterasi 3: Pengecekan Unary Minus ---
    # Jika ekspresi diawali dengan '-' namun bukan bilangan dasar, periksa ekspresi setelah '-'
    if expr.startswith("-"):
        return valid_expr(expr[1:])

    # --- Iterasi 4: Pembentukan Ekspresi dengan Operator Biner ---
    # Daftar operator yang diperbolehkan (perhatikan '**' harus diperiksa terlebih dahulu)
    operators = ["**", "+", "-", "*", "/"]
    # Lakukan iterasi untuk masing-masing operator
    for op in operators:
        # Cari posisi operator op pada level 0 (di luar tanda kurung)
        positions = split_by_operator(expr, op)
        for pos in positions:
            left = expr[:pos].strip()  # Ekspresi sebelum operator
            right = expr[pos + len(op) :].strip()  # Ekspresi setelah operator

            # Untuk operator '+' dan '-', pastikan operand kanan tidak diawali tanda minus
            if op in ["+", "-"] and right.startswith("-"):
                continue

            # Jika kedua sisi (x dan y) valid, maka x op y valid sesuai Rule 3
            if valid_expr(left) and valid_expr(right):
                return True

    # Jika tidak ada aturan yang terpenuhi, ekspresi dianggap tidak valid
    return False


# Main program: meminta input dari user dan menampilkan hasil valid atau tidak valid.
if __name__ == "__main__":
    # User dapat memasukkan kalimat aritmatika (misalnya: (14-3)+((19.5*2)/3) atau 13-(9+)+5-3)
    expr_input = input("Masukkan kalimat aritmatika: ")
    if valid_expr(expr_input):
        print("Valid")
    else:
        print("Tidak Valid")
