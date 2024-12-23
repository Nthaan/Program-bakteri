import time
import sys 

sys.setrecursionlimit(100000000)


def hitung_bakteri_iteratif(n):
    return 2 ** n

def hitung_bakteri_rekursif(n):
    if n == 0:
        return 1
    else:
        return 2 * hitung_bakteri_rekursif(n - 1)


def analisis_pertumbuhan_bakteri(n):
    start_iteratif = time.time()
    hasil_iteratif = hitung_bakteri_iteratif(n)
    end_iteratif = time.time()
    waktu_iteratif = end_iteratif - start_iteratif

    start_rekursif = time.time()
    hasil_rekursif = hitung_bakteri_rekursif(n)
    end_rekursif = time.time()
    waktu_rekursif = end_rekursif - start_rekursif


    print(f"Jumlah bakteri setelah {n} periode waktu (iteratif): {hasil_iteratif}, waktu: {waktu_iteratif:.10f} detik")
    print(f"Jumlah bakteri setelah {n} periode waktu (rekursif): {hasil_rekursif}, waktu: {waktu_rekursif:.10f} detik")


if __name__ == "__main__":
    n = int(input("Masukkan jumlah periode waktu (n): "))
    analisis_pertumbuhan_bakteri(n)