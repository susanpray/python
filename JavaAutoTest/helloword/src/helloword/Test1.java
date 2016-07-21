package helloword;

import java.util.Scanner;

import javax.xml.bind.annotation.XmlElementDecl.GLOBAL;



public class Test1 {
//		@SuppressWarnings("resource")
		public static void main(String args[]) {
			Scanner scanner = new Scanner(System.in);
			System.out.println("please input a age and name:");
			if (scanner.hasNext()){
				int age = scanner.nextInt();
				System.out.println("age is : " + age);
			}
			
			System.out.println("please input a name:");
			if (scanner.hasNext()){
				String name = scanner.next();
				System.out.println("name is : " + name);
			}
				
//			System.out.println(name + " is " + age + " years old ");
			}	
	}

