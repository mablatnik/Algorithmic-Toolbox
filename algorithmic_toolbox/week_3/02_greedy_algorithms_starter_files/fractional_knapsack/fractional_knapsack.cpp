#include <iostream>
#include <vector>

using std::vector;

// finding the maximum index i.e the index for which values/weights is maximum
int get_max_index(vector<int> weights, vector<int> values) {
    int max_i = 0;
    double max = 0;

    for (int i = 0; i < weights.size(); i++) {
        if (weights[i] != 0 && (double) values[i] / weights[i] > max) {
            max = (double) values[i] / weights[i];
            max_i = i;  //maximum index
        }
    }
    return max_i;
}

// filling the knapsack staring from the maximum index
double get_optimal_value(int capacity, vector<int> weights, vector<int> values) {
    double value = 0.0;

    for (int i = 0; i < weights.size(); i++) {
        if (capacity == 0) return value; // capacity of the knapsack
        int index = get_max_index(weights, values);
        int a = std::min(capacity, weights[index]); 
        value += a * (double) values[index] / weights[index]; // total value of item placed in knapsack
        weights[index] -= a;
        capacity -= a;
    }

    return value;
}

int main() {
    int n;
    int capacity;
    std::cin >> n >> capacity;
    vector<int> values(n);
    vector<int> weights(n);
    for (int i = 0; i < n; i++) {
        std::cin >> values[i] >> weights[i];
    }

    double optimal_value = get_optimal_value(capacity, weights, values);

    std::cout.precision(10); //print the answer upto five decimal for error  corrections
    std::cout << optimal_value << std::endl;
    return 0;
}
