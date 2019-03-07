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

public class JDBCTestQuery {

public static void main(String s[]) throws Exception {

    Connection conn = null;
    PreparedStatement prdstmnt = null;
    try {
        final String URL_STRING = "jdbc:drill:schema=dfs.tmp;drillbit=test-123";
        Class.forName("org.apache.drill.jdbc.Driver").newInstance();
        conn = DriverManager.getConnection(URL_STRING,"test","test");
        prdstmnt = conn.prepareStatement("SELECT * FROM cp.`employee.json`");
        prdstmnt.executeQuery();
        prdstmnt.close();
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
}
