
#include <iostream>
#include <set>
#include <string>
#include <algorithm>

std::string restoreGenome(const std::vector<std::string>& fragments) {
    std::set<char> uniqueLetters;


    for (const std::string& fragment : fragments) {
        for (char letter : fragment) {
            uniqueLetters.insert(letter);
        }
    }

    std::string genome;
    for (char letter : uniqueLetters) {
        genome += letter;
    }
    std::sort(genome.begin(), genome.end());

    return genome;
}

int main() {
    int n;
    std::cin >> n;

    std::vector<std::string> fragments(n);
    for (int i = 0; i < n; i++) {
        std::cin >> fragments[i];
    }

    std::string genome = restoreGenome(fragments);
    std::cout << genome << std::endl;

    return 0;
}
