package lab.programs.Program6;

import java.util.Scanner;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Cust_Tick {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		ApplicationContext context = new AnnotationConfigApplicationContext(Config.class);
		Ticket tick = context.getBean(Ticket.class);
		Customer c = (Customer) tick.getCus();
		while (true) {
			System.out.println("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@");
			System.out.println("1-Read Details\n2-Display\n3-Exit");
			System.out.println("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@");
			System.out.print("Enter your choice : ");
			int ch = sc.nextInt();
			switch(ch) {
			case 1:
				System.out.println("***********CUSTOMER*************");
				System.out.print("Customer Name : ");
				c.setName(sc.next());
				System.out.print("Customer Age : ");
				c.setAge(sc.nextInt());
				System.out.print("Customer Address : ");
				c.setAddress(sc.next());
				System.out.println("***********TICKET*************");
				System.out.print("Enter Ticket Id : ");
				tick.setTno(sc.nextInt());
				System.out.print("Enter Seat no : ");
				tick.setSeatno(sc.nextInt());
				System.out.print("Enter Ticket Price : ");
				tick.setPrice(sc.nextFloat());
				break;
			case 2:
				System.out.println("================TICKET DETAILS=================");
				System.out.println(tick.toString());
				System.out.println("===============================================");
				break;
			case 3:
				break;
			default:
				System.out.println("Invalid Entry!!!");
			}
			
		}
	}

}
