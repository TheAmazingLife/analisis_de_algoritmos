#ifndef DIVIDE_AND_CONQUER_MEJORADO_HPP
#define DIVIDE_AND_CONQUER_MEJORADO_HPP
#include <vector>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include "brute_force_mejorado.hpp"

bool compXDQ(const std::pair<int, int> &p1, const std::pair<int, int> &p2);
bool compYDQ(const std::pair<int, int> &p1, const std::pair<int, int> &p2);
double minDistDQ(std::vector<std::pair<int, int>> &dots, int left, int right);
double minDist_DQ_Mejorado(std::vector<std::pair<int, int>> &dots);
double minDistCentroDQ(std::vector<std::pair<int, int>> &centro, double d);

#endif

