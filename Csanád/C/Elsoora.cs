// See https://aka.ms/new-console-template for more information
using System.Text.Json;

Console.WriteLine("Hello, World!");
double ar = double.Parse(Console.ReadLine());

Console.WriteLine("szopd le a faszom");
Console.WriteLine(ar);

var masar = ar * 5;

Console.WriteLine(masar);

masar = masar / 25;

Console.WriteLine(masar);

//for (0; 100; 1)
{
//    Console.WriteLine("Laci");
}

//for (int i = 1; i <= 100; i ++)
{
    Console.WriteLine("Laci");
}

var egyik = Console.ReadLine();
var masik = Console.ReadLine();

var ossze = egyik + masik;

Console.WriteLine(ossze);

//Az alkatresz jelenlegi ara: 17500
//Aremeles(szazalekban): 8.7

//Az alkatresz uj ara: 19022
Console.WriteLine();
Console.Write("Az alkatresz jelenlegi ara: ");
float eredetiar = float.Parse(Console.ReadLine());
Console.Write("Aremeles (szazalekban): ");
float aremeles = float.Parse(Console.ReadLine());
Console.WriteLine();
Console.Write("Az alkatresz uj ara: ");

var ujar = eredetiar + (eredetiar * aremeles / 100);
Console.WriteLine(ujar);



