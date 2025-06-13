#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <ctime>
#include <cstdlib>

// Utility function to generate random elements
template<typename T>
T random_choice(const std::vector<T>& vec) {
    return vec[rand() % vec.size()];
}

// Generate random timestamp in string format
std::string generate_timestamp() {
    time_t rawtime = time(nullptr);
    struct tm * timeinfo = localtime(&rawtime);
    char buffer[25];
    strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", timeinfo);
    return std::string(buffer);
}

int main() {
    srand(time(0)); // Seed for randomness

    std::ofstream file("../data/transactions.csv");
    if (!file.is_open()) {
        std::cerr << "Failed to open output file.\n";
        return 1;
    }

    // Write CSV headers
    file << "transaction_id,user_id,amount,timestamp,device_id,location,payment_method,is_fraud\n";

    // Dummy data pools
    std::vector<std::string> users = {"U001", "U002", "U003", "U004"};
    std::vector<std::string> devices = {"D100", "D101", "D102"};
    std::vector<std::string> locations = {"Delhi", "Mumbai", "Bangalore", "Kolkata"};
    std::vector<std::string> methods = {"UPI", "Credit Card", "Wallet"};

    int num_transactions = 100;

    for (int i = 1; i <= num_transactions; ++i) {
        std::string user = random_choice(users);
        float amount = (rand() % 5000) + 100;  // Rs.100 - Rs.5099
        std::string timestamp = generate_timestamp();
        std::string device = random_choice(devices);
        std::string location = random_choice(locations);
        std::string method = random_choice(methods);

        // Simple rule-based fraud: high amount or odd hour (simulated randomly)
        bool high_value = amount > 4000;
        bool odd_hour = rand() % 10 == 0; // 10% chance
        bool changed_device = rand() % 15 == 0; // 6.6% chance

        bool is_fraud = high_value || odd_hour || changed_device;

        file << "T" << i << "," << user << "," << amount << "," << timestamp << ","
             << device << "," << location << "," << method << "," << is_fraud << "\n";
    }

    file.close();
    std::cout << "transactions.csv generated with " << num_transactions << " entries.\n";
    return 0;
}
