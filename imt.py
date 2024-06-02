def luas_area_tubuh(a, b, t):
    """
    Menghitung luas area tubuh manusia menggunakan rumus:
    Luas permukaan elips (BSA) = (π/2) * (a * b) + (π/2) * (a + b) * t

    Parameters:
    a (float): lebar tubuh tampak depan dalam cm
    b (float): lebar tubuh tampak samping dalam cm
    t (float): tinggi tubuh manusia dalam cm

    Returns:
    float: luas area tubuh manusia dalam meter persegi
    """
    import math

    # Konversi dari cm ke meter
    a = a / 100
    b = b / 100
    t = t / 100

    # Konstanta π
    pi = math.pi

    # Menghitung luas area tubuh
    luas_area = (pi / 2) * (a * b) + (pi / 2) * (a + b) * t

    return luas_area

def hitung_berat_badan(bsa, t):
    """
    Menghitung berat badan manusia menggunakan rumus:
    Berat badan = (BSA^2 * 3600) / tinggi badan

    Parameters:
    bsa (float): luas permukaan tubuh manusia (BSA) dalam meter persegi
    t (float): tinggi tubuh manusia dalam cm

    Returns:
    float: berat badan manusia dalam kilogram
    """

    berat_badan = (bsa ** 2 * 3600) / t
    return berat_badan

def hitung_imt(berat_badan, tinggi_badan):
    """
    Menghitung Indeks Massa Tubuh (IMT) dan menentukan kategori IMT.

    Parameters:
    berat_badan (float): Berat badan dalam kilogram
    tinggi_badan (float): Tinggi badan dalam sentimeter

    Returns:
    float: Nilai IMT
    str: Kategori IMT
    """
    # Konversi tinggi dari cm ke meter
    tinggi_badan_meter = tinggi_badan / 100

    # Menghitung IMT
    imt = berat_badan / (tinggi_badan_meter ** 2)

    # Menentukan kategori IMT
    if imt < 18.5:
        kategori = "Berat Badan Kurang"
    elif 18.5 <= imt < 25:
        kategori = "Berat Badan Ideal"
    elif 25 <= imt < 30:
        kategori = "Berat Badan Lebih"
    elif 30 <= imt < 40:
        kategori = "Obesitas I"
    else:
        kategori = "Obesitas II"

    return imt, kategori