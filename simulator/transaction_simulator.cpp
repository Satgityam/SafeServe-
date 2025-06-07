#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
using namespace std;

string generate_device() {
    int id = rand() % 5;
    return "device_" + to_string(id);
}

string generate_time() {
    int hour = rand() % 24;
    int minute = rand() % 60;
    return to_string(hour) + ":" + to_string(minute);
}

int main() {
    srand(time(0));
    ofstream file("../data/transactions.csv");
    file << "transaction_id,user_id,time,amount,device_id,location\n";
    
    for (int i = 1; i <= 100; ++i) {
        int amount = rand() % 10000;
        string device = generate_device();
        string time = generate_time();
        int user_id = rand() % 20;
        string location = (rand() % 2 == 0) ? "CityA" : "CityB";
        file << i << ",user_" << user_id << "," << time << "," << amount << "," << device << "," << location << "\n";
    }

    file.close();
    cout << "Transactions generated!\n";
    return 0;
}
