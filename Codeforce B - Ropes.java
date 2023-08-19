/**
 * Codeforce B - Ropes
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
	private final int MAX_N = 1000010;
	private final int MAX_TREE = (MAX_N << 2);
	private final char SYMBOL = '@';

	private int[] movX = { 0, 0, 1, -1 };
	private int[] movY = { -1, 1, 0, 0 };
	private long[] cards = { 1, 10, 100, 1000, 10000 };
	private long MOD = 1000000007;
	private double ERROR = 1e-9;

	public void solve() throws Exception {
		int npieces=nextInt(),k=nextInt();
		long [] pieces =new long [npieces];
		for(int i=0;i<npieces;i++) 
			pieces[i]=nextLong();
		
		Arrays.sort(pieces);
		
		double begin,end,pivot;
		
		begin=0;
		end=pieces[npieces-1];
		
		while(Math.abs(end-begin)>ERROR) {
			pivot=(begin+end)/2;
			if(goodCut(pivot,pieces,k))
				begin=pivot;
			else
				end=pivot;
		}
		
		out.printf("%.20f\n",begin);
	}

	

	private boolean goodCut(double x, long[] pieces, int k) {
		if (x == 0) return true;
		int cutTotal=0;
		for(int i=0;i<pieces.length && cutTotal<k;i++) {
			cutTotal+=(pieces[i]/x);
		}
		
		return (cutTotal>=k);
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