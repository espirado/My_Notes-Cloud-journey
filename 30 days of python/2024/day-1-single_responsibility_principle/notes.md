Theory:
The Single-Responsibility Principle (SRP) states that a class should have only one reason to change, meaning it should have only one job or responsibility. This makes the class more maintainable, easier to refactor, and less prone to bugs as the application grows.

Key benefits of SRP:

Maintainability: Changes in one responsibility do not affect others.
Testability: Easier to write unit tests for a focused, single-responsibility class.
Flexibility and Reusability: Class can be reused in other contexts because it doesn't handle unnecessary concerns.


In this example, we have a Customer class that has three responsibilities: sending an email to the customer, placing an order, and generating an invoice. This violates the SRP because if we need to change any of these responsibilities, we would need to modify the Customer class

Single-responsibility principle (SRP)
Open–closed principle (OCP)
Liskov substitution principle (LSP)
Interface segregation principle (ISP)
Dependency inversion principle (DIP)