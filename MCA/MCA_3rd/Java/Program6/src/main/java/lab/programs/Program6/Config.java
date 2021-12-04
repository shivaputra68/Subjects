package lab.programs.Program6;

import java.util.Scanner;

import org.springframework.beans.factory.annotation.Configurable;
import org.springframework.context.annotation.Bean;


@Configurable

public class Config {

	Scanner sc = new Scanner(System.in);
	@Bean
	public Customer getCustomer() {
		
		return new Customer();
		
	}
	
	@Bean
	public Ticket getTecket() {
		Ticket t = new Ticket();
		t.setCus(getCustomer());
		return t;
	}
}
