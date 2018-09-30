import java.util.Scanner;
import java.util.Random;

class SelectionSort {

  private static int[] selectionSort(int[] items) {
    for (int i = 0; i < items.length; i++) {
      int minIndex = i;
      for (int j = i; j < items.length; j++) {
        if (items[j] < items[minIndex]) {
          minIndex = j;
        }
      }
      int swap = items[minIndex];
      items[minIndex] = items[i];
      items[i] = swap;
    }
    return items;
  }

  public static final void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int n = scan.nextInt();
    int[] items = new int[n];
    for (int i = 0; i < n; i++) {
      items[i] = scan.nextInt();
    }
    scan.close();

    selectionSort(items);

    for (int i = 0; i < items.length; i++) {
      System.out.print(items[i]);
      if (i != items.length - 1) {
        System.out.print(" ");
      } else {
        System.out.println("");
      }
    }
  }

}

