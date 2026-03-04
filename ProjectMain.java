package projectG5;

import java.util.Date;
import java.util.Scanner;
import java.util.InputMismatchException;

public class ProjectMain 
{
    public static void main(String[] args)
    {
        int  type;
        boolean exit = true;
        Scanner input = new Scanner(System.in);
        Date todayDates = new Date();
        Transportation transport[] = new Transportation[10];
        transport[0] = new Unscheduled("Taxi", 2, 70);
        transport[1] = new Scheduled("Bus", 1, 50, 5, 10, 8, 0);
        
        
        do{
            System.out.println("Main Menu: \n 1. Add Transport\n 2. Select Transport\n 3. Exit");
            System.out.print("Please enter choices: ");
            String choice = input.nextLine();
            switch(choice)
            {
                case "1": System.out.println("Transport type:\n 1. Without scheduled\n 2. With scheduled");
                        System.out.print("Enter type of transport: ");
                        type = input.nextInt();
                        addTransport(transport, type); break;
                 case "2": selectTransport(transport); break;
            
                 case "3": System.out.println("Thank you for using the program. "); 
                         exit = false;
                         break;
                         
                 default: System.out.println("Invalid input. "); break;
            }
        }while(exit);
        
    }
    
    public static void addTransport(Transportation[] t, int add)
    {    
        Scanner input = new Scanner(System.in);
        String name;
        int  speed, frequency, trips, hour, minute;
        double price;
        
        System.out.print("Transport name: ");
        name = input.nextLine();
        System.out.print("Price per KM (RM): ");
        price = input.nextInt();
        System.out.print("Speed (KM/Hour): ");
        speed = input.nextInt();
        
        if (add == 1)
        {
            t[Transportation.count] = new Unscheduled(name, price, speed);
        }
        
        else if (add == 2)
        {
            System.out.println("Speed (KM/Hour): ");
            t[Transportation.count] = new Scheduled();
        }
    }
    
    public static void selectTransport(Transportation[] t)
    {
        Scanner input = new Scanner(System.in);
        int choice, hour, minute, second = 0;
        double distance;
        String time, t1, t2;
        
        for (int i = 0; i < Transportation.count; i++)
        {
            System.out.println((i + 1) + ". " + t[i].name);
        }
        
        System.out.print("Please select transport: ");
        choice = input.nextInt();
        System.out.println(t[choice - 1].toString());
        
        System.out.print("Please enter distance(KM): ");
        distance = input.nextInt();
        System.out.print("Please enter departure time (00:00): ");
        time = input.next();
        hour = Integer.parseInt(time.substring(0, 2));
        minute = Integer.parseInt(time.substring(3));
        
        System.out.println("Travelling fee: " + t[choice - 1].travellingFee(distance));
        System.out.println("Travelling time: " + t[choice - 1].travellingTime(distance));
        System.out.println("Arrival time: " + t[choice - 1].arrivalTime(hour, minute, distance));
    }
}