def akhir(V0, a, t):
    """Fungsi ini dapat digunakan dalam menghitung kecepatan akhir pada GLBB
    Argument:
        V0 (float/int): Kecepatan Awal
        a (float/int): Percepatan
        t (float/int): Waktu
    Return:
        Vt (float): Hasil perhitungan kecepatan akhir
    """
    Vt = V0 + a*t
    return Vt

def jarak(V0, t, a):
    """Fungsi ini dapat digunakan dalam menghitung jarak pada GLBB
    Argument:
        V0 (float/int): Kecepatan Awal
        t (float/int): Waktu
        a (float/int): Percepatan
    Return:
        s (float): Hasil perhitungan jarak
    """
    s = V0*t + ((a*(t**2))/2)
    return s