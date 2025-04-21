#ifndef BRUTE_FORCE_HPP
#define BRUTE_FORCE_HPP

#include <vector>
#include <utility>
#include <cmath>
#include <limits>

double calculateDistance(std::pair<double, double> p1, std::pair<double, double> p2);
double minDist_BF(std::vector<std::pair<double, double>> &dots);

#endif