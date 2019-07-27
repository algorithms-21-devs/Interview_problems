/*
  Q6 Medium
  Time complexity: O(kn), worst case O(n^2) when k=n
  Space complexity: O(1)

  Iterate through the entire array to find the largest element (stored in 'ithLargest'). Replace the element in the array with a very small value as a way to eliminate it. Repeat to find the 2nd largest element. Do this k times to find the kth largest element. Since the array will be iterated k times, time complexity is O(kn).
*/

class Main {
  public static void main(String[] args) {
    // test cases

    System.out.println(largest(new int[]{9,9,2}, 2)); // 9

    System.out.println(largest(new int[]{-3,83,0,30,90,70},3)); // 70

    System.out.println(largest(new int[]{0},1)); // 0

    System.out.println(largest(new int[]{18,18,18,18,18,18}, 4)); // 18

    try {
      System.out.println(largest(new int[]{17,15,18},8)); // exception
    } catch(Exception e) {
      System.out.println(e);
    }

    System.out.println(largest(new int[]{})); // null

    try {
      System.out.println(largest(null)); // exception
    } catch(Exception e) {
      System.out.println(e);
    }
  }

  // overloading with k=1 to match test cases
  public static Integer largest(int[] arr) {
    return largest(arr, 1);
  }

  public static Integer largest(int[] arr, int k) throws NullPointerException, IllegalArgumentException {
    // exceptions
    if (arr == null) {
      throw new NullPointerException("Array is null");
    }
    if (arr.length == 0) {
      return null;
    }
    if (k <= 0 || k > arr.length) {
      throw new IllegalArgumentException("k must be between 1 and arr.length");
    }

    final int MIN = -10000; // minimum possible element in array is -9999
    int ithLargest = 0; // largest element after each iteration
    int currLargestIndex = 0; // index of largest element so far during each iteration

    // iterate through array k times to find kth largest
    for (int i = 0; i < k; i++) {
      // iterate through array to find current largest
      for (int j = 0; j < arr.length; j++) {
        if (arr[j] > arr[currLargestIndex]) {
          currLargestIndex = j;
        }
      }
      ithLargest = arr[currLargestIndex];
      arr[currLargestIndex] = MIN; // set to MIN to ignore during future iterations
    }

    return ithLargest;
  }
}