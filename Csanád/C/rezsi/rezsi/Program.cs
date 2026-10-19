/*
 Január: 8000
Február: 7000
Március: 6000
Április: 5000
Május: 4000
Június: 3000
Július: 2000
Augusztus: 1000
Szeptember: 2000
Október: 3000
November: 4000
December: 5000
Példa kimenet

Az éves rezsi költség: 50000
Átlagos havi rezsi költség: 4166.666666666667
A maximum havi rezsi költség: 8000
A minimum havi rezsi költség: 1000
 */

List<string> honapok = new() { "Január", "Február", "Március", "Április", "Május", "Június", "Július", "Augusztus", "Szeptember", "Október", "November", "December" };
List<int> honapkolt = new();

float eves = 0;

for (int i = 0; i < 12; i++)
{
    Console.Write(honapok[i]+": ");
    int honap = int.Parse(Console.ReadLine());
    eves += honap;
    honapkolt.Add(honap);
}

Console.WriteLine($"Az éves rezsi költség: {eves}");
Console.WriteLine($"Átlagos havi rezsi költség: {eves/honapok.Count()}");
Console.WriteLine($"A maximum havi rezsi költség: {honapkolt.Max()}");
Console.WriteLine($"A minimum havi rezsi költség: {honapkolt.Min()}");