Dictionary<int, string> szotar = new() { [21] = "Radics Roland" , [69] = "Fodor Benedek"};

szotar[55] = "Kis Pista";

Console.WriteLine(szotar[55]);


foreach (KeyValuePair<int, string> i in szotar)
{
    Console.WriteLine($"A kulcs: {i.Key}, az érték: {i.Value}");
}