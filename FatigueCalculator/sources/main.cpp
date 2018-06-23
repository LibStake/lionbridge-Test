#include <iostream>
#include <vector>
#include "./FatigueCalculator.h"

int main() {
    std::cout << "Fatigue checker -- Gipyo Choi" << std::endl;

    std::vector<int> *works1 = new std::vector<int>({4, 3, 3}); int time1 = 4;
    std::vector<int> *works2 = new std::vector<int>({2,1,2}); int time2 = 1;
    std::vector<int> *works3 = new std::vector<int>({1,1}); int time3 = 3;

    FatigueCalculator *calc = new FatigueCalculator();

    std::cout << "Result Case [4,3,3]\t\t n=4\t\t:: " << calc->calculateFatigue(time1, works1) << std::endl;
    std::cout << "Result Case [2,1,2]\t\t n=1\t\t:: " << calc->calculateFatigue(time2, works2) << std::endl;
    std::cout << "Result Case [1,1]\t\t n=3\t\t:: " << calc->calculateFatigue(time3, works3) << std::endl;

    if (calc) delete calc;
    if (works1) delete works1;

    return 0;
}
