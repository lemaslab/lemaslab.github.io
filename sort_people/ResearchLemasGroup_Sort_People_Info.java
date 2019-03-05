package sample_prjects;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ResearchLemasGroup_Sort_People_Info {
	
	
	public ResearchLemasGroup_Sort_People_Info(){
	File people=new File("C:\Users\Luran\Documents\GitHub\lemas-lab-group.github.io\_people");
	File[] listOfPeople = new File[5];
	listOfPeople = people.listFiles();
	String[] keyWord = {"name", "position", "avatar"};
	boolean found=false;
	for(int i=0;i<listOfPeople.length;i++) {
		
		Scanner scan;
		try {
			scan = new Scanner(listOfPeople[i]);
			for(int j=0;j<keyWord.length;j++) {
		while(scan.hasNext() || found==true){
	            String line = scan.nextLine();
	            if(line.contains(keyWord[j])){
	            	//line=line.substring(keyWord[j].length()-1);
	                System.out.println(line);
	                found=true;
	            }
		}
		found=false;
		}
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
	}	
		
	
	
}	
	
}


	   // public static void main(String[] args) throws FileNotFoundException{
	     //   FileSearch fileSearch = new FileSearch();
	       // fileSearch.parseFile("src/main/resources/test.txt", "am");
	    //}

	
	
	
	
	

