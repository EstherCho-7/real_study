#include <iostream>
#include <cmath>

double Integral(double a, double b, int n);

double function(double x) {
	return sin(x);
}

int main() {
	double a, b;
	int n;

	std::cout << "Enter the lower limit (a): ";
	std::cin >> a;
	std::cout << "Enter the upper limit (b): ";
	std::cin >> b;
	std::cout << "Enter the number of subdivisions (n): ";
	std::cin >> n;

	double result=Integral(a, b, n);
	std::cout << "The interal result is: " << result << std::endl;

	return 0;
}

double Integral(double a, double b, int n) {
	double h=(b-a)/n;
	double sum=0.0;

	for(int i=1; i<n; ++i) {
		sum += function(a+i*h);
	}
	
	sum += (function(a)+function(b)) / 2.0;
	return sum*h;
}
