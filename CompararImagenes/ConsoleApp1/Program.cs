using System;
using System.Drawing;
using AForge.Imaging;


namespace ConsoleApp1
{
    internal class Program
    {

        static void Main(string[] args)
        {
            //string ruta = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);

            Bitmap image2 = new Bitmap("C:\\Users\\User\\Desktop\\.jpg");
            Bitmap image1 = new Bitmap("C:\\Users\\User\\Desktop\\.jpg");

            ExhaustiveTemplateMatching tm = new ExhaustiveTemplateMatching(0);

            TemplateMatch[] matchings = tm.ProcessImage(image1, image2);
           
            if (matchings[0].Similarity > 0.9988f)
            {
                // Son Similares
                Console.WriteLine("Son Similares");
            }

            else
            {
                //No son similares
                Console.WriteLine("No Son iguales");
            }
            Console.ReadKey();

        }
    }
}

