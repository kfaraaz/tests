import org.apache.log4j.Logger;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.Types;
import java.sql.*;
import java.io.*;
import java.lang.*;
import java.util.*;
import java.util.Scanner;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class RunQuery implements Runnable {

    Connection conn = null;
    String query = null;

    RunQuery(String query) {
        this.query = query;
    }

    public void run() {
       Connection conn = null;
       PreparedStatement prdstmnt = null;
       try {
               final String URL_STRING = "jdbc:drill:schema=dfs.tmp;auth=MAPRSASL;drillbit=test-9145";
               Class.forName("org.apache.drill.jdbc.Driver").newInstance();
               conn = DriverManager.getConnection(URL_STRING,"test","test");
               prdstmnt = conn.prepareStatement(this.query);
               //prdstmnt.executeUpdate();
               prdstmnt.executeQuery();
               Thread.sleep(60000);
               //prdstmnt.close();
        } catch (Exception e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        } finally {
            if(conn != null)
                try { conn.close(); } catch(SQLException sqlexcpn){ sqlexcpn.printStackTrace(); }
            if(prdstmnt != null)
                try { prdstmnt.close(); } catch(SQLException sqlexcpn){ sqlexcpn.printStackTrace(); }
        }
    }
    
    // read SQL queries from text file
    // and add those queries to an ArrayList
    public static void addQueriesToList(ArrayList<String> list) {
        String sql_query = new String();
        try {
                // File test_queries.sql has a list of SQL queries, one query on each line.
                Scanner scanner = new Scanner(new File("/test/test_queries.sql")).useDelimiter(System.lineSeparator());
                while (scanner.hasNextLine()){
                    list.add(scanner.nextLine());
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        }
    }

    public static void main(String s[]) throws Exception {

        ArrayList<String> list = new ArrayList<String>();
        RunQuery.addQueriesToList(list);

        // newFixedThreadPool : Creates a thread pool that reuses a fixed number of threads operating off a shared unbounded queue.
        ExecutorService executor = Executors.newFixedThreadPool(1);
        try {
            ListIterator<String> lst_itrator = list.listIterator();
            while(lst_itrator.hasNext()) {
                executor.submit(new RunQuery( lst_itrator.next() ));
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        }
    }
}
