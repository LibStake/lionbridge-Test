#include <iostream>
#include <string>
#include "./Checker.h"

int main() {

	Checker *ck = new Checker();
	std::string input = "";

	std::cout << "Parenthesis Checker -- Gipyo Choi" << std::endl;
	std::cout << "String input >> "; std::getline(std::cin, input);

	std::cout << "Input string is >> " << input << std::endl;
	std::cout << "Checking result :: ";
	if (ck->checkStringPrarenthesis(input)) std::cout << "True"; else std::cout << "False";
	std::cout << std::endl;

	delete ck;

	return 0;
}
