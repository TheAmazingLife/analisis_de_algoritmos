// g++ -std=c++20 -O0 -o uhr uhr_2.cpp ../src/brute_force/brute_force.cpp ../src/brute_force/brute_force_mejorado.cpp ../src/divide_and_conquer/divide_and_conquer.cpp ../src/divide_and_conquer/divide_and_conquer_mejorado.cpp
// ./uhr testings 64 8 512 2 
#include <cstdint>
#include <chrono>
#include <cmath>
#include <fstream>
#include <iostream>
#include <random>
#include <vector>

#include "utils.cpp"
#include "../src/brute_force/brute_force.hpp"
#include "../src/brute_force/brute_force_mejorado.hpp"
#include "../src/divide_and_conquer/divide_and_conquer.hpp"
#include "../src/divide_and_conquer/divide_and_conquer_mejorado.hpp"

int main(int argc, char *argv[])
{
    // Validate and sanitize input
    std::int64_t runs, lower, upper, step;
    validate_input(argc, argv, runs, lower, upper, step);

    // Clock and stats vars
    std::int64_t n, i, executed_runs;
    std::int64_t total_runs_additive = runs * (((upper - lower) / step) + 1);
    std::vector<double> times_bf(runs), times_dq(runs), q;
    double mean_time, time_stdev, dev;
    auto begin_time = std::chrono::high_resolution_clock::now();
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::nano> elapsed_time;

    // RNG
    std::random_device rd;
    std::mt19937_64 rng(rd());

    // Output files
    std::ofstream out_bf("brute_force_vs.csv");
    std::ofstream out_dq("brute_force_mejorado_vs.csv");
    out_bf << "n,t_mean,t_stdev,t_Q0,t_Q1,t_Q2,t_Q3,t_Q4" << std::endl;
    out_dq << "n,t_mean,t_stdev,t_Q0,t_Q1,t_Q2,t_Q3,t_Q4" << std::endl;

    std::cerr << "\033[0;36mRunning tests...\033[0m" << std::endl << std::endl;
    executed_runs = 0;

    for (n = lower; n <= upper; n *= step) {
        std::uniform_int_distribution<std::int64_t> u_distr(-100, 100);

        for (i = 0; i < runs; i++) {
            display_progress(++executed_runs, total_runs_additive * 2);  // x2 por ambos tests

            // Generar un solo set de puntos y duplicarlo
            std::vector<std::pair<double, double>> points(n);
            for (auto &point : points) {
                point = {u_distr(rng), u_distr(rng)};
            }

            // Test Brute Force
            begin_time = std::chrono::high_resolution_clock::now();
            double result_bf = minDist_BF(points);
            end_time = std::chrono::high_resolution_clock::now();
            elapsed_time = end_time - begin_time;
            times_bf[i] = elapsed_time.count();

            // Test Divide and Conquer (usar los mismos puntos)
            begin_time = std::chrono::high_resolution_clock::now();
            double result_dq = minDist_BF_mejorado(points);
            end_time = std::chrono::high_resolution_clock::now();
            elapsed_time = end_time - begin_time;
            times_dq[i] = elapsed_time.count();
        }

        // --- Estadísticas para Brute Force ---
        mean_time = std::accumulate(times_bf.begin(), times_bf.end(), 0.0) / runs;
        time_stdev = 0;
        for (auto t : times_bf) {
            dev = t - mean_time;
            time_stdev += dev * dev;
        }
        time_stdev = std::sqrt(time_stdev / (runs - 1));
        quartiles(times_bf, q);
        out_bf << n << "," << mean_time << "," << time_stdev << "," << q[0] << "," << q[1] << "," << q[2] << "," << q[3] << "," << q[4] << std::endl;

        // --- Estadísticas para Divide and Conquer ---
        mean_time = std::accumulate(times_dq.begin(), times_dq.end(), 0.0) / runs;
        time_stdev = 0;
        for (auto t : times_dq) {
            dev = t - mean_time;
            time_stdev += dev * dev;
        }
        time_stdev = std::sqrt(time_stdev / (runs - 1));
        quartiles(times_dq, q);
        out_dq << n << "," << mean_time << "," << time_stdev << "," << q[0] << "," << q[1] << "," << q[2] << "," << q[3] << "," << q[4] << std::endl;
    }

    std::cerr << std::endl << "\033[1;32mDone!\033[0m" << std::endl;
    out_bf.close();
    out_dq.close();

    return 0;
}
