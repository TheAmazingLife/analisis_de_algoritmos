#include "brute_force_mejorado.hpp"


// Funcion que calcula la distancia euclidea entre 2 puntos
double calculateSquareDistance (std::pair<double, double> p1, std::pair<double, double> p2) {
    return (pow(p1.first - p2.first, 2) + pow(p1.second - p2.second, 2));
}

// Distancia minima entre 2 puntos usando fuerza bruta
// Esta funcion recibe un vector de puntos y devuelve la distancia minima entre 2 puntos
// La distancia minima se calcula usando la formula de distancia euclidea
// La complejidad de esta funcion es O(n^2) ya que se compara cada punto con todos los puntos


double minDist_BF_mejorado(std::vector<std::pair<double, double>> &dots) {
    // Declaracion de variable que almacena minima distancia
    double minSquareDistance = std::numeric_limits<double>::max();
    size_t dotSize = dots.size();

    // Calcularemos la distancia minima entre 2 puntos y almacenamos la minima distancia
    for (size_t i = 0; i < dotSize; i++)
    {
        for (size_t j = i+1; j < dotSize; j++)
        {
            double squaredistance = calculateSquareDistance(dots[i], dots[j]);
            if (minSquareDistance == 0 || squaredistance <= minSquareDistance)
            {
                minSquareDistance = squaredistance;
                if (minSquareDistance == 0) return 0.0;
            }
        }
    }
    return (sqrt(minSquareDistance));
}
