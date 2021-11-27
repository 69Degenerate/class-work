import java.util.*;
class student
{
     int rollno;
     String name;
     float salary;
     public void accept()          
    {
        Scannners s=new Scannner(System.in);
        System.out.println("enter the number:");
        rollno=s.nextInt();
        name=s.nextLine();
        salary=s.nextFloat();
    }
     public void display()
    {
     System.out.println("rollno:",rollno);  
     System.out.println("name:",name);
     System.out.println("salary:",salary);
    }
}
class run
{
    public static void main(String args[])
     {
      student s1=new student();
     s1.accept();
     s1.display();   
    }       
}