#include <iostream>
#include <cmath> // Untuk fungsi sqrt()

using namespace std;

int main() {
    double sisiAlas, tinggiLimas, luasAlas, volume, luasPermukaan, tinggiSisiTegak, luasSisiTegak;
    string nama;
    string noBP;

    // Input data
    cout << "Masukkan nama: ";
    getline(cin, nama);
    cout << "Masukkan No BP: ";
    getline(cin, noBP);
    cout << "Masukkan panjang sisi alas limas (cm): ";
    cin >> sisiAlas;
    cout << "Masukkan tinggi limas (cm): ";
    cin >> tinggiLimas;

    // Menghitung luas alas
    luasAlas = sisiAlas * sisiAlas;

    // Menghitung volume
    volume = (luasAlas * tinggiLimas) / 3;

    // Menghitung tinggi sisi tegak (menggunakan Pythagoras)
    tinggiSisiTegak = sqrt((sisiAlas / 2) * (sisiAlas / 2) + tinggiLimas * tinggiLimas);

    // Menghitung luas sisi tegak
    luasSisiTegak = (sisiAlas * tinggiSisiTegak) / 2;

    // Menghitung luas permukaan
    luasPermukaan = luasAlas + 4 * luasSisiTegak;

    // Menampilkan hasil
    cout << "\nNama: " << nama << endl;
    cout << "No BP: " << noBP << endl;
    cout << "Volume limas: " << volume << " cm^3" << endl;
    cout << "Luas permukaan limas: " << luasPermukaan << " cm^2" << endl;

    return 0;
}
