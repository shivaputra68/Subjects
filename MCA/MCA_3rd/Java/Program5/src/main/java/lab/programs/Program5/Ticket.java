package lab.programs.Program5;

public class Ticket {
	
	private int tid;
	private float price;
	private String destination;
	private Customer cus;
	
	public Customer getCus() {
		return cus;
	}
	public void setCus(Customer cus) {
		this.cus = cus;
	}
	public int getTid() {
		return tid;
	}
	public void setTid(int tid) {
		this.tid = tid;
	}
	public float getPrice() {
		return price;
	}
	public void setPrice(float price) {
		this.price = price;
	}
	public String getDestination() {
		return destination;
	}
	public void setDestination(String destination) {
		this.destination = destination;
	}
	@Override
	public String toString() {
		return "Ticket Id : " + tid + "\nTicket Price : " + price + "\nDestination : " + destination + "\nCustomer Name : " + 
	cus.getName()+"\n Customer Age : "+cus.getAge() + "\nCustomer Address : "+cus.getAddress();
	}
	
	

}
