/*
Codeforce A. Word - 59A

Tematica: String

Idea basica: Dada una palabra contar la cantidad de minúsculas y mayúsculas de la palabra
En caso que la cantidad de minusculas sea igual o mayor que la cantidad de mayusculas se
debe imprimir la palabra en minúsculas sino en mayúsculas 
*/

using System;

namespace JudgeOnline
{
    public class Program
    {
    	private const int MAX_N = 55;
        private const long MOD = 10000009;

        private int gcd(int _a,int _b){
            while(_b>0){
                _a=_a%_b;
                _a^=_b;
                _b^=_a;
                _a^=_b;
            }
            return _a;
        }

    	
        public Program(){}

        public void solve(){
            int lowers = 0;
            int uppers = 0;
            string input = Console.ReadLine();
            string convert = "";

            for(int i=0;i<input.Length;i++){
                if('a' <= input[i] && input[i]<='z'){
                    lowers++;
                }
                if('A' <= input[i] && input[i]<='Z'){
                    uppers++;
                }
            }

            for(int i=0;i<input.Length;i++){
                if(lowers >= uppers && 'A' <= input[i] && input[i]<='Z' ){
                    int x =  (int) input[i]- (int)'A';
                    char s = (char) ((int)'a'+x);
                    convert = convert + s;
                }else if (lowers < uppers && 'a' <= input[i] && input[i]<='z' ){
                    int x =  (int) input[i]- (int)'a';
                    char s = (char) ((int)'A'+x);
                    convert = convert + s;
                }else{
                    convert=convert+input[i];
                }
            }

            Console.WriteLine(convert);
        }

        public static void Main(string[] args)
        {
            Program p = new Program(); 
            p.solve();
        }
    }
}

