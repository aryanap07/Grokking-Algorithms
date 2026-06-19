#include <iostream>
#include <vector>
using namespace std;

vector<int> quicksort(vector<int> arr) {
    if (arr.size() < 2) {
        return arr;
    }

    int pivot = arr[0];
    vector<int> less, greater;

    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] <= pivot)
            less.push_back(arr[i]);
        else
            greater.push_back(arr[i]);
    }

    vector<int> result = quicksort(less);
    result.push_back(pivot);

    vector<int> right = quicksort(greater);
    result.insert(result.end(), right.begin(), right.end());

    return result;
}

int main() {
    vector<int> arr = {1, 4, 6, 8, 2, 5, 0};

    vector<int> sorted = quicksort(arr);

    for (int num : sorted) {
        cout << num << " ";
    }

    return 0;
}