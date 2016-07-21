package helloword;
import java.io.*;
public class CheckingAccount {
	private double balance;
	private int number;
	public CheckingAccount(int number){
		this.number = number;
	}
	public void depoist(double amount){
		balance += amount;
	}
	public void withdraw(double amount) throws InsufficientFundsException{
		if(amount <= balance)
		{
			balance -=amount;
		}
		else
		{
			double needs = amount - balance;
			throw new InsufficientFundsException(needs);
		}
		
	}
	public double getBallance()
	{
		return balance;
	}
	public int getNumber()
	{
		return number;
	}

}
