#include <iostream>
#include <vector>
using namespace std;

int findSmallest(vector<int>& arr) {
    int smallest = arr[0];
    int smallest_index = 0;

    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] < smallest) {
            smallest = arr[i];
            smallest_index = i;
        }
    }

    return smallest_index;
}

vector<int> selectionSort(vector<int> arr) {
    vector<int> newArr;

    while (!arr.empty()) {
        int smallest_index = findSmallest(arr);

        newArr.push_back(arr[smallest_index]);
        arr.erase(arr.begin() + smallest_index);
    }

    return newArr;
}

int main() {
    vector<int> arr = {5, 3, 6, 2, 10};

    vector<int> sorted = selectionSort(arr);

    for (int num : sorted) {
        cout << num << " ";
    }

    return 0;
}