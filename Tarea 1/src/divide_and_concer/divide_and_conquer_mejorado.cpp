#include "divide_and_conquer_mejorado.hpp"

// Ordenar puntos por coordenada x
bool compXDQ(const std::pair<int, int> &p1, const std::pair<int, int> &p2) {
    return p1.first < p2.first;
}

// Ordenar puntos por coordenada y
bool compYDQ(const std::pair<int, int> &p1, const std::pair<int, int> &p2) {
    return p1.second < p2.second;
}

double minDistCentroDQ(std::vector<std::pair<int, int>> &centro, double d) {
    // Ordenar los puntos por coordenada y
    std::sort(centro.begin(), centro.end(), compYDQ);

    double minSqrtDist = d * d; // Almacenamos la distancia minima al cuadrado
    double centroSize = centro.size();
    for (size_t i = 0; i < centroSize; i++) {
        for (size_t j = i + 1; j < centroSize && (centro[j].second - centro[i].second) < d; j++) {

            double nuevaDist = calculateSquareDistance(centro[i], centro[j]);
            //minSqrtDist = std::min(minSqrtDist, nuevaDist);

            if (nuevaDist < minSqrtDist) {
                minSqrtDist = nuevaDist;
                d = sqrt(minSqrtDist);  // Actualiza d 
            }
        }
    }

    return sqrt(minSqrtDist);
}

double minDistDQ(std::vector<std::pair<int, int>> &dots, int left, int right) {
    // Caso base: si hay 2 o menos puntos, usamos fuerza bruta
    if (right - left <= 3) {
        double minSqrtDist = std::numeric_limits<double>::max();
        for (int i = left; i < right; i++) {
            for (int j = i + 1; j < right; j++) {
                double distance = calculateSquareDistance(dots[i], dots[j]);
                minSqrtDist = std::min(minSqrtDist, distance);
            }
        }
        return sqrt(minSqrtDist);
    }

    // Dividir el conjunto de puntos en dos mitades
    int mid = (left + right) / 2;

    // Calcular la distancia minima en las dos mitades
    double dIzq = minDistDQ(dots, left, mid);
    double dDer = minDistDQ(dots, mid, right);

    // Tomar la minima distancia entre las dos mitades
    double d = std::min(dIzq, dDer);

    // Crear un vector para almacenar los puntos dentro de la distancia d
    std::vector<std::pair<int, int>> centro;
    for (int i = left; i < right; i++) {
        if (abs(dots[i].first - dots[mid].first) < d) {
            centro.push_back(dots[i]);
        }
    }

    return std::min(d, minDistCentroDQ(centro, d));
}

double minDist_DQ_Mejorado(std::vector<std::pair<int, int>> &dots) {
    // Ordenar los puntos por coordenada x
    std::sort(dots.begin(), dots.end(), compXDQ);

    // Llamar a la funcion recursiva
    return minDistDQ(dots, 0, dots.size());
}