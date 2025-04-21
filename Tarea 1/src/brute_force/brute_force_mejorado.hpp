#ifndef BRUTE_FORCE_MEJORADO_HPP
#define BRUTE_FORCE_MEJORADO_HPP

#include <vector>
#include <utility>
#include <cmath>
#include <limits>

double calculateSquareDistance(std::pair<double, double> p1, std::pair<double, double> p2);
double minDist_BF_mejorado(std::vector<std::pair<double, double>> &dots);

#endif