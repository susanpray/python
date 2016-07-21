package helloword;


public class Test2 {
	public static void main(String[] args) {
		
		double[] mylist = {1.9, 2.9, 3.4, 3.5};
		for (double element: mylist){
			System.out.println(element);
		}
			
		double total = 0;
		for (int i=0; i < mylist.length; i++){
			total += mylist[i];
		}
		System.out.println("Total is " + total);
		
		double max = mylist[0];
		for (int i=0; i < mylist.length; i++){
			if (mylist[i] > max){
				max = mylist[i];
			}
		}
		System.out.println("Max is " + max);
			
	
		}

	}

