#include <iostream>
using namespace std;

int main() {
    int n;
    long long fib[200] = {0, 1, 1}; // Inisialisasi dua suku pertama Fibonacci
    long long sum = 2; // Jumlah dua suku pertama

    // Menghitung bilangan Fibonacci hingga suku ke-199
    for (int i = 3; i < 200; ++i) {
        fib[i] = fib[i - 1] + fib[i - 2];
        sum += fib[i]; // Menambahkan suku ke-i ke dalam jumlah
    }


    do {
        cout << "Masukkan nilai n (3 <= n <= 199 dan n bukan antara 100 dan 109): ";
        cin >> n;
    } while (n < 3 || n > 199 || (n > 100 && n < 110)); // Validasi input


    cout << "Bilangan Fibonacci ke-" << n << " adalah: " << fib[n] << endl;


    // Menghitung jumlah dari f_1 hingga f_n
    long long total = 0;
    for (int i = 1; i <= n; ++i) {
        total += fib[i];
    }
    

    
    cout << "Jumlah dari f_1 hingga f_" << n << " adalah: " << total << endl;


	return 0;
}