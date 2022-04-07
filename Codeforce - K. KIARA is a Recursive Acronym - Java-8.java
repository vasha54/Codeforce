// Codeforce - K. KIARA is a Recursive Acronym

/*
Tematica: String + Counting Sort 

Idea Basica: Ver si existe una palabra que todas sus letras sean letras de iniciales de las palabras de un listado.

*/
import java.io.*;
import java.math.*;
import java.util.*;
import java.util.*;
import java.lang.*;
import java.util.regex.*;


public class Main {
    
   
    
    private BufferedReader in;
    private PrintWriter out;
    private StringTokenizer st;
    private final int MAX_N = 510;
    
    private int [] movX = { 0, 0, 1, -1};
    private int [] movY = {-1, 1, 0,  0};
    private long [] cards ={1,10,100,1000,10000};
   
   
    public void solve() throws Exception {
        int nWords =nextInt(),checkLetters,pivot;
        
        boolean [] letters =new boolean [26];
        
        String [] listWords =new String[nWords];
        
        for(int i=0;i<nWords;i++){
            listWords[i]=next();
            letters[listWords[i].charAt(0)-'A']=true;
        }
        
        boolean find=false;
        
        for(int i=0;i<nWords && !find;i++){
            checkLetters = 1;
            pivot =1;
            
            while(pivot < listWords[i].length() && letters[listWords[i].charAt(pivot)-'A']==true){
              checkLetters++;
              pivot++;
            }
            
            if(checkLetters == listWords[i].length() )
                find=true;
        }
        
        out.printf("%s\n",(find==true)? "Y" : "N");
       
    }
    
    Main() throws Exception {
       /*Esta entrada  se debe activar cuando se hace una ejercicio de lectura hasta fin de fichero 
       copiar la entrada en un fichero "Input.txt" y comentar el otro in . A la hor de enviar comentar
       este y descomentar el otro
       */
       //in = new BufferedReader(new FileReader("Input.txt"));
       //out = new PrintWriter(new FileWriter("Output.txt"));
       in = new BufferedReader(new InputStreamReader(System.in));
	   out = new PrintWriter(System.out);
       eat("");
       solve();
       in.close();
       out.close();
    }

    private void eat(String str) { st = new StringTokenizer(str);}

    String next() throws Exception {
        while (!st.hasMoreTokens()) {
            String line = in.readLine();
            if (line == null) return null;
            eat(line);
        }
        return st.nextToken();
    }

    int nextInt() throws Exception {return Integer.parseInt(next());}

    long nextLong() throws Exception {return Long.parseLong(next());}

    double nextDouble() throws Exception {return Double.parseDouble(next());}

    public static void main(String[] args) throws Exception {new Main();}

}
