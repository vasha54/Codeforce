/*
Codeforce - A. Translation - 41A

Tematica: String

Idea basica: Verificar si una cadena es la inversa de la otra 
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
            string wordBerlandish = Console.ReadLine();
            string wordBirlandish = Console.ReadLine();

            if(wordBirlandish.Length == wordBerlandish.Length){
               
              bool isReverse = true;

              for(int i=0, j=wordBerlandish.Length-1; i<wordBirlandish.Length && j>=0 && isReverse == true; i++, j-- ){
                if( wordBirlandish[i] != wordBerlandish[j]) isReverse= false;
              } 

              Console.WriteLine(( isReverse == true ? "YES":"NO"));

            }else{
                    Console.WriteLine("NO");
            }
        }

        public static void Main(string[] args)
        {
            Program p = new Program(); 
            p.solve();
        }
    }
}

