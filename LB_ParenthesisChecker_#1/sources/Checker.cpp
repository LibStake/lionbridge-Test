#include <iostream>
#include <algorithm>
#include <stack>
#include <string>
#include "./Checker.h"

Checker::Checker() {
	// Do nothing.
}

bool Checker::checkStringPrarenthesis(std::string input) {

	// Check if it is empty or beyond the restriction.
	if (input.length() > MAXSTRINGLENGTH || input.empty()) return false;

	// Check using stack
	for (std::string::iterator it = input.begin(); it != input.end(); ++it) {
		switch (*it) {
		case '(' :
			stack.push(*it);
			break;
		case ')' :
			if (stack.top() == '(') stack.pop();
			else stack.push(*it);
			break;
		default :
			// Not '(' or ')'
			//return false;
			continue;
		}
	}

	// Check stack for evaluation.
	if (stack.empty()) return true;
	else return false;
}
