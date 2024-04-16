#include <iostream>
#include <cmath>

int main() {
    int n, x[100], i;
    char again;

    do {
        std::cout << "Input banyak data n = ";
        std::cin >> n;

        for(i = 0; i < n; i++) {
            std::cout << "Input nilai x ke-" << i+1 << " = ";
            std::cin >> x[i];
        }

        std::cout << "No\tX\tf(x)\tg(x)\th(x)\n";
        for(i = 0; i < n; i++) {
            if(x[i] > 0) {
                std::cout << i+1 << "\t" << x[i] << "\t" << 3*x[i]*x[i]+7*x[i] << "\t" << 2*x[i]*x[i]-5*x[i] << "\t" << (3*x[i]*x[i]+7*x[i]) * (2*x[i]*x[i]-5*x[i]) << "\n";
            } else {
                std::cout << i+1 << "\t" << x[i] << "\t" << 4 << "\t" << pow((3*x[i]*x[i]+7*x[i]), 2) - sqrt(3*x[i]*x[i]+7*x[i]) << "\t" << 4 * (pow((3*x[i]*x[i]+7*x[i]), 2) - sqrt(3*x[i]*x[i]+7*x[i])) << "\n";
            }
        }

        std::cout << "Input nilai x lagi? Y/N ";
        std::cin >> again;

    } while(again == 'Y' || again == 'y');

    return 0;
}