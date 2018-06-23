#pragma once
#include <stack>
#include <string>

#define MAXSTRINGLENGTH 100000

class Checker {
private:
	std::stack<char> stack;  // parsing container
public:
	// Constructor
	Checker();

	// Functions
	bool checkStringPrarenthesis(std::string input);
};
