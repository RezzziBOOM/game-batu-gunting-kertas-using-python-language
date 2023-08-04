import random
print("==== Oh Iya jadi ronde ya di itung setiap kamu keluar dari permainaanya ====")
print("==== Jadi setiap ronde kamu bebas mau main berapa kali sama computer ====")
def tampilkan_pilihan():
    print("""
    =================================================
        MAIN GAME GUNTING BATU KERTAS YOK!!!! 
                        RezzziBOOM
    =================================================
    Kode |                Pilihan                    |     
    -------------------------------------------------
    1.                      GUNTING           
    2.                        BATU              
    3.                       KERTAS
    0.                  KELUAR PERMAINAN                      
    =================================================
    """)

def permainan():
    global skor_pemain, skor_komputer  

    while True:
        tampilkan_pilihan()
        print(f"Pemain [{skor_pemain}]:[{skor_komputer}] Komputer")

        pilihan_str = {1: "Gunting", 2: "Batu", 3: "Kertas"}
        for x in range(1, 4):
            print(f"{x}. {pilihan_str[x]}")

        print("0. Keluar Permainan")

        while True:
            try:
                pilihan = int(input(">> "))
                if pilihan in [0, 1, 2, 3]:
                    break
                else:
                    print("Pilihan tidak valid! Silakan pilih angka 1, 2, 3, atau 0 (Keluar).")
            except ValueError:
                print("Masukan harus berupa angka!")

        if pilihan == 0:
            break
        elif pilihan == 4:
            print("Permainan telah selesai. Skor akhir:")
            print(f"Pemain: {skor_pemain} Komputer: {skor_komputer}")
            return

        print(f"Kamu Memilih {pilihan_str[pilihan]} ")

        pilihan_komputer = random.randint(1, 3)
        print(f"Komputer Memilih {pilihan_str[pilihan_komputer]}")

        if pilihan == pilihan_komputer:
            print("Hasilnya Seri")
        elif (pilihan == 1 and pilihan_komputer == 3) or (pilihan == 2 and pilihan_komputer == 1) or (pilihan == 3 and pilihan_komputer == 2):
            print("Kamu Menang")
            skor_pemain += 1
        else:
            print("Komputer Menang")
            skor_komputer += 1

        input("Tekan Enter Untuk Lanjut...")


skor_akhir_pemain = 0
skor_akhir_komputer = 0

# Main program
n_permainan = int(input("Lu Mau Main Berapa Ronde Ama BOT Gua? "))

for i in range(n_permainan):
    skor_pemain = 0
    skor_komputer = 0

    print(f"================ Permainan ke-{i+1} ================")
    permainan()
    print(f"Skor sementara setelah permainan ke-{i+1}:")
    print(f"Skor Kamu: {skor_pemain} Skor Komputer: {skor_komputer}")

    # Menyimpan skor akhir dari setiap ronde
    skor_akhir_pemain += skor_pemain
    skor_akhir_komputer += skor_komputer

print("Permainan selesai. Terima kasih telah bermain!")
print(f"Skor Akhir Kamu: {skor_akhir_pemain} Skor Akhir Komputer: {skor_akhir_komputer}")

if skor_akhir_pemain > skor_akhir_komputer:
    print("Selamat! Kamu Menang! NAH GITU DONG LAWAN BOT MASA KALAH!!!.")
elif skor_akhir_pemain < skor_akhir_komputer:
    print("Sayang sekali, AELA NOB BANGET LU LAWAN BOT GUA AJA KALAH!!!.")
else:
    print("Hasilnya Seri! AELA NOB BANGET LU LAWAN BOT GUA AJA SERI!!!.")
