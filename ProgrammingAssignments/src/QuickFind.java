import java.util.Random;
import java.util.Scanner;


public class QuickFind {
	private int [] myArray = new int [10];
	
	private void initializeArray(){
		for (int i=0;i<10;i++){
			myArray[i]=i;
		}
	}
	
	private boolean isConnected(int posX, int posY){
		return myArray[posX]== myArray[posY];
	}
	public int[] getArray(){
		return myArray;
	}
	private void union (int x, int y){
		boolean result = isConnected(x,y);
		if (result ==false){
			int idx = myArray[x];
			int idy = myArray[y];
			for (int i=0; i<myArray.length;i++){
				if (myArray[i]== idx)
					myArray[i]=idy;
			}
		}
	}
	
	public static void main(String[] args){
		QuickFind quickFind = new QuickFind();
		quickFind.initializeArray();
		Random rand = new Random();
		for (int i=0;i<4;i++){
			int x= rand.nextInt(9)+0;
			int y = rand.nextInt(9)+0;
			quickFind.union(x, y);
		}
		System.out.println(" The changed array is");
		int [] myArray = quickFind.getArray();
		for (int i=0; i< myArray.length;i++){
			System.out.println(myArray[i]);
		}
		
	}
	

}
