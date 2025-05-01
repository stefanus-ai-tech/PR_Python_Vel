
import java.util.NoSuchElementException;

class SinglyNode<T> {
    T data;
    SinglyNode<T> next;

    SinglyNode(T data) {
        this.data = data;
        this.next = null;
    }

}

public class SinglyLinkedList<T> {
    private SinglyNode<T> head;
    private int size;

    public SinglyLinkedList(){
        this.head = null;
        this.size = 0;
    }

    public boolean isEmpty() {
        return head == null;
    }

    public int size(){
        return size;
    }   

    public void addFirst (T data){
        SinglyNode<T> newNode = new SinglyNode<>(data);
        newNode.next = head; // new node points to the old head
        head = newNode;      // head now points to the new node
        size++;
    }

    public void addLast (T data){
        SinglyNode<T> newNode = new SinglyNode<>(data);
        if (isEmpty()) {
            head = newNode; 
        } else {
            SinglyNode<T> current = head;
            while (current.next != null){ // transverse to the last node
                current = current.next;
            }
            current.next = newNode; // last node points to the new node
        }
        size++;
    }

    public T removeFirst(){
        if (isEmpty()){
            throw new NoSuchElementException("Listnya empty bos");
        }
        T data = head.data;
        head = head.next;
        size--;
        return data;
    }

    public T removeLast() {
        if (isEmpty()){
            throw new NoSuchElementException("Listnya empty bos");
        }
        T data;
        if (head.next == null){
            data = head.data;
            head = null;
        } else {
            SinglyNode<T> current = head;
            while (current.next.next != null){ // Stop at the second to last node 
                current = current.next;
            }
            data = current.next.data; // Get data from the last node
            current.next = null; //disconnect the last node
        }
        size--;
        return data;
    }

    public void display(){
        if (isEmpty()){
            System.out.println("Listnya empty bos");
            return;
        }
        System.out.print("Singly list: Head => ");
        SinglyNode<T> current = head;
        while (current != null){
            System.out.print(current.data + " => ");
            current = current.next;
        }
        System.out.println("Null");
    }
    
    public static void main(String[] args){
        SinglyLinkedList<Integer> sll = new SinglyLinkedList<>();
        sll.addLast(10);
        sll.addLast(20);
        sll.addFirst(5);
        sll.addLast(30);
        sll.display();

    System.out.println("Size: "+ sll.size());
    System.out.println("Removed first: "+ sll.removeFirst());
    sll.display();

    System.out.println("Removed last: "+ sll.removeLast());
    sll.display();
    System.out.println("Size: " + sll.size());
    }
}
