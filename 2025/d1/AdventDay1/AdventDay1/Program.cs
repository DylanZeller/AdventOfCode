// See https://aka.ms/new-console-template for more information

namespace AdventDay1;

internal static class Program
{
    public static void Main(string[] args)
    {
        var inputLines = File.ReadAllLines("input.txt");
        var startNum = 50;
        var currentNum = startNum;
        var timesCrossed = 0;
        var timesHit = 0;

        foreach (var line in inputLines)
        {
            var isZero = currentNum == 0;
            var direction = line[0] == 'R' ? 1 : -1;
            var num = int.Parse(line[1..]);
            timesCrossed += num / 100;
            currentNum += direction * (num % 100);
            if (!isZero && currentNum is < 0 or > 100) timesCrossed++;
            currentNum = (currentNum + 100) % 100;
            if (currentNum == 0) timesHit++;
        }
        Console.WriteLine($"Times Hit: {timesHit}");
        Console.WriteLine($"Times Crossed: {timesCrossed}");
        Console.WriteLine($"Times Hit + Times Crossed: {timesHit + timesCrossed}");
    }
}