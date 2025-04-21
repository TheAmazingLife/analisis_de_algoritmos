#include "brute_force.hpp"

// Funcion que calcula la distancia euclidea entre 2 puntos
double calculateDistance (std::pair<double, double> p1, std::pair<double, double> p2) {
    return sqrt(pow(p1.first - p2.first, 2) + pow(p1.second - p2.second, 2));
}

// Distancia minima entre 2 puntos usando fuerza bruta
// Esta funcion recibe un vector de puntos y devuelve la distancia minima entre 2 puntos
// La distancia minima se calcula usando la formula de distancia euclidea
// La complejidad de esta funcion es O(n^2) ya que se compara cada punto con todos los puntos
double minDist_BF(std::vector<std::pair<double, double>> &dots) {
    // Declaracion de variable que almacena minima distancia
    double minDistance = std::numeric_limits<double>::max();

    // Calcularemos la distancia minima entre 2 puntos y almacenamos la minima distancia
    for (size_t i = 0; i < dots.size(); i++)
    {
        for (size_t j = i+1; j < dots.size(); j++)
        {
            double distance = calculateDistance(dots[i], dots[j]);
            if (minDistance == 0 || distance <= minDistance)
            {
                minDistance = distance;
            }
        }
    }
    return minDistance;
}