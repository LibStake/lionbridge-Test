#pragma once
#include <vector>

class FatigueCalculator {
    private:
    std::vector<int> *works;
    int remTime;

    public:
    FatigueCalculator();
    ~FatigueCalculator();

    long calculateFatigue(int time, std::vector<int> *workArray);	// Calculate minimum fatigue
    void swap(int idx1, int idx2);									// Swap two values in vector
    void pushToBack(int idx);										// Re-sort to descending order
};
