/*
 Add meg az 1. gyümölcsöt: alma
Add meg az 2. gyümölcsöt: barack
Add meg az 3. gyümölcsöt: narancs
Add meg az 4. gyümölcsöt: szilva
Add meg az 5. gyümölcsöt: eper
 */
List<string> gyumolcsok = new();


for (int i = 1; i <= 5; i++)
{
    Console.Write($"Add meg az {i}. gyümölcsöt: ");
    string gyumolcs = Console.ReadLine();
    gyumolcsok.Add(gyumolcs);
}

gyumolcsok.Sort();

foreach (string gyumi in gyumolcsok)
{
    Console.WriteLine(gyumi);
}