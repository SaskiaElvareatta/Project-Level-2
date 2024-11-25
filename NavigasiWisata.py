import heapq

class NavigasiWisata:
    def __init__(self):
        self.graph = {
            "Museum": {"Taman Kota": 2, "Kebun Binatang": 4},
            "Taman Kota": {"Museum": 2, "Pantai": 7},
            "Pantai": {"Taman Kota": 7, "Gunung": 10, "Kebun Binatang": 6},
            "Gunung": {"Pantai": 10, "Danau": 5},
            "Danau": {"Gunung": 5},
            "Kebun Binatang": {"Museum": 4, "Pantai": 6},
        }

    def cari_rute_terpendek(self, start, end):
        queue = [(0, start, [])]  # (jarak, tempat saat ini, rute)
        visited = set()

        while queue:
            jarak, tempat, rute = heapq.heappop(queue)

            if tempat in visited:
                continue

            visited.add(tempat)
            rute = rute + [tempat]

            if tempat == end:
                return rute, jarak

            for neighbor, distance in self.graph.get(tempat, {}).items():
                if neighbor not in visited:
                    heapq.heappush(queue, (jarak + distance, neighbor, rute))

        return [], float("inf")

def main():
    navigasi = NavigasiWisata()

    print("Selamat datang di Sistem Navigasi Wisata!")
    print("Tempat yang tersedia: Museum, Taman Kota, Pantai, Gunung, Danau, Kebun Binatang")

    start = input("Masukkan tempat awal: ").strip().title()
    end = input("Masukkan tempat tujuan: ").strip().title()

    rute, jarak = navigasi.cari_rute_terpendek(start, end)

    if jarak != float("inf"):
        print(f"Rute terpendek dari {start} ke {end} adalah: {' -> '.join(rute)} dengan jarak {jarak} km.")
    else:
        print(f"Tidak ada rute yang tersedia dari {start} ke {end}. Jarak yang dicari adalah {jarak} km.")

if __name__ == "__main__":
    main()
