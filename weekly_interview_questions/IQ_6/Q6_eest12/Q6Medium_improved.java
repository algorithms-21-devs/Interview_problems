/*
  Q6 Medium
  Time complexity: O(kn), worst case O(n^2) when k=n/2
  Space complexity: O(1)

  Implements partial selection sort. Iterate through the entire array to find the largest element, and swap it with the element at position 0. Iterate again to find the 2nd largest element, and swap it with the element at position 1. Do this k times to find the kth largest element, which will end up at position k-1.
  
  In the cases where k > (n/2), it makes more sense to look for the (n-k+1)th smallest element instead, as this will reduce the number of iterations. For example, in an array with 10 elements, instead of looking for the 9th largest, we can look for the 2nd smallest, iterating only 2 times.

  Although the time complexity is the same, selection sort reduces the number of elements that are visited during each iteration, and the inversion from k to n-k+1 reduces the number of iterations to n/2 at most.
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

    if (k > arr.length/2) {
      return smallest(arr, arr.length-k+1);
    }

    // iterate through array k times to find kth largest
    for (int i = 0; i < k; i++) {
      int currLargestIndex = i; // index of largest unsorted element so far
      // iterate through unsorted part of array to find current largest
      for (int j = i; j < arr.length; j++) {
        if (arr[j] > arr[currLargestIndex]) {
          currLargestIndex = j;
        }
      }
      // swap largest and leftmost unsorted elements
      int temp = arr[i];
      arr[i] = arr[currLargestIndex];
      arr[currLargestIndex] = temp;
    }

    return arr[k-1];
  }

  public static int smallest(int[] arr, int k) {
    // iterate through array k times to find kth smallest
    for (int i = 0; i < k; i++) {
      int currSmallestIndex = i; // index of largest unsorted element so far
      // iterate through unsorted part of array to find current smallest
      for (int j = i; j < arr.length; j++) {
        if (arr[j] < arr[currSmallestIndex]) {
          currSmallestIndex = j;
        }
      }
      // swap smallest and leftmost unsorted elements
      int temp = arr[i];
      arr[i] = arr[currSmallestIndex];
      arr[currSmallestIndex] = temp;
    }

    return arr[k-1];
  }
}