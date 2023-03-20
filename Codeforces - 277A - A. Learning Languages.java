/**
 * Codeforces - 277A - A. Learning Languages
 * Temáticas: Estructura de Datos + Disjoint Set
 *  
 *  Idea: Dado un grupo de personas y los idiomas que estos hablan detectar los
 *  grupos comunicacionales que se pueden crear. Dos personas están en un mismo 
 *  grupo comunicacional si enetre ellos tiene un idioma común o existe un grupo
 *  de personas que le pueden servir de traductor. La solución es contar la 
 *  cantidad grupo comuniciales que existen y a ese valor restarle uno porque
 *  es la minima cantidad de empleados que deben aprender un nuevo idioma
 *  para que todos los empleados se puedan comunicar tener en cueanta que si todo
 *  los grupos tienen ningun lenguaje entonces es todos los grupos
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
		int npersons = nextInt(),nlanguages = nextInt();
		ArrayList< Set<Integer> >persons = new ArrayList<Set<Integer> >();
		DisJoinSet dsu = new DisJoinSet(npersons);
		
		for(int i=0;i<npersons;i++) {
			int languajes = nextInt();
			persons.add( new TreeSet<Integer>());
			for(int j=0;j<languajes;j++){
				persons.get(i).add(nextInt());
				
			}
			dsu.languajes.get(i).addAll(persons.get(i));
		}
		
		
		for(int i=0;i<npersons;i++) {
			for(int j=i+1;j<npersons;j++) {
				Set<Integer> languajesI = persons.get(i);
				Set<Integer> languajesJ = persons.get(j);
				if(Collections.disjoint(languajesI, languajesJ)==false) {
					dsu.join(i,j);
				}
			}
		}
		
		ArrayList<Integer> groups = new ArrayList<Integer>();
		
		for(int i=0;i<npersons;i++) {
			if(dsu.parent[i] ==i) {
				//out.printf("%d -> %d\n",i,dsu.languajes.get(i).size());
				groups.add(dsu.languajes.get(i).size());
			}
		}
		
		Collections.sort(groups);
		
		int answer=groups.size()-1;
		
		if(groups.size()>=2 && groups.get(groups.size()-1)==0)
			answer++;
			
		
		out.printf("%d\n", answer);
		
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
		public List<Set<Integer> >  languajes;
		public int ncomponents;

		public DisJoinSet(int n) {
			this.ncomponents = n;
			parent = new int [this.ncomponents+1];
			sizes = new int [this.ncomponents+1];
			languajes = new ArrayList<Set<Integer> >();
			for(int i=0;i<this.ncomponents+1;i++) { 
				sizes[parent[i]=i]=1;
				languajes.add(new TreeSet<Integer>());
			}
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
				languajes.get(x).addAll(languajes.get(y));
				this.ncomponents--;
			}
		}
	}
}
