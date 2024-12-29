public class abstractexample {

    public static void main(String[] args) {
        // Now you can directly instantiate Circle without an instance of AbstractExample
        Circle circle = new Circle(5);  // Passing radius to constructor
        System.out.println("Area of circle: " + circle.area());
    }

    // Making Circle a static class so it can be used without an instance of AbstractExamples
    public static class Circle extends Shape {
        int radius;
        
        // Constructor to initialize radius
        public Circle(int radius) {
            this.radius = radius;
        }
        
        // Implementing the abstract area method
        @Override
        int area() {
            return (int)(Math.PI * radius * radius);  // Area of a circle formula: πr²|| math.pi return a double and return type is int so do explicit typecasting
        }
    }
    public static class recantgle extends Shape{
        int l;
        int b;

        public recantgle(int l,int b){
            this.b=b;
            this.l=l;

        }
        @Override
        int area(){
            return (l*b);

        }
    }
}

// Abstract class Shape
abstract class Shape {
    abstract int area();  // Abstract method to be implemented by subclasses
}
