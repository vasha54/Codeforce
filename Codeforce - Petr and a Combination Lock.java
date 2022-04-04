// Codeforce - Petr and a Combination Lock

/*
Tematica:Masacara de Bit 

Idea Basica: En las mascara de bit los bits activos son giros a la izquierda mientras los bit no activos
son giros a la derecha
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
   
    public void solve() throws Exception {
        int cTurn = nextInt();
        int [] turns = new int [cTurn];
        
        for(int i=0;i<cTurn;i++)
           turns[i]=nextInt();
           
        boolean isPosible =false;
        
        for(int i=0;i<(1<<cTurn) && isPosible == false;i++){
            int sum=0;
            for(  int j=0;j<cTurn;j++){
                if((i & (1<<j))==(1<<j)){
                    sum+=turns[j];
                }else{
                    sum-=turns[j];
                }
            }
            if(sum%360==0)isPosible =true;
        }
        
        out.printf("%s\n",((isPosible==true)? "YES":"NO"));
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
