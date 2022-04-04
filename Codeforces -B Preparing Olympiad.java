//Codeforces - Preparing Olympiad

/*
Tematica:Masacara de Bit 

Idea Basica: Generar todos los posibles subconjuntos y ver cuales cumple con las restriccones.
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
        int nProblem, answer =0, combinations;
        long [] problems;
        long minScore, maxScore, diferenceScore;
        nProblem = nextInt();
        
        problems =new long [nProblem];
        minScore = nextLong();
        maxScore = nextLong();
        diferenceScore = nextLong();
        
        for(int i=0;i<nProblem;i++)
           problems[i] = nextLong();
           
        
        for(int i=0;i<(1<<nProblem);i++){
            long sumScore =0;
            int cProblem = 0;
            long minProblem = Long.MAX_VALUE;
            long maxProblem = Long.MIN_VALUE;
            
            for(int j=0;j<nProblem;j++){
                if((i & (1<<j)) == (1<<j)){
                    cProblem++;
                    sumScore+=problems[j];
                    minProblem = Math.min(minProblem,problems[j]);
                    maxProblem = Math.max(maxProblem,problems[j]);
                }
            }
            
            if( minScore<= sumScore && sumScore<=maxScore && maxProblem-minProblem >=diferenceScore){
                answer++;
            }
        }
        
        out.println(answer);
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


