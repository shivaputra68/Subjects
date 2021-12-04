package lab.programs.Program5;

public class Customer {
	
	private int age;
	private String name,address;
	public int getAge() {
		return age;
	}
	public void setAge(int id) {
		this.age = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}
	@Override
	public String toString() {
		return "Customer [id=" + age + ", name=" + name + ", address=" + address + "]";
	}
	
	
}
