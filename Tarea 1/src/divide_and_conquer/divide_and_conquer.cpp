#include "divide_and_conquer.hpp"
#include <algorithm>

// Ordenar puntos por coordenada x
bool compX(const std::pair<double, double> &p1, const std::pair<double, double> &p2) {
    return p1.first < p2.first;
}

// Ordenar puntos por coordenada y
bool compY(const std::pair<double, double> &p1, const std::pair<double, double> &p2) {
    return p1.second < p2.second;
}

double minDistCentro(std::vector<std::pair<double, double>> &centro, double d) {
    // Ensure centro is a std::vector for compatibility with std::sort
    // Ordenar los puntos por coordenada y
    std::sort(centro.begin(), centro.end(), compY);

    double minDist = d;

    for (size_t i = 0; i < centro.size(); i++) {
        for (size_t j = i + 1; j < centro.size() && (centro[j].second - centro[i].second) < minDist; j++) {
            double nuevaDist = calculateDistance(centro[i], centro[j]);
            minDist = std::min(minDist, nuevaDist);
        }
    }

    return minDist;
}

double minDist(std::vector<std::pair<double, double>> &dots, int left, int right) {
    // Caso base: si hay 2 o menos puntos, usamos fuerza bruta
    if (right - left <= 3) {
        double minDist = std::numeric_limits<double>::max();
        for (int i = left; i < right; i++) {
            for (int j = i + 1; j < right; j++) {
                double distance = calculateDistance(dots[i], dots[j]);
                minDist = std::min(minDist, distance);
            }
        }
        return minDist;
    }

    // Dividir el conjunto de puntos en dos mitades
    int mid = (left + right) / 2;

    // Calcular la distancia minima en las dos mitades
    double dIzq = minDist(dots, left, mid);
    double dDer = minDist(dots, mid, right);

    // Tomar la minima distancia entre las dos mitades
    double d = std::min(dIzq, dDer);

    // Crear un vector para almacenar los puntos dentro de la distancia d
    std::vector<std::pair<double, double>> centro;
    for (int i = left; i < right; i++) {
        if (abs(dots[i].first - dots[mid].first) < d) {
            centro.push_back(dots[i]);
        }
    }

    return std::min(d, minDistCentro(centro, d));
}

double minDist_DQ(std::vector<std::pair<double, double>> &dots) {
    // Ordenar los puntos por coordenada x
    std::sort(dots.begin(), dots.end(), compX);

    // Llamar a la funcion recursiva
    return minDist(dots, 0, dots.size());
}