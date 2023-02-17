#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>
 
int main()
{
    int n;
    std::cin >> n;
    std::vector<int> v(n);
 
    for (int i = 0; i < n; i++)
        std::cin >> v[i];
 
    std::sort(v.begin(), v.end());
    v.erase(std::unique(v.begin(), v.end()), v.end());
 
    int k;
    std::cin >> k;
    for (int i = 0; i < k; i++) {
        int itmp;
        std::cin >> itmp;
        std::cout << std::distance(v.begin(), std::lower_bound(v.begin(), v.end(), itmp)) << std::endl;
    }
}