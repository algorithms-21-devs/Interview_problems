/*
    Q3 Medium
    Time complexity: O(n)
    Space complexity: O(n)
    
    Copy linked list to an array list. Iterate through the array list from the left and from the right until the middle is reached. Return false if at any point the left value doesn't match the right.
*/

import java.util.ArrayList;

public class Palindrome {
    
    static class Node {
        char val;
        Node next;
        public Node(){}
        public Node(char val, Node next) {
            this.val = val;
            this.next = next;
        }
    }

    public static void main(String []args) {
        Node l1 = new Node('a', new Node('n', new Node('a', null)));
        Node l2 = new Node('A', new Node('n', new Node('a', null)));
        Node l3 = new Node('p', new Node('e', new Node('e', new Node('p', null))));
        Node l4 = new Node('r', new Node('o', new Node('t', new Node('a', new Node('t', new Node('o', new Node('r', null)))))));
        Node l5 = new Node('z', null);
        Node l6 = new Node('h', new Node('e', new Node('l', new Node('l', new Node('o', null)))));
        Node l7 = new Node('j', new Node('a', new Node('m', new Node('e', new Node('s', null)))));
        Node l8 = new Node();
        Node l9 = null;
        
        System.out.println(isPalindrome(l1)); // true
        System.out.println(isPalindrome(l2)); // true
        System.out.println(isPalindrome(l3)); // true
        System.out.println(isPalindrome(l4)); // true
        System.out.println(isPalindrome(l5)); // true
        System.out.println(isPalindrome(l6)); // false
        System.out.println(isPalindrome(l7)); // false
        System.out.println(isPalindrome(l8)); // exception
        System.out.println(isPalindrome(l9)); // exception
    }
     
    private static boolean isPalindrome(Node head) throws NullPointerException, IllegalArgumentException {
        
        // exceptions
        if (head == null) {
            throw new NullPointerException("Function argument is null");
        }
        if (head.val == '\u0000' && head.next == null) {
            throw new IllegalArgumentException("List is empty");
        }
        
        ArrayList<Character> arr = new ArrayList<>();
        Node curr = head;
        
        // copy list node values to array list
        while (curr != null) {
            arr.add(Character.toUpperCase(curr.val));
            curr = curr.next;
        }
        
        // iterate through array list from both sides
        // until the middle is reached
        int right = arr.size() - 1;
        for (int left = 0; left <= right; left++) {
            // compare left and right
            if (arr.get(left) != arr.get(right)) {
                return false;
            }
            right--;
        }
        
        return true;
    }
}
