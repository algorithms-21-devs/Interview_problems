/*
    Q3 Hard
    Time complexity: O(n^2)
    Space complexity: O(1)
    
    Set 'start' and 'end' pointers to keep track of the leftmost and rightmost nodes to be compared. Initially, 'start' is the head of the list, and 'end' is null. A 'curr' node iterates between 'start' and 'end' to find the node that comes before 'end'. Then 'start' moves one node to the right, and 'end' moves one node to the left. Because 'curr' has to iterate between 'start' and 'end' continously until the two nodes meet or until the two nodes have unequal values, the time complexity is O(n^2).
*/

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
        
        Node start = head;
        Node end = null;
        Node curr = head;
        
        // move 'start' to the right and 'end' to the left
        // until they meet in the middle;
        // condition works for even-sized strings
        while (start != end) {
            // iterate through list until curr reaches end node
            while (curr != null && curr.next != end) {
                curr = curr.next;
            }
            
            // move end pointer to the left
            end = curr;
            
            // check if start and end have reached the middle;
            // condition works for odd-sized strings
            if (start == end) {
                return true;
            }
            
            // compare left node to right node
            if (Character.toUpperCase(start.val) != Character.toUpperCase(end.val)) {
                return false;
            }
            
            // move start pointer to the right and reset curr
            start = start.next;
            curr = start;
        }
        
        return true;
    }
}
