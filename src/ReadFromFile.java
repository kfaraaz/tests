import java.io.*;
import java.util.*;

public class ReadFromFile {

    // Brute force method to find the inversions in an array.
    static long getInvCount(int arr[], int n)
    {
        long inv_count = 0;
        for (int i = 0; i < n ; i++) {
            for (int j = i+1; j < n; j++) {
                if (arr[i] > arr[j]) {
                    inv_count++;
                }
            }
        }
        return inv_count;
    }

    public static void main ( String s[] ) throws Exception {
        int arr[] = new int[100001];
        Scanner scr = new Scanner(new FileInputStream("arr_inv_data.txt")).useDelimiter("\n");
        while ( scr.hasNext() ) {
            int idxVal = Integer.parseInt(scr.next());
            arr[idxVal] = idxVal;
        } scr.close();
        System.out.println(ReadFromFile.getInvCount(arr,100000));

    }

}
