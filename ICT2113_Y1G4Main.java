package com.mycompany.ict2113_assignmenty1g4;

import java.util.Scanner;

public class ICT2113_Y1G4Main 
{
    public static void main (String[] args)
    {
        String studName[] = {"Joshua", "Kelly", "Ivan", "Daniel", "Mike", "Michelle", "Mathew", "Julia", "Isaac", "Christopher", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null"};
        String studId[] = {"J220", "J221", "J222", "J223", "J224", "J225", "J226", "J227", "J228", "J229", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null"};
        String studProgram[] = {"DITN","DITN","DITN","DITN","DITN","DITN","DITN","DITN","DITN","DITN", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null"};
        double accumulatedTotal[] = {89.00d, 94.00d, 76.00d, 67.00d, 84.00d, 79.00d, 82.00d, 69.00d, 96.00d, 65.00d, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  
        int highest = 0, lowest = 0, choice;
        double temp = accumulatedTotal[0]; //initialized the temp variable to use and compare with the value from the accumulated total array.
        Scanner input = new Scanner(System.in);
        
        // a for loop to find the highest score student from the initialized value.
        for (int i = 0; i < ICT2113_Y1G4Student.count; i++)
        {
            if (temp < accumulatedTotal[i])
            {
                temp = accumulatedTotal[i];
                highest = i; //keep track of the highest value in the array and store it in highest variable.
            }
        }
        
        // a for loop to find the lowest score student from the initialized value.
        for (int i = 0; i < ICT2113_Y1G4Student.count; i++)
        {
            if (temp > accumulatedTotal[i])
            {
                temp = accumulatedTotal[i];
                lowest = i; //keep track of the lowest value in the array and store it in lowest variable.
            }
        }
        
        ICT2113_Y1G4Student highestScoreStud = new ICT2113_Y1G4Student(studName[highest], studId[highest], studProgram[highest], accumulatedTotal[highest]); //create highest score student object and store the highest score student inside.
        ICT2113_Y1G4Student lowestScoreStud = new ICT2113_Y1G4Student(studName[lowest], studId[lowest], studProgram[lowest], accumulatedTotal[lowest]); //create lowest score student object and store the lowest score student inside.
        
        //do while loop to repeat the action to carry out if user enter an unexpected value.
        do
        {
            System.out.println("Function Option: \n 1. Add Student \n 2. Show Score \n 3. Quit\n");
            System.out.print("Enter choices to proceed: ");
            choice = input.nextInt();
            
        
            switch(choice)
            {
                case 1: addStudent(highestScoreStud, lowestScoreStud, studName, studId, studProgram, accumulatedTotal, ICT2113_Y1G4Student.count); break;//pass the student object as reference and pass all the 4 array to the add student method. 
                case 2: showScore(highestScoreStud, lowestScoreStud); break;
                case 3: System.out.println("Thank you for using the program."); break;
            }       
            
            //Print error message when user enter unexpected value.
            if(choice < 0 || choice > 3)
            {
                System.out.println("Please Enter choices from(1 - 3).\n");
            }
        }
        
        while (choice != 3);        
    }   
    
    public static void addStudent(ICT2113_Y1G4Student highestScoreStud, ICT2113_Y1G4Student lowestScoreStud, String studName[], String studId[], String studProgram[], double accumulatedTotal[], int add)
    {
        Scanner input = new Scanner(System.in);
        int highest = 0, lowest = 0;
        double temp = accumulatedTotal[0];
        int hold = 0;
        
        //Enter the new student information
        System.out.print("Enter student name: ");
        studName[add] = input.nextLine();
        
        //Determine whether the student id enter by user is not repeated from the initialized array because student id is unique number.
        do
        {
            System.out.print("Enter student ID: ");
            studId[add] = input.next();
            studId[add] = studId[add].toUpperCase();
            
            for (int i = 0; i < add; i++)
            {
                if(studId[add].equals(studId[i]))
                {
                    hold = i; //if the student id is same it will keep track of it and store it in hold variable.
                }   
            }
            
            //Print error message when user enter unexpected value.
            if(studId[add].equals(studId[hold]))
            {
                System.out.println("The student ID is an existing ID please enter a new ID. ");
            }
        }
        
        while (studId[add].equals(studId[hold]));
  
        System.out.print("Enter student program: ");
        studProgram[add] = input.next();
        studProgram[add] = studProgram[add].toUpperCase();
        
        //Make sure that the score enter by user is between 0 and 100.
        do
        {
            System.out.print("Enter student accumulated total: ");
            accumulatedTotal[add] = input.nextDouble();
            
            if (accumulatedTotal[add] < 0 || accumulatedTotal[add] > 100)
            {
                System.out.println("Please enter score within (0 - 100)");
            }
        }
        
        while(accumulatedTotal[add] < 0 || accumulatedTotal[add] > 100);

        System.out.println("Succesfully add student! \n");
        
        //Update the highest and lowest score student from the array.
        for (int i = 0; i <= ICT2113_Y1G4Student.count; i++)
        {
            if (temp < accumulatedTotal[i])
            {
                temp = accumulatedTotal[i];
                highest = i;
            }
        }
        
        for (int i = 0; i <= ICT2113_Y1G4Student.count; i++)
        {
            if (temp > accumulatedTotal[i])
            {
                temp = accumulatedTotal[i];
                lowest = i;
            }
        }
        
        //Store the updated highest and lowest score student into the highest and lowest score student object.
        highestScoreStud.setStudName(studName[highest]);
        highestScoreStud.setStudId(studId[highest]);
        highestScoreStud.setStudProgram(studProgram[highest]);
        highestScoreStud.setAccumulatedTotal(accumulatedTotal[highest]);
        
        lowestScoreStud.setStudName(studName[lowest]);
        lowestScoreStud.setStudId(studId[lowest]);
        lowestScoreStud.setStudProgram(studProgram[lowest]);
        lowestScoreStud.setAccumulatedTotal(accumulatedTotal[lowest]);   
    }
    
    public static void showScore(ICT2113_Y1G4Student highestScoreStud, ICT2113_Y1G4Student lowestScoreStud)
    {
        //Print the highest and lowest score student object by calling to string method.
        System.out.println("Highest score student: \n" + highestScoreStud.toString());
        System.out.println("Lowest score student: \n" + lowestScoreStud.toString() + "\n");
    }
}
