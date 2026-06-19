import java.util.*;

public class Main {

    public static int findSmallest(ArrayList<Integer> arr) {
        int smallest = arr.get(0);
        int smallestIndex = 0;

        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) < smallest) {
                smallest = arr.get(i);
                smallestIndex = i;
            }
        }

        return smallestIndex;
    }

    public static ArrayList<Integer> selectionSort(ArrayList<Integer> arr) {
        ArrayList<Integer> newArr = new ArrayList<>();

        while (!arr.isEmpty()) {
            int smallestIndex = findSmallest(arr);

            newArr.add(arr.get(smallestIndex));
            arr.remove(smallestIndex);
        }

        return newArr;
    }

    public static void main(String[] args) {
        ArrayList<Integer> arr =
                new ArrayList<>(Arrays.asList(5, 3, 6, 2, 10));

        System.out.println(selectionSort(arr));
    }
}