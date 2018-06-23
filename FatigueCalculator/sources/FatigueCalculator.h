#pragma once
#include <vector>

class FatigueCalculator {
    private:
    std::vector<int> *works;
    int remTime;

    public:
    FatigueCalculator();
    ~FatigueCalculator();

    long calculateFatigue(int time, std::vector<int> *workArray);
    void swap(int idx1, int idx2);
    void pushToBack(int idx);
};
