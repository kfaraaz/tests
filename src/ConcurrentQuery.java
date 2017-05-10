/*
 * Run this export command before running this concurrency test.
 * Also ensure you are using the correct Drill version in the path below
 *
export CLASSPATH=".:/etc/drill/conf:/opt/mapr/drill/drill-1.11.0/jars/*:/opt/mapr/drill/drill-1.11.0/jars/ext/*:/opt/mapr/drill/drill-1.11.0/jars/3rdparty/*:/opt/mapr/drill/drill-1.11.0/jars/classb/*:/opt/mapr/drill/drill-1.11.0/jars/jdbc-driver/*:commons-exec-1.3.jar"
 * */

import org.apache.log4j.Logger;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.Types;
import java.sql.*;
import java.io.*;
import java.util.Scanner;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ConcurrentQuery implements Runnable {
 
    Connection conn = null;

    ConcurrentQuery(Connection conn) {
        this.conn = conn;
    }
 
    public void run() {
        try {
            selectData();
        } catch (Exception e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        } 
    }
  
    // Get SQL query from script file. 
    public String getSQLQuery() {
        String sql_query = new String();
        try {
                Scanner scanner = new Scanner(new File("/root/concur/testSQL.q")).useDelimiter(";");
                while(scanner.hasNext()) {
                    sql_query = scanner.next();
                }
        } catch (Exception e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        } finally {
            return sql_query;
        }
    }
 
    // SELECT data 
    public void selectData() {
        try {
                executeQuery(getSQLQuery());
        } catch(Exception e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        }
    }
 
    // Execute Query
    public void executeQuery(String query) {
        try {
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(query);
                
                while(rs.next()) {
                    // do Nothing!!!  
                }
            if (rs != null)
                rs.close();
            stmt.close();
            //conn.close();                         
        } catch (Exception e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        }
    }
    
    public static void main(String s[]) throws Exception {
        
        final String URL_STRING = "jdbc:drill:schema=dfs.tpcds_sf1_parquet_views;drillbit=centos-01";
        Class.forName("org.apache.drill.jdbc.Driver").newInstance();
        Connection conn = DriverManager.getConnection(URL_STRING,"test","test");
        
        // newFixedThreadPool : Creates a thread pool that reuses a fixed number of threads operating off a shared unbounded queue.
        ExecutorService executor = Executors.newFixedThreadPool(8);
        try {
            for (int i = 1; i <= 8; i++) {
                executor.submit(new ConcurrentQuery(conn));
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        } 
    }
}
