import java.util.Iterator;


public class RandomizedQueue<Item> implements Iterable<Item> {
	private Item [] randomQueue;
	private int N=0;
	private int initialSize=10;
    public RandomizedQueue(){
    	 
    	randomQueue= (Item[]) new Object[initialSize];
    }
    public boolean isEmpty(){
    	return N==0;
    }
    
    public int size(){
    	return N;
    }
    public void enqueue(Item item){
    	if (item == null){
    		throw new NullPointerException();
    	}
    	if (N<10){
    	randomQueue[N++]= item;
    	
    	}
    	else{
    		Item [] temp_queue = randomQueue;
    		initialSize= 2*initialSize;
    		randomQueue = (Item[]) new Object[initialSize];
    		for (int i=0; i<N;i++){
    			randomQueue[i]= temp_queue[i];
    		}
    		randomQueue[N++]= item;
    		
    	}
    }
    public Item dequeue(){
    	if (N < 1){
    	throw new NullPointerException();
    	}
    	else{
    		Item item = randomQueue[N-1];
    		randomQueue[N-1]= null;
    		N--;
    		return item;
    	}
    }
    
    public Item sample(){
    	
    	return randomQueue[0];
    }
    
	@Override
	public Iterator<Item> iterator() {
		// TODO Auto-generated method stub
		return new ListIterator();
	}
	private class ListIterator implements Iterator<Item>{
        private int i=N;
		@Override
		public boolean hasNext() {
			// TODO Auto-generated method stub
			return i >0;
		}

		@Override
		public Item next() {
			// TODO Auto-generated method stub
			
			return randomQueue[--i];
		}

		@Override
		public void remove() {
			// TODO Auto-generated method stub
			
		}
		
	}
	
	public static void main(String[] args){
		try{
		RandomizedQueue<Integer> queue = new RandomizedQueue<Integer>();
		for (int i=0;i<20;i++){
			queue.enqueue(i*2);
		}
		for (int i=30;i>22;i--)
		   queue.dequeue();
		System.out.println("Size of queue is ");
		System.out.println(queue.size());
		Iterator<Integer> iter= queue.iterator();
		while(iter.hasNext()){
			System.out.println("Success");
			iter.next();
		}
		}
		catch(NullPointerException e){
			System.out.println("No more elements left");
		}
		
	}

}
