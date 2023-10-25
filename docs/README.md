# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah

## Perimeter
- Circle: C = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

### Table of formules
|           | Circle | Rectangle | Square | Triangle |
|   :---:   |  :---: |   :---:   |  :---: |  :---:   |
| Area      | πR² | ab | a² | ah |
| Perimeter | 2πR | 2a + 2b | 4a | a + b + c |

# Functions description
## Area
- get_circle_area(r) - returns an area of given circle  
    get_circle_area(5) -> 78.53981633974483
- get_rectangle_area(a, b) - returns an area of given rectangle  
    get_rectangle_area(5, 6) -> 30
- get_square_area(a) - returns an area of given square  
    get_square_area(5) -> 25
- get_triangle_area(a, h) - returns an area of given triangle  
    get_triangle_area(5, 10) -> 25.0

## Perimeter
- get_circle_perimeter(r) - returns a circumference of given circle  
    get_circle_perimeter(5) -> 31.41592653589793
- get_rectangle_perimeter(a, b) - returns a perimeter of given rectangle  
    get_rectangle_perimeter(5, 6) -> 22
- get_square_perimeter(a) - returns a perimeter of given square  
    get_square_perimeter(5) -> 20
- get_triangle_perimeter(a, h) - returns a perimeter of given triangle  
    get_triangle_perimeter(5, 10, 15) -> 30

# Commit history
- v.0.0.3 - added tests for all functions
- v.0.0.2 - updated documentation
- v.0.0.1 - added rectangle and triangle math functions