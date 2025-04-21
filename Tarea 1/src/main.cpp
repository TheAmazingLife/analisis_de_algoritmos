#include <iostream>
#include <random>
#include "brute_force/brute_force.hpp"
#include "brute_force/brute_force_mejorado.hpp"
#include "divide_and_conquer/divide_and_conquer.hpp"
#include "divide_and_conquer/divide_and_conquer_mejorado.hpp"

// para compilar:
// g++ main.cpp brute_force.cpp brute_force_mejorado.cpp divide_and_conquer.cpp divide_and_conquer_mejorado.cpp -o main -std=c++20
// para ejecutar
// ./main

int main() {
    // Vector que almacena los puntos
    std::random_device rd;
    std::mt19937_64 rng(rd());
    std::uniform_int_distribution<std::int64_t> u_distr(-100, 100); // Cambiar rango si es necesario
    int n;
    std::cout << "Ingrese el número de puntos: ";
    std::cin >> n;

    std::vector<std::pair<double, double>> points(n);
    for (auto &point : points) {
        point = {u_distr(rng), u_distr(rng)};
    }

    std::cout << "Puntos generados:\n";
    for (const auto &p : points) {
        std::cout << "(" << p.first << ", " << p.second << ")\n";
    }

    // Pruebas de los algoritmos
    double minDistance_BF = minDist_BF(points);
    double minDistance_BF_Mejorado = minSquareDist_BF(points);
    double minDistance_DQ = minDist_DQ(points);
    double minDistance_DQ_Mejorado = minDist_DQ_Mejorado(points);

    // Resultados
    std::cout << "\nResultados:\n";
    std::cout << "Distancia mínima (Fuerza Bruta): " << minDistance_BF << std::endl;
    std::cout << "Distancia mínima (Fuerza Bruta Mejorado): " << minDistance_BF_Mejorado << std::endl;
    std::cout << "Distancia mínima (Divide y Conquista): " << minDistance_DQ << std::endl;
    std::cout << "Distancia mínima (Divide y Conquista Mejorado): " << minDistance_DQ_Mejorado << std::endl;

    return 0;
}