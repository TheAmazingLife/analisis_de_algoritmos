#include <iostream>
#include <random>
#include "brute_force.hpp"
#include "divide_and_conquer.hpp"

// para compilar:
// g++ main.cpp brute_force.cpp divide_and_conquer.cpp -o main -std=c++20
// para ejecutar
// ./main

int main()
{

    // Vector que almacena los puntos

    std::random_device rd;
    std::mt19937_64 rng(rd());
    std::uniform_int_distribution<std::int64_t> u_distr(-100,100); // change depending on app
    int n; std::cin >> n;
    std::vector<std::pair<double, double>> points(n);
    for (auto &point : points)
    {
        point = {u_distr(rng), u_distr(rng)};
    }

    for (auto &&i : points)
    {
        std::cout << "Punto generado: (" << i.first << ", " << i.second << ")" << std::endl;
    }
        
    double minDistance_BF = minDist_BF(points);
    double minDistance_DQ = minDist_DQ(points);

    std::cout << "Distancia minima (Brute Force): " << minDistance_BF << std::endl;
    std::cout << "Distancia minima (Divide and Conquer): " << minDistance_DQ << std::endl;

    return 0;
}