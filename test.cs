using System;
using System.Collections.Generic;


namespace TestLib
{
    public class SecretOp
    {
        private int internalVal1 = 1;
        private int internalVal2 = 1;

        public  void Main(string[] args)
        {
            Console.WriteLine ("Hello Mono World");
        }

        public  SecretOp(int newVal1, int newVal2)
        {
            internalVal1 = newVal1;
            internalVal1 = newVal2;
        }
        
        public int computeInternal()
        {
            int temp = 0;

            temp = internalVal1 + internalVal2;
            temp = temp * 3;

            return temp;
        }

        public string readFile(string fileName)
        {
            return System.IO.File.ReadAllText(fileName);
        }

        public int complexDictionaryFunc(Dictionary<string, int> dict)
        {
            int sum = 0;
            foreach(var key in dict.Keys)
            {
                Console.WriteLine($"Processing Key {key} with the value: {dict[key]}");
                sum += dict[key];
            }

            return sum;
        }

        public int compute(int val1, int val2)
        {
            int temp = 0;

            temp = val1;
            temp = temp * val2;

            return temp;
        }
    }

    public class SecretOpCaller
    {
        public int computeWrapper(SecretOp secretOpObj)
        {
            int result = secretOpObj.computeInternal();

            Console.WriteLine("computeWrrapper result is " + result.ToString());

            return result;
        }
    }
}
