package com.mycompany.ict2113_assignmenty1g4;

public class ICT2113_Y1G4Student 
{
    private String studName, studId, studProgram;   
    private double accumulatedTotal;
    static int count = 10;
    
    public ICT2113_Y1G4Student(String studName, String studId, String studProgram, double accumulatedTotal) 
    {
        this.studName = studName;
        this.studId = studId;
        this.studProgram = studProgram;
        this.accumulatedTotal = accumulatedTotal;
    }

    public ICT2113_Y1G4Student() 
    {
    }
    
    public void setStudName(String studName) 
    {
        this.studName = studName;
    }

    public void setStudId(String studId) 
    {
        this.studId = studId;
    }

    public void setStudProgram(String studProgram) 
    {
        this.studProgram = studProgram;
    }
    
    public void setAccumulatedTotal(double accumulatedTotal) 
    {
        if (accumulatedTotal >= 0 && accumulatedTotal <= 100)
            this.accumulatedTotal = accumulatedTotal;
    }
    
    public double getCgpa()
    {
        return accumulatedTotal / 25;
    }

    @Override
    public String toString() 
    {
        return "Student Name: " + studName + "\nStudent ID: " + studId + "\nStudent Program: " + studProgram + "\nAccumulated Total: " + accumulatedTotal + "\nCGPA: " + getCgpa() + "\n ";
    }
    
}
