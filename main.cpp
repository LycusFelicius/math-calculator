#include <iostream>
#include <stdio.h>
#include <Windows.h>
#include <unistd.h>
#include <string>
#include <stdlib.h>
#include <sstream>
#include <iterator>
#include <algorithm>
#include <math.h>
using namespace std;
//pythagoras func
int s_func (int a, int b, int c) {
    int result;
    if (a == 0) {
        a = pow(c, 2) - pow(b, 2);
        result = sqrt(a);
    } else if (b == 0) {
        b = pow(c, 2) - pow(a, 2);
        result = sqrt(b);
    } else if (c == 0) {
        c = pow(a, 2) + pow(b, 2);
        result = sqrt(c);
    }
    return result;
}
//main CLI interface func
int main () {
    int a = 0;
    int b = 0;
    int c = 0;
    int end;
    cout << "Fill unknown value with 0!" << endl;
    cout << "Enter value a : ";
    cin >> a;
    cout << "Enter value b : ";
    cin >> b;
    cout << "Enter value c : ";
    cin >> c;
    end = s_func (a, b, c);
    cout << "Hasilnya : " << end << endl;
    system("PAUSE");
}