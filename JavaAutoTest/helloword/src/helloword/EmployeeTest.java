package helloword;

public class EmployeeTest {
	public static void main(String args[]){
	      /* ʹ�ù����������������� */
	      Employee empOne = new Employee("James Smith");
	      Employee empTwo = new Employee("Mary Anne");
	      Employee empThree = new Employee("susan wang");
	      // ��������������ĳ�Ա����
	      empOne.empAge(26);
	      empOne.empDesignation("Senior Software Engineer");
	      empOne.empSalary(1000);
	      empOne.printEmployee();
	      System.out.println("++++++++++++++++++");

	      empTwo.empAge(21);
	      empTwo.empDesignation("Software Engineer");
	      empTwo.empSalary(500);
	      empTwo.printEmployee();
	      System.out.println("++++++++++++++++++");
	      
	      empThree.empAge(65);
	      empThree.empDesignation("Software testing Engineer");
	      empThree.empSalary(800);
	      empThree.printEmployee();
	      System.out.println("++++++++++++++++++");
	      
	   }
}
