#include <iostream>
#include <algorithm>
#include <vector>
#include "./FatigueCalculator.h"

FatigueCalculator::FatigueCalculator() {
    works = nullptr;
    remTime = 0;
}

FatigueCalculator::~FatigueCalculator() {
}

long FatigueCalculator::calculateFatigue(int time, std::vector<int> *workArray) {
	// Check constraints (should be size of array <= 20000 , value of N <= 1000000)
	if (workArray->size() > 20000 || time > 1000000) return -1;

	// Fill internal values.
    works = workArray;
    remTime = time;

    // Sort to Descending order
    std::sort(works->begin(), works->end());
    std::reverse(works->begin(), works->end());

    // Check working time constraint
    if (works->at(0) > 50000) return -1;

	// Minimize maximum value
	int firstElem = 0;
	while (remTime != 0 && firstElem < (int)(works->size())) {
		works->at(firstElem)--;
		remTime--;
		if (works->at(firstElem) == 0) firstElem++;
		else pushToBack(firstElem);
	}

	// Sum result
	long result = 0;
	for (int i = firstElem; i < (int)(works->size()); i++) {
		result += (long)(works->at(i)*works->at(i));
	}

	return result;
}

void FatigueCalculator::pushToBack(int idx) {
	while (idx+1 < (int)(works->size()) && works->at(idx) < works->at(idx+1)) {
		swap(idx, idx+1);
		idx++;
	}
}

void FatigueCalculator::swap(int idx1, int idx2) {
    int temp = works->at(idx1);
    works->at(idx1) = works->at(idx2);
    works->at(idx2) = temp;
}
