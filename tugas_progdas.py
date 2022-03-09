def garis():
    print("-------------------------------")

#Fungsi Bubble Sort Ascending(Dari kecil ke besar)
def sort_asc(array):
    n = len(array) #n itu adalah jumlah baris
    #perulangan pertama
    for i in range(n):
        #perulangan kedua
        for j in range(n-i-1):
            #membandingkan masing" elemen ke kanan
            if array[j] > array[j+1]:
                #jika lebih besar, tukar ke kiri
                array[j], array[j+1] = array[j+1], array[j]
    return array

#fungsi bubble sort descending (Dari besar ke kecil)
def sort_desc(array):
    n = len(array) #n itu adalah jumlah baris
    #perulangan pertama
    for i in range(n):
        #perulangan kedua
        for j in range(n-i-1):
            #membandingkan masing" elemen ke kanan
            if array[j] < array[j+1]:
                #jika lebih besar, tukar ke kiri
                array[j], array[j+1] = array[j+1], array[j]
    return array

#input nilai
garis()
print("Masukan tiga buah nilai")
#input nama
nama = (input("Masukan Nama Anda : "))
#input nilai
nilai_a = int(input("Nilai A : "))
nilai_b = int(input("Nilai B : "))
nilai_c = int(input("Nilai C : "))
nilai_d = int(input("Nilai D : "))
nilai_e = int(input("Nilai E : "))
nilai_f = int(input("Nilai F : "))
nilai_g = int(input("Nilai G : "))
nilai_h = int(input("Nilai H : "))
nilai_i = int(input("Nilai I : "))
nilai_j = int(input("Nilai J : "))
angka = [nilai_a, nilai_b, nilai_c, nilai_d, nilai_e, nilai_f, nilai_g, nilai_h, nilai_i, nilai_j]
garis()
print()

#fungsi rata rata
def rata_rata(angka):
    return sum(angka)/len(angka)

#nilai akhir
print("-----HASIL AKHIR------")
#nama
print("Nama Anda : ",(nama))
#sort
print("Urutan angka ascending : ",(sort_asc(angka)))
print("Urutan angka descending : ",(sort_desc(angka)))

#angka terbesar
print("Angka terbesar : ", max(angka))

#angka terkecil
print("Angka terkecil : ", min(angka))

#rata rata
print("Rata ratanya : ", round(rata_rata(angka),2))
