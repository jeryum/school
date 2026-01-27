import java.util.Scanner;

public class YanggieComlab {

    public static void main(String[] args) {

        Scanner enter = new Scanner(System.in);

        System.out.print("Employee name: ");
        String name = enter.nextLine();

        System.out.print("Employee id: ");
        int id = enter.nextInt();

        System.out.print("Enter hourly rate: ");
        int rate = enter.nextInt();

        System.out.print("Enter regular hours: ");
        int regular = enter.nextInt();

        System.out.print("Enter overtime hours: ");
        int overtime = enter.nextInt();

        int regularPay = regular * rate;
        double overtimePay = rate * overtime * 1.5;
        double grossPay = regularPay + overtimePay;

        System.out.println("\n--- PAY SLIP ---");
        System.out.println("Name: " + name);
        System.out.println("ID: " + id);
        System.out.println("Regular Pay: " + regularPay);
        System.out.println("Overtime Pay: " + overtimePay);
        System.out.println("Gross Pay: " + grossPay);

        enter.close();
    }
}
