/*
 Add meg az 1. tanuló jegyét: 5
Add meg az 2. tanuló jegyét: 4
Add meg az 3. tanuló jegyét: 3
Add meg az 4. tanuló jegyét: 2
Add meg az 5. tanuló jegyét: 4
Add meg az 6. tanuló jegyét: 3
Add meg az 7. tanuló jegyét: 5
Add meg az 8. tanuló jegyét: 2
Add meg az 9. tanuló jegyét: 1
Add meg az 10. tanuló jegyét: 5
Példa kimenet

Jegyek: [5, 4, 3, 2, 4, 3, 5, 2, 1, 5]
Az osztály átlaga: 3.4
 */
int legnagyobb;

float ossz = 0;
List<int> jegyek = new();

for (int i = 1; i <= 10; i++)
{
    Console.Write($"Add meg az {i}. tanuló jegyét: ");
    int jegy = int.Parse(Console.ReadLine());
    while (jegy < 1 || jegy > 5)
    {
        Console.Write($"Add meg az {i}. tanuló jegyét újra (1 és 5 között): ");
        jegy = int.Parse(Console.ReadLine());
    }
    jegyek.Add(jegy);
    ossz += jegy;
}
int hanyadik = 0;
Console.Write("jegyek: [");
foreach (int i in jegyek)
{
    hanyadik += 1;
    if (hanyadik == jegyek.Count())
    {
        Console.Write($"{i}");
    }
    else
    {
        Console.Write($"{i}, ");
    }
}
Console.WriteLine("]");

jegyek.Sort();
hanyadik = 0;
Console.Write("sortolva jegyek: [");
foreach (int i in jegyek)
{
    hanyadik += 1;
    if (hanyadik == jegyek.Count())
    {
        Console.Write($"{i}");
    }
    else
    {
        Console.Write($"{i}, ");
    }
}
Console.WriteLine("]");

Console.WriteLine($"Az osztály legnagyobb jegye: {jegyek[0]}");
Console.WriteLine($"Az osztály legnagyobb jegye: {jegyek[9]}");

Console.WriteLine($"Az osztály átlaga: {ossz / 10}"); 
