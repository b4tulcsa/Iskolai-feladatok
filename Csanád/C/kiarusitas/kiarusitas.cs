/*
 Add meg a termékek darabszámát: 5

Add meg az 1. termék árát: 10000
Add meg az 2. termék árát: 20000
Add meg az 3. termék árát: 30000
Add meg az 4. termék árát: 40000
Add meg az 5. termék árát: 50000

Eredeti árak: [10000, 20000, 30000, 40000, 50000]
Az akciós árak: [7000, 14000, 21000, 28000, 35000]

Az akciós átlagár: 21000
 */

Console.Write("Add meg a termékek darabszámát: ");
int darab = int.Parse(Console.ReadLine());

List<int> eredeti = new();
List<float> modositott = new();

for (int i = 1; i <= darab; i++)
{
    Console.Write($"Add meg a {i}. termék árár: ");
    int ar = int.Parse(Console.ReadLine());
    eredeti.Add(ar);
}

int hanyadik = 0;
Console.Write("Eredeti árak: [");
foreach (int i in eredeti)
{
    float mod = (float)(i * 0.7f);
    modositott.Add(mod);
    hanyadik += 1;
    if (hanyadik == eredeti.Count())
    {
        Console.Write($"{i}");
    }
    else
    {
        Console.Write($"{i}, ");
    }
}
Console.WriteLine("]");

hanyadik = 0;
float ossz = 0;
Console.Write("Modositott árak: [");
foreach (float i in modositott)
{
    ossz += i;
    hanyadik += 1;
    if (hanyadik == modositott.Count())
    {
        Console.Write($"{i}");
    }
    else
    {
        Console.Write($"{i}, ");
    }
}
Console.WriteLine("]");

Console.WriteLine("Az akciós átlagár: " + ossz / modositott.Count());