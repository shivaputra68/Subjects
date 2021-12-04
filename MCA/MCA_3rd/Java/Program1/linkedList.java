package Program1;
import java.util.Scanner;
import java.util.LinkedList;
public class linkedList {
	String name,branch,result;
	linkedList(String name,String branch,String result){
		this.name=name;
		this.branch=branch;
		this.result=result;
	}
	
	public String toString() {
		return this.name+" "+this.branch+" "+this.result;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		LinkedList<linkedList> ll = new LinkedList<linkedList>();
		while(true) {
			System.out.println("1-Add records\n"
					+ "2-Display\n 3-Remove\n4-Clear\n5-Exit");
			System.out.println("Enter your choice : ");
			int ch = sc.nextInt();
			switch(ch) {
			case 1:
				System.out.println("Enter Name : ");
				String name = sc.next();
				System.out.println("Enter branch : ");
				String branch = sc.next();
				System.out.println("Enter result : ");
				String result = sc.next();
				System.out.println("ADD at : 1-First\n2-Middle\n3-Last\n");
				int c = sc.nextInt();
				switch(c) {
				case 1:
					ll.addFirst(new linkedList(name,branch,result));
					System.out.println("Inserted at 1st");
					break;
				case 2:
					System.out.println("Enter the posistion between 0 to "+(ll.size()-1)+" : ");
					int pos  = sc.nextInt();
					ll.add(pos,new linkedList(name,branch,result));
					System.out.println("inserted at middle");
					break;
				case 3:
					ll.addLast(new linkedList(name,branch,result));
					System.out.println("inserted at last");
					break;
				default:
					ll.add(new linkedList(name,branch,result));
					break;
				}
				break;
			case 2:
				for(linkedList a : ll) {
					System.out.println(a.name+" "+a.branch+" "+a.result);
				}
				break;
			case 3:
				System.out.println("Remove at : 1-First\n2-Middle\n3-Last\n");
				int cho = sc.nextInt();
				switch(cho) {
				case 1:
					ll.removeFirst();
					System.out.println("removed at 1st");
					break;
				case 2:
					System.out.println("Enter the posistion between 0 to "+(ll.size()-1)+" : ");
					int pos  = sc.nextInt();
					ll.remove(pos);
					System.out.println("removed at middle");
					break;
				case 3:
					ll.removeLast();
					System.out.println("removed at last");
					break;
				default:
					break;
				}
				break;
			case 4:
				System.out.println("Get at : 1-First\n2-Middle\n3-Last\n");
				int choice = sc.nextInt();
				switch(choice) {
				case 1:
					
					System.out.println("1st element : "+ll.getFirst());
					break;
				case 2:
					System.out.println("Enter the posistion between 0 to "+(ll.size()-1)+" : ");
					int pos  = sc.nextInt();
					
					System.out.println(pos +" element is "+ll.get(pos));
					break;
				case 3:
					
					System.out.println("last element" +ll.getLast());
					break;
				default:
					
					break;
				}
				break;
			case 5:
				break;
			default:
				break;
			}
		}

	}

}
