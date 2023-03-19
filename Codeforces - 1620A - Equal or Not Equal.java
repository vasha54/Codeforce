/**
 * Codeforces - 1620A - Equal or Not Equal
 * Temáticas: Estructura de Datos + Disjoint Set
 *  
 *  Idea: Unir aquellos se dicen que son iguales y luego chequear que los que son
 *  diferentes no pertenezcan al mismo cojunto.
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
	private final int MAX_N = 10010;
	private final int MAX_TREE = (MAX_N << 2);
	private final char SYMBOL = '@';

	private int[] movX = {  0, 0, 1, -1 , 1,  1, -1, -1 };
	private int[] movY = { -1, 1, 0,  0 , 1, -1,  1, -1 };
	private long[] cards = { 1, 10, 100, 1000, 10000 };
	private long MOD = 1000000009;


	public void solve() throws Exception {
		int cases = nextInt(),nnodes,curr,next;
		
		while(cases>0) {
			cases--;
			String pattern=next();
			nnodes = pattern.length();
			
			DisJoinSet dsu = new DisJoinSet(nnodes);
			boolean correct = true;
			
			for(int i=0;i<nnodes;i++) {
				curr=i;
				next =(i+1) % nnodes;
				
				if(pattern.charAt(i)=='E')
					dsu.join(curr, next);
			}
			
			for(int i=0;i<nnodes && correct;i++) {
				curr=i;
				next =(i+1) % nnodes;
				
				if(pattern.charAt(i)=='N') {
					curr =dsu.root(curr);
					next =dsu.root(next);
					if(curr == next) correct=false;
				}
			}
			
			out.printf("%s\n", (correct?"YES":"NO"));
		}

	}

	Main() throws Exception {
		/*
		 * Esta entrada se debe activar cuando se hace una ejercicio de lectura hasta
		 * fin de fichero copiar la entrada en un fichero "Input.txt" y comentar el otro
		 * in . A la hor de enviar comentar este y descomentar el otro
		 */
		//in = new BufferedReader(new FileReader("Input.txt"));
		// out = new PrintWriter(new FileWriter("Output.txt"));
		in = new BufferedReader(new InputStreamReader(System.in));
		out = new PrintWriter(System.out);
		eat("");
		solve();
		in.close();
		out.close();
	}

	private void eat(String str) {
		st = new StringTokenizer(str);
	}

	private String next() throws Exception {
		while (!st.hasMoreTokens()) {
			String line = in.readLine();
			if (line == null)
				return null;
			eat(line);
		}
		return st.nextToken();
	}

	private int nextInt() throws Exception {return Integer.parseInt(next());}

	private long nextLong() throws Exception {return Long.parseLong(next());}

	private double nextDouble() throws Exception {return Double.parseDouble(next());}

	public static void main(String[] args) throws Exception {new Main();}  

	private class DisJoinSet{
		public int [] parent;
		public int [] sizes ;
		public int ncomponents;

		public DisJoinSet(int n) {
			this.ncomponents = n;
			parent = new int [this.ncomponents+1];
			sizes = new int [this.ncomponents+1];
			for(int i=0;i<this.ncomponents+1;i++) sizes[parent[i]=i]=1;
		}

		public int root(int x){
			if (x == parent[x]) return x;
			else{
				parent[x] = root(parent[x]);
				return parent[x];
			}
		}

		void join(int a,int b){
			int x = root(a); int y = root(b);
			if(x != y) {
				if(sizes[x] < sizes[y]) {
					int tmp = x; x = y; y =tmp;
				}
				parent[y] = x;
				sizes[x] += sizes[y];
				this.ncomponents--;
			}
		}
	}
}
