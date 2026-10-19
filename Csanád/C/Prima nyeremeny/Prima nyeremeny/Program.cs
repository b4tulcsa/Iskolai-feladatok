int x;
Console.Write("Add meg a csoki gyartasi sorszamat: ");
x = int.Parse(Console.ReadLine());

int osztok = 0;

for (int i = 1; i <= x; i++)
{
    if (x % i == 0)
    {
        osztok++;
    }
}

if (osztok == 2)
{
    Console.WriteLine("Gratulalok, nyertel!");
}
else
{
    Console.WriteLine("Sajnos nem nyert!");
}