package Program1;
import java.util.Scanner;
import java.util.ArrayList;
public class arrayList {
	String name, id, phone;
	arrayList(String name,String id,String phone){
		this.name = name;
		this.id=id;
		this.phone=phone;
	}
	
	public String toString() {
		return "Array Element : "+this.name+" "+this.id+" "+this.phone;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList<arrayList> al = new ArrayList<arrayList>();
		while(true) {
			System.out.println("1-Add records\n"
					+ "2-Display\n 3-Remove\n4-Clear\n5-Exit");
			System.out.println("Enter your choice : ");
			int ch = sc.nextInt();
			switch(ch) {
			case 1:
				System.out.println("Enter Name : ");
				String name = sc.next();
				System.out.println("Enter ID : ");
				String id = sc.next();
				System.out.println("Enter the phone : ");
				String phone = sc.next();
				al.add(new arrayList(name,id,phone));
				break;
			case 2:
				for(arrayList a : al) {
					System.out.println(a.name+" "+a.id+" "+a.phone);
				}
				break;
			case 3:
				System.out.println("Enter the index value between 0 and "+(al.size()-1)+" : ");
				int index = sc.nextInt();
				if(al.size()==1) {
					System.out.println("Element removed"+al.removeAll(al));
				}else if(al.size() == 0) {
					System.out.println("Empty List");
				}else {
					System.out.println("The element is removed"+al.remove(index));
				}
				break;
			case 4:
				al.clear();
				System.out.println("Empty list");
				break;
			case 5:
				
				break;
			default:
				System.out.println("Invalid option!!");
				break;
			}
		}
	}

}
