import java.util.*;

public class Main {

    public static List<Integer> quicksort(List<Integer> arr) {
        if (arr.size() < 2) {
            return arr;
        }

        int pivot = arr.get(0);

        List<Integer> less = new ArrayList<>();
        List<Integer> greater = new ArrayList<>();

        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) <= pivot) {
                less.add(arr.get(i));
            } else {
                greater.add(arr.get(i));
            }
        }

        List<Integer> result = new ArrayList<>();

        result.addAll(quicksort(less));
        result.add(pivot);
        result.addAll(quicksort(greater));

        return result;
    }

    public static void main(String[] args) {
        List<Integer> arr = Arrays.asList(1, 4, 6, 8, 2, 5, 0);

        List<Integer> sorted = quicksort(arr);

        System.out.println(sorted);
    }
}