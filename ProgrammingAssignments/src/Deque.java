import java.util.Iterator;


public class Deque <Item> implements Iterable<Item>{
	private Node first;
	private Node last;
	private Integer Qcount;
	private class Node {
		Item item;
		Node next;
	}
	public Deque(){
		  first = null;
		  last = null;
		  Qcount=0;
	}
	public boolean isEmpty(){
		return first == null;
	}
	public int size(){
		return Qcount;
	}
	public void addFirstItem(Item item){
		Node newNode= first;
		first = new Node();
		first.item=item;
		first.next= newNode;
		Qcount++;
	}
	public void addLastItem(Item item){
		Node temp = first;
		Node newNode = new Node();
		while (temp.next!= null){
			temp = temp.next;
		}
		last = temp;
		newNode.item= item;
		newNode.next=null;
		last.next= newNode;
		Qcount++;
	}
	public Item removeFirst(){
		if (first ==null){
		return null;
		}
		else {
			first = first.next;
			--Qcount;
			return first.item;
		}
	}
	public Item removeLast(){
		Node current = first;
		Node Next = first.next;
		if (first == null){
			return null;
		}
		while (Next.next!=null){
			current= Next;
			Next= Next.next;
		}
		current.next=null;
		Qcount --;
		return Next.item;
		
	}
	
	
    @Override
	public Iterator<Item> iterator() {
		// TODO Auto-generated method stub
		return new ListIterator();
	}
    private class ListIterator implements Iterator<Item>{
    	private Node current = first;
    	public boolean hasNext(){
    		return current !=null;
    	}
    	public Item next(){
    		Item item=current.item;
    		current = current.next;
    		return item;
    	}
		@Override
		public void remove() {
			// TODO Auto-generated method stub
			
		}
    }
	public static void main(String[] args){
		Deque <Integer> temp_queue = new Deque<Integer>();
		for (int i=0; i<10;i++){
			temp_queue.addFirstItem(i);
		}
		for (int i=5;i>0;i--){
			if (temp_queue.isEmpty()==false){
				temp_queue.removeLast();
				temp_queue.addLastItem(i+10);
			}
		}
		System.out.println(" size of queue is \n");
		System.out.println(temp_queue.size());
		temp_queue.removeFirst();
		Iterator <Integer> check = temp_queue.iterator();
		while (check.hasNext()){
			System.out.println("Success");
			check.next();
		}
		
		
	}

}
