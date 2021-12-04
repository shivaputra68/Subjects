package Program2;
import java.util.HashMap;
import java.util.Scanner;
import java.util.TreeMap;
import java.util.Set;
public class treeMap {

	String roll;
	String name;
	int age;
	
	treeMap(String name,String roll,int age){
		this.name=name;
		this.age=age;
		this.roll=roll;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		TreeMap<String,treeMap> hm = new TreeMap<String,treeMap>();
		while (true)
		{
			System.out.println("1. add elements\n2. display\n3. search\n4. Empty check\n5. size\n6. remove elements\n7. List the values\n8. exit");
			System.out.println("Enter you choice: ");
			int choice = sc.nextInt();
			switch (choice) {
			case 1:
				System.out.println("Enter the name: ");
				String name = sc.next();
				System.out.println("Enter the roll no: ");
				String roll = sc.next();
				System.out.println("Enter the age: ");
				int age = sc.nextInt();
				treeMap g1 = new treeMap(name,roll,age);
				hm.put(name, g1);
				System.out.println("------------------------------------------------");
				break;
				
			case 2:
				Set<String> s = hm.keySet();
				for(String keys : s) {
					System.out.println(keys+" " +hm.get(keys).name+" "+hm.get(keys).roll+" "+hm.get(keys).age);
				}
				
				break;
			case 3:
				System.out.println("Enter the key to search the record :");
				String names = sc.next();
				Boolean flag = hm.containsKey(names);
				if (flag==true){
					System.out.println("The concerned key exits!!!");
				}
				else {
					System.out.println("Sorry unable to search !!!");
				}
				System.out.println("------------------------------------------------");
				break;
			case 4:
				System.out.println("Choice 4");
				System.out.println("------------------------------------------------");
				Boolean flag2 = hm.isEmpty();
				if (flag2==true){
					System.out.println("The Hash map is empty!!!");
				}
				else {
					System.out.println("The Hash map is not empty!!!");
				}
				System.out.println("------------------------------------------------");
				break;
				
			case 5:
				System.out.println("Choice 5");
				System.out.println("------------------------------------------------");
				System.out.print("The Size is: ");
				System.out.println(hm.size());
				System.out.println("------------------------------------------------");
				break;
			case 6:
				System.out.println("Enter the key to remove from the hash map");
				String key_name = sc.next();
				System.out.println(hm.remove(key_name)+" removed successfully ");
				System.out.println("------------------------------------------------");
				break;
			
			case 7:
				System.out.println("The values are: ");
				System.out.println(hm.values());
				System.out.println("------------------------------------------------");
			default:
				break;
			}
		}
	}
}
