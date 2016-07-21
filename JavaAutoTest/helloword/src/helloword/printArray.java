package helloword;


public class printArray {
	public static void printArray(int[] array) {
		for(int Element: array){
			System.out.println(Element);
		}	
	
	}
	public static void main(String[] args) {
		printArray(new int[]{3, 1, 2, 6, 4, 2});
	}

}
