from models.parkir import Parkir

def main():
    parkir = Parkir()

    # Memulai proses parkir
    parkir.mulai_parkir("karin", "2024-06-08 08:00", "Mobil")
    parkir.mulai_parkir("putri", "2024-06-08 09:00", "Motor")

    # Mengakhiri proses parkir
    parkir.akhir_parkir("karin", "2024-06-08 12:00")
    parkir.akhir_parkir("putri", "2024-06-08 10:00")

    # Menghitung dan menampilkan biaya parkir
    parkir.hitung_biaya("karin")
    parkir.hitung_biaya("putri")

if __name__ == "__main__":
    main()
