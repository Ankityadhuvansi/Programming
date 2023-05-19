/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-->0){
            int number = sc.nextInt();
            // sc.nextLine();
            String str = sc.next();
            // str.toLowerCase();
            if(number < 4){
                System.out.println("YES");
            }
            else{
                int count = 0;
                for(int i = 0; i<str.length(); i++){
                    if(count == 4){
                        break;
                    }
                    else if(str.charAt(i)=='a' || str.charAt(i) =='e' || str.charAt(i) == 'i' || str.charAt(i) == 'o' || str.charAt(i) == 'u'){
                        count = 0;
                    }
                    else{
                        count++;
                    }
                }
                if(count == 4){
                    System.out.println("NO");
                }
                else{
                    System.out.println("YES");
                }
            }
        }
	}
}
