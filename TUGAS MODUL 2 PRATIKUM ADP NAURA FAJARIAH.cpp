#include <iostream>

using namespace std;

int main(){
    int tujuan, kelas, tiket, harga, hkelas, hargad;
    string ntujuan, nclass, ndiskon;
    cout<< "Selamat datang di pemesanan tiket Bus PT ANS Lintas-Sumatera\n";
    cout<< "Tujuan yang dipilih:\n1.Medan:Rp70000\n2.Padang:Rp50000\n3.Jambi:Rp30000\n4.Pekanbaru:Rp40000\n5.Bengkulu:Rp60000\n6.Palembang:Rp80000\nPilih(1-6):\n";
    cin>>tujuan;
    if (tujuan==1){harga=70000;ntujuan="Medan";}
    else if (tujuan==2){harga=50000;ntujuan="Padang";}
    else if (tujuan==3){harga=30000;ntujuan="Jambi";}
    else if (tujuan==4){harga=40000;ntujuan="Pekanbaru";}
    else if (tujuan==5){harga=60000;ntujuan="Bengkulu";}
    else if (tujuan==6){harga=80000;ntujuan="Palembang";}
    else {"error";}
cout<<"---------------------------------------------------------------------------------------------------------------\n";


    cout<< "Kelas yang dipilih:\n1.Ekonomi Class:Rp10000\n2.Bisnis Class:Rp20000\n3.First Class:Rp30000\n(Pilih 1-3):\n";
    cin>> kelas;
    if (kelas==1){hkelas=10000;nclass="Ekonomi Class";}
    else if (kelas==2){hkelas=20000;nclass="Bisnis Class";}
    else if (kelas==3){hkelas=30000;nclass="First Class";}
    else {"error";}

cout<<"---------------------------------------------------------------------------------------------------------------\n";
    cout<< "Jumlah Tiket: ";cin>>tiket;
cout<<"---------------------------------------------------------------------------------------------------------------\n";

    if (tiket>=3&&tiket<=5){hargad=tiket*(harga+hkelas)*95/100;ndiskon="5%";}
    else if (tiket>5){hargad=tiket*(harga+hkelas)*90/100;ndiskon="10%";}
    cout<< "Tujuan               : "<<ntujuan<<endl;
    cout<< "Kelas                : "<<nclass<<endl;
    cout<< "Jumlah Tiket         : "<<tiket<<endl;
    cout<< "Total                : Rp"<<tiket*(harga+hkelas)<<endl;
    cout<< "Diskon               : "<<ndiskon<<endl;
    cout<< "Total Setelah Diskon : Rp"<<hargad;







}