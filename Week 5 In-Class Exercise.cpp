#include <iostream>
#include <string>

// =========================================================
// For Exercise 2,
// TODO: Define the OOPCourse::Math namespace structure and
//       the internal anonymous namespace here.

// Anonymous namespace (private helper)
namespace
{
    void log_calculation(int result)
    {
        std::cout << "LOG: Calculation performed, result is " << result << "\n";
    }
}

// Nested namespace using C++17 syntax
namespace OOPCourse::Math
{
    int add_and_log(int a, int b)
    {
        int result = a + b;
        log_calculation(result);  // Call anonymous namespace helper
        return result;
    }
}

// =========================================================


// Main program
int main()
{
    // --- Exercise 1: String reversal and largest value ---
    std::cout << "--- Exercise 1: String Reversal ---\n";
    
    // String variables for input
    std::string num_a, num_b;
    
    std::cout << "Enter the first 3-digit number: ";
    std::cin >> num_a;
    
    std::cout << "Enter the second 3-digit number: ";
    std::cin >> num_b;
    
    // Empty strings for reversed results
    std::string reversed_a, reversed_b;
    

    // 1. Reversal with a for-loop
    // Iterate backwards over num_a
    for (int i = num_a.length() - 1; i >= 0; i--)
    {
        reversed_a += num_a[i];
    }
    
    // Iterate backwards over num_b
    for (int i = num_b.length() - 1; i >= 0; i--)
    {
        reversed_b += num_b[i];
    }
    

    // 2. Comparison and Output
    if (reversed_a > reversed_b)
    {
        std::cout << "The largest reversed number is: " << reversed_a << "\n";
    }
    else
    {
        std::cout << "The largest reversed number is: " << reversed_b << "\n";
    }
    
    std::cout << "\n";
    
    
    // --- Exercise 2: Namespaces ---
    std::cout << "--- Exercise 2: Namespaces ---\n";
    
    // Using declaration to bring only add_and_log into scope
    using OOPCourse::Math::add_and_log;

    // Call add_and_log(15, 27) and print the result
    int result = add_and_log(15, 27);
    std::cout << "Result of add_and_log(15, 27): " << result << "\n";

    return 0;
}
