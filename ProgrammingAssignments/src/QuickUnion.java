import java.util.Random;


public class QuickUnion {
	private int [] myArray = new int [10];
	
	private void initializeArray(){
		for (int i=0; i<10;i++){
			myArray[i]=i;
		}
	}
	private int[] getArray(){
		return myArray;
	}
	private int root( int x){
		while (x != myArray[x])
			x= myArray[x];
		return x;
	}
	
	private boolean isConnected(int x, int y){
		return root(x) == root(y);
	}
	
	private void union(int x, int y){
	 boolean result = isConnected(x,y);
	 if (result == false){
		 int i = root(x);
		 int j= root(y);
		 myArray[i]=j;
	  }
	 }
		
	 public static void main(String[] args){
			QuickUnion quickUnion = new QuickUnion();
			quickUnion.initializeArray();
			Random rand = new Random();
			for (int i=0;i<4;i++){
				int x= rand.nextInt(9)+0;
				int y = rand.nextInt(9)+0;
				quickUnion.union(x, y);
			}
			System.out.println(" The changed array is");
			int [] myArray = quickUnion.getArray();
			for (int i=0; i< myArray.length;i++){
				System.out.println(myArray[i]);
			}
	}
	
	

}
