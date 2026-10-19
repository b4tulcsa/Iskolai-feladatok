Console.Write("Hallgato jegyeinek szama: ");
int darab = int.Parse(Console.ReadLine());
float ossz = 0;


for (int i = 1; i <= darab; i++)
{
    Console.Write($"{i}.jegy:");
    int jegy = int.Parse(Console.ReadLine());
    if (jegy >= 1 && jegy <= 5)
    {
        ossz += jegy;
    }
    else
    {
        Console.WriteLine("Hibás jegy");
        break;
    }
}

if (ossz / darab >= 4.0)
{
    Console.WriteLine("A jegyek atlaga: " + ossz / darab);
    Console.WriteLine("A hallgato osztondijra jogosult!");
}
else
{
    Console.WriteLine("A jegyek atlaga: " + ossz / darab);
    Console.WriteLine("A hallgato nem jogosult az osztondijra!");
}

/*
Hallgato jegyeinek szama: 5

1.jegy: 3
2.jegy: 5
3.jegy: 5
4.jegy: 4
5.jegy: 5

A jegyek atlaga: 4.4
A hallgato osztondijra jogosult!
*/
