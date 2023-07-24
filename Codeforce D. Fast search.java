/**
 * Codeforce D. Fast search
 * Temáticas: Busqueda Binaria 
 *  
 * Idea:
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
	private final int MAX_N = 110;
	private final int MAX_TREE = (MAX_N << 2);
	private final char SYMBOL = '@';

	private int[] movX = { 0, 0, 1, -1 };
	private int[] movY = { -1, 1, 0, 0 };
	private long[] cards = { 1, 10, 100, 1000, 10000 };
	private long MOD = 1000000009;

	public void solve() throws Exception {
		int nvalues = nextInt();

		long r, l,minR,maxR;
		long[] values = new long[nvalues];

		for (int i = 0; i < nvalues; i++) {
			values[i] = nextLong();
		}
		Arrays.sort(values);
		int queries = nextInt(), answer;
		
		for(int i=0;i<queries;i++) {
			l = nextLong();
			r = nextLong();
			minR = Math.min(r, l);
			maxR = Math.max(r, l);
			if(i!=0) out.print(" ");
			
			if(maxR < values[0]) out.print(0);
			else if(minR > values[nvalues-1]) out.print(0);
			else {
				int iL = searchClosetLeft(values,minR);
				int iR = searchClosetRigth(values,maxR);
				out.print(iR-iL+1);
			}
			
		}
	}

	

	private int searchClosetRigth(long[] values, long maxR) {
		int index =-1;
		int begin = 0;
		int end = values.length-1;
		int pivot;
		
		while(begin<=end) {
			pivot= (begin+end)/2;
			if(values[pivot]<=maxR) {
				if(index==-1)
					index = pivot;
				else
					index = Math.max(index,pivot);
				begin = pivot +1;
			}else
				end = pivot-1;
		}
		
		return index;
	}



	private int searchClosetLeft(long[] values, long minR) {
		int index =-1;
		int begin = 0;
		int end = values.length-1;
		int pivot;
		
		while(begin<=end) {
			pivot= (begin+end)/2;
			if(values[pivot]>=minR) {
				if(index==-1)
					index=pivot;
				else 
					index = Math.min(index,pivot);
				end=pivot-1;
			}else
				begin=pivot+1;
		}
		
		return index;
	}



	Main() throws Exception {
		/*
		 * Esta entrada se debe activar cuando se hace una ejercicio de lectura hasta
		 * fin de fichero copiar la entrada en un fichero "Input.txt" y comentar el otro
		 * in . A la hor de enviar comentar este y descomentar el otro
		 */
		// in = new BufferedReader(new FileReader("Inpu.txt"));
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

	String next() throws Exception {
		while (!st.hasMoreTokens()) {
			String line = in.readLine();
			if (line == null)
				return null;
			eat(line);
		}
		return st.nextToken();
	}

	int nextInt() throws Exception {
		return Integer.parseInt(next());
	}

	long nextLong() throws Exception {
		return Long.parseLong(next());
	}

	double nextDouble() throws Exception {
		return Double.parseDouble(next());
	}

	public static void main(String[] args) throws Exception {
		new Main();
	}

}