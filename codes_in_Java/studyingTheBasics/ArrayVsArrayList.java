import java.util.ArrayList;
import java.util.Arrays;

public class ArrayVsArrayList {

    //  [Array VS ArrayList]

    public static void main(String args[]) {

        // Array:

        // Arrays must have a size and their size is FIXED (will never expand or get smaller)
        // Arrays can store 2 data types...
        // - Primitive types (int, long, boolean, char...)
        // AND
        // - Objects (Integer, Long... or any object created by a custom class)
        
        String[] foodsArray1 = new String[3]; // Capacity of "3"

        String[] foodsArray2 = {"Potato", "Tomato", "Cucumber", "Garlic"}; // Implied capaciy of "4"

        // acessing values from it...
        System.out.println(foodsArray2[1]);

        // getting its size...
        System.out.println(foodsArray2.length);

        // adding elemnts to the end of it...
        System.out.println("CANNOT ADD STUFF IN Arrays BECAUSE SIZE IS FIXED AND CANNOT CHANGE");

        // setting elemnts...
        foodsArray2[0] = "Onion";
        System.out.println(foodsArray2[0]);

        // removing elemnts...
        System.out.println("CANNOT REMOVE STUFF IN Arrays BECAUSE SIZE IS FIXED AND CANNOT CHANGE");

        // printing the entire array...
        System.out.println(foodsArray2); // Just print the memory adress!

        // --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
        System.out.println("\n");
        // --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

        // ArrayList:

        // ArrayLists do not have a fixed sizer. They dynamically expand or contract their size.
        // Arrays can store ONLY 1 data type...
        // - Objects (Integer, Long... or any object created by a custom class)


        ArrayList<String> foodsArrayList1 = new ArrayList<>();

        ArrayList<String> foodsArrayList2 = new ArrayList<>(Arrays.asList("Potato", "Tomato", "Cucumber", "Garlic"));

        // acessing values from it...
        System.out.println(foodsArrayList2.get(1));

        // getting its size...
        System.out.println(foodsArrayList2.size());

        // adding elemnts to the end of it...
        foodsArrayList2.add("Banana");
        System.out.println(foodsArrayList2.get(4));

        // setting elemnts...
        foodsArrayList2.set(4, "Pineapple");
        System.out.println(foodsArrayList2.get(4));

        // removing elemnts...
        foodsArrayList2.remove(0);
        System.out.println(foodsArrayList2.get(0));

        // printing the entire array...
        System.out.println(foodsArrayList2); // Print every elemnt like a python list!

    }
}
