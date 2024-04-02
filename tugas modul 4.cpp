#include <iostream>
#include <string>
using namespace std;

bool hurufVokal(char n) {
    n = tolower(n);
    return (n == 'a' || n == 'e' || n == 'i' || n == 'o' || n == 'u');
}

string gantihurufvokaldengani(string lyrics) {
    for (char& n : lyrics) {
        if (hurufVokal(n)) {
            n = 'i';
        }
    }
    return lyrics;
}

int main() {
    string lyrics;
    cout << "  __________________________________________________\n" ;
	cout << " |                                                  |\n" ;
	cout << " |      {Welcome To The Chenged Song Lyrics}        |\n" ;
	cout << " |__________________________________________________|\n" ;
	cout << "\n ";
	cout << "\n ";
	cout << "_____________________________________________________\n";
	cout << " Masukkan Teks Lirik Lagu Yang Akan diubah: \n ";
	cout << " \n ";
	cout << " Before : ";
 	getline(cin, lyrics);
	
    string ubahlirik = gantihurufvokaldengani(lyrics);

    cout << " After :  " << ubahlirik << endl;
	cout << " Thank you! ";
    return 0;
}