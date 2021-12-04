package lab.programs.Program6;

public class Ticket {
	
	int tno,seatno;
	float price;
	Customer cus;
	
	@Override
	public String toString() {
		return "Ticket No : " + tno + "\nSeatNo : " + seatno + "\nPrice=" + price + "\nCustomer Name : " + 
	cus.getName()+ "\nCustomer Age : "+cus.getName()+"\nCustomer Address : "+cus.getAddress();
	}
	public Customer getCus() {
		return cus;
	}
	public void setCus(Customer cus) {
		this.cus = cus;
	}
	public int getTno() {
		return tno;
	}
	public void setTno(int tno) {
		this.tno = tno;
	}
	public int getSeatno() {
		return seatno;
	}
	public void setSeatno(int seatno) {
		this.seatno = seatno;
	}
	public float getPrice() {
		return price;
	}
	public void setPrice(float price) {
		this.price = price;
	}

}
