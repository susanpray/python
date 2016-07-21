package helloword;

public class Test{ 
   public void pupAge(){
      int age=0;
      age = age + 199;
      System.out.println("小狗的年龄是: " + age);
   }
   
   public static void main(String args[]){
      Test test = new Test();
      test.pupAge();
   }
}