// See https://aka.ms/new-console-template for more information

Console.WriteLine(linear_search([1, 13, 38, 75, 101, 151], 234));

static string linear_search(int[] array, int search_value)
{
    for(int i = 0; i < array.Length; i++)
    {
        if(array[i] == search_value)
            return $"The value: {array[i]} is found at index:{i}";
        else if(array[i] > search_value) break;
    }
    return "The value is not found";
}
