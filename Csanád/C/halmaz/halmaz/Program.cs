HashSet<int> a = new() { 1, 2, 3, 4, 5 };

HashSet<int> b = new() { 2, 4, 6, 8, 10 };

a.UnionWith(b);

foreach (int i in a)
{
    Console.WriteLine(i);
}

Console.WriteLine();

HashSet<string> halmaz = new() { "A", "B", "C" };

foreach (string tag in halmaz)
{
    Console.WriteLine(tag);
}

//halmaz. -> foreach

foreach (string item in halmaz)
{
    
}

halmaz.Add("");
halmaz.Remove("");
Console.WriteLine(halmaz.Contains(""));

if (halmaz.Contains("") == true)
{
    Console.WriteLine("Benne van!!");
}
else
{
    Console.WriteLine("Nincs benne!!");
}