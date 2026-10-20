Dictionary<string, string> dict = new();

for (int i = 0; i < 3; i++)
{
    Console.Write("Kérem az auto modelljét: ");
    string auto = Console.ReadLine();

    Console.Write("Kérem az auto rendszámát (3 betu 3 szam): ");
    string rendszam = Console.ReadLine();

    Console.WriteLine();

    dict[auto] = rendszam;
}


foreach (KeyValuePair<string,string> i in dict)
{
    Console.WriteLine($"az autó modellje: {i.Key}, a rendszáma: {i.Value}");
    Console.WriteLine();
}