package lab.programs.Program5;

import java.util.Scanner;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
    	Scanner sc = new Scanner(System.in);
        ApplicationContext context = new ClassPathXmlApplicationContext("config.xml");
        Ticket tc = (Ticket) context.getBean("ticket");
        Customer c =(Customer) tc.getCus();
        
        while(true) {
        	System.out.println("1-Read Details\n2-Display\n3-Exit");
        	System.out.print("Enter your Choice : ");
        	int ch = sc.nextInt();
        	switch(ch) {
        	case 1:
        		System.out.println("***********TICKET***********");
        		System.out.print("Enter Ticket ID : ");
        		tc.setTid(sc.nextInt());
        		System.out.print("Enter Ticket Price : ");
                tc.setPrice(sc.nextFloat());
                System.out.println("Enter Destination : ");
                tc.setDestination(sc.next());
                System.out.println("**********CUSETOMER***********");
                System.out.println("Enter Customer name : ");
                c.setName(sc.next());
                System.out.println("Enter Customer age : ");
                c.setAge(sc.nextInt());
                System.out.println("Enter Customer Address : ");
                c.setAddress(sc.next());
        		break;
        	case 2:
        		System.out.println("============TICKET DETAILS=========");
                System.out.println(tc.toString());
                System.out.println("===================================");
        		break;
        	case 3:
        		
        		break;
        	default:
        		System.out.println("Invalid Entry!!!");
        	}
        }
        
		
    }
}
