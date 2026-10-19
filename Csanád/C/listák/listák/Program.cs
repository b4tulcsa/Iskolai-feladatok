List<string> autok = new();
autok.Add("Suzuki");
autok.Add("nem Suzuki1");
autok.Add("nem Suzuki2");
autok.Add("nem Suzuki3");

Console.WriteLine(autok[1]);

autok.Remove(autok[1]);

Console.WriteLine(autok.Count());
//nem mukodik igy
for (int i = 0;i > autok.Count(); i++)
{
    Console.WriteLine(autok[i]);
}
Console.WriteLine();
//igy igen
foreach (string auto in autok)
{
    Console.WriteLine(auto);
}

List<string> betuk = new() { "B", "A", "E", "C", "D" };

betuk.Sort();

foreach (string betu in betuk)
{
    Console.WriteLine(betu);
}