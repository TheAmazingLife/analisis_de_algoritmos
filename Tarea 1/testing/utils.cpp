/** Author: LELE */

#ifndef UTILS
#define UTILS

#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

inline void validate_input(int argc, char *argv[], std::int64_t& runs,
    std::int64_t& lower, std::int64_t& upper, std::int64_t& step)
{
    if (argc != 6) {
        std::cerr << "Usage: <filename> <RUNS> <LOWER> <UPPER> <STEP>" << std::endl;
        std::cerr << "<filename> is the name of the file where performance data will be written." << std::endl;
        std::cerr << "It is recommended for <filename> to have .csv extension and it should not previously exist." << std::endl;
        std::cerr << "<RUNS>: numbers of runs per test case: should be >= 32." << std::endl;
        std::cerr << "<LOWER> <UPPER> <STEP>: range of test cases." << std::endl;
        std::cerr << "These should all be positive." << std::endl;
        std::exit(EXIT_FAILURE);
    }

    // Read command line arguments
    try {
        runs = std::stoll(argv[2]);
        lower = std::stoll(argv[3]);
        upper = std::stoll(argv[4]);
        step = std::stoll(argv[5]);
    } catch (std::invalid_argument const& ex) {
        std::cerr << "std::invalid_argument::what(): " << ex.what() << std::endl;
        std::exit(EXIT_FAILURE);
    } catch (std::out_of_range const& ex) {
        std::cerr << "std::out_of_range::what(): " << ex.what() << std::endl;
        std::exit(EXIT_FAILURE);
    }

    // Validate arguments
    if (runs < 4) {
        std::cerr << "<RUNS> must be at least 4." << std::endl;
        std::exit(EXIT_FAILURE);
    }
    if (step <= 0 or lower <= 0 or upper <= 0) {
        std::cerr << "<STEP>, <LOWER> and <UPPER> have to be positive." << std::endl;
        std::exit(EXIT_FAILURE);
    }
    if (lower > upper) {
        std::cerr << "<LOWER> must be at most equal to <UPPER>." << std::endl;
        std::exit(EXIT_FAILURE);
    }
}

inline void display_progress(std::int64_t u, std::int64_t v)
{
    const double progress = u / double(v);
    const std::int64_t width = 70;
    const std::int64_t p = width * progress;
    std::int64_t i;

    std::cerr << "\033[1m[";
    for (i = 0; i < width; i++) {
        if (i < p)
            std::cerr << "=";
        else if (i == p)
            std::cerr << ">";
        else
            std::cerr << " ";
    }
    std::cerr << "] " << std::int64_t(progress * 100.0) << "%\r\033[0m";
    std::cerr.flush();
}

inline void quartiles(std::vector<double>& data, std::vector<double>& q)
{
    q.resize(5);
    std::size_t n = data.size();
    std::size_t p;

    std::sort(data.begin(), data.end());

    if (n < 4) {
        std::cerr << "quartiles needs at least 4 data points." << std::endl;
        std::exit(EXIT_FAILURE);
    }

    // Get min and max
    q[0] = data.front();
    q[4] = data.back();

    // Find median
    if (n % 2 == 1) {
        q[2] = data[n / 2];
    } else {
        p = n / 2;
        q[2] = (data[p - 1] + data[p]) / 2.0;
    }

    // Find lower and upper quartiles
    if (n % 4 >= 2) {
        q[1] = data[n / 4];
        q[3] = data[(3 * n) / 4];
    } else {
        p = n / 4;
        q[1] = 0.25 * data[p - 1] + 0.75 * data[p];
        p = (3 * n) / 4;
        q[3] = 0.75 * data[p - 1] + 0.25 * data[p];
    }
}

#endif
