/*
//laci
for (int i = 1; i <= 100; i++)
{
    Console.WriteLine("Laci" + " " + i);
}


//100-0
for (int i = 100; i >= 0; i -= 1)
{
    Console.WriteLine(i);
}

//laci extra
Console.Write("Hányszor legyen a név: ");
int szam = int.Parse(Console.ReadLine());
Console.Write("Mi legyen a név: ");
string nev = Console.ReadLine();
Console.WriteLine("");
for (int i = 1; i <= szam; i++)
{
    Console.WriteLine(nev + " " + i);
}


//páros számok
int ossz = 0;

Console.Write("Az intervallum also vegpontja: ");
int also = int.Parse(Console.ReadLine());

Console.Write("Az intervallum felso vegpontja: ");
int felso = int.Parse(Console.ReadLine());

for (int i = also; i <= felso; i++)
{
    if (i % 2 == 0)
    {
        ossz += i;
    }
}
Console.WriteLine($"A(z)[{also}; {felso}] intervallumba eso paros szamok osszege: {ossz}");
*/

for (int i = 1; i <= 10; i++)
{
    for (int j = 1; j <= 10; j++)
    {
        Console.Write(i * j+" ");
    }
    Console.WriteLine("");
}