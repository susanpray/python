package helloword;

public class Puppy{
	   int puppyAge;
	   public Puppy(String name){
	      // �������������һ��������name
	      System.out.println("Passed Name is :" + name ); 
	   }

	   public void setAge( int age ){
	       puppyAge = age;
	   }

	   public int getAge( ){
	       System.out.println("Puppy's age is :" + puppyAge ); 
	       return puppyAge;
	   }

	   public static void main(String []args){
	      /* �������� */
	      Puppy myPuppy = new Puppy( "tommy" );
	      /* ͨ���������趨age */
	      myPuppy.setAge( 2 );
	      /* ������һ��������ȡage */
	      myPuppy.getAge( );
	      /*��Ҳ�����������������ʳ�Ա���� */
	      System.out.println("Variable Value :" + myPuppy.puppyAge ); 
	   }
	}

