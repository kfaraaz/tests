import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.SQLException;
import java.io.BufferedWriter;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Arrays;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.File;
import java.util.ArrayList;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;

public class PgqlResultGenerator {

	private static List<File> searchFiles(File root, String regex) {
		List<File> list = new ArrayList<File>();
		Pattern pattern = Pattern.compile(regex + "$");
		Matcher matcher = null;
		if (root.isFile()) {
			matcher = pattern.matcher(root.getName());
			if (matcher.find()) {
				list.add(root);
				return list;
			}
		} else {
			for (File file : root.listFiles()) {
				if (!file.getName().equals("datasources")) {
					list.addAll(searchFiles(file, regex));
				}
			}
		}
		return list;
	}

	private static String getSqlStatement(String queryFileName)
			throws IOException {
		StringBuilder builder = new StringBuilder();
		BufferedReader reader = new BufferedReader(new FileReader(new File(
				queryFileName)));
		String line = null;
		while ((line = reader.readLine()) != null && !line.trim().isEmpty()) {
			builder.append(line + '\n');
		}
		reader.close();
		String statement = builder.toString().trim();
		if (statement.endsWith(";")) {
			statement = statement.substring(0, statement.length() - 1);
		}
		return statement;
	}

	public static void main(String[] argv) throws SQLException {

		Connection connection = null;
		String jdbcUrl = argv[0];
		String filePath = argv[1];
		Statement stmt = null;

		try {

			Class.forName("org.postgresql.Driver");
			connection = DriverManager.getConnection(jdbcUrl, "postgres",
					"postgres");
			stmt = connection.createStatement();

		} catch (Exception e) {

			System.out.println("Where is your PostgreSQL JDBC Driver? "
					+ "Include in your library path!");
			e.printStackTrace();
			return;

		}

		System.out.println("PostgreSQL JDBC Driver Registered!");
		List<String> listOfFailedQueries = new ArrayList<String>();
		for (File file : searchFiles(new File(filePath), argv[2])) {
			String queryFileName = file.getAbsolutePath();
			System.out.println("Query files executed:"+file.getAbsolutePath());
			ResultSet resultSet = null;
			try {
				String splitResult[]=queryFileName.split("\\.(?=[^\\.]+$)");
				Path newFile = Paths.get(splitResult[0] + argv[3]);

				Files.deleteIfExists(newFile);
				newFile = Files.createFile(newFile);

				resultSet = stmt.executeQuery(getSqlStatement(queryFileName));

				BufferedWriter writer = Files.newBufferedWriter(newFile,
						Charset.defaultCharset());

				int columnCount = resultSet.getMetaData().getColumnCount();
				while (resultSet.next()) {
					StringBuilder builder = new StringBuilder();
					for (int i = 1; i <= columnCount; i++) {
						// builder.append(new String(resultSet.getBytes(i)) +
						// "\t");
						builder.append(resultSet.getObject(i) + "\t");
					}
					String entry = builder.toString().trim();
					writer.append(entry);
					writer.newLine();
				}
				writer.flush();
				System.out.println("Expected file generated:"+splitResult[0]+argv[3]);

			}

			catch (Exception e) {
				listOfFailedQueries.add(queryFileName);
				System.out.println("Query failed with error");
				e.printStackTrace();
			}

			finally{
				if(resultSet!=null)
					resultSet.close();
			}

		}
		if(listOfFailedQueries.size()>0)
		{
			System.out.println("number of queries failed:"+listOfFailedQueries.size());
			for(String failedQuery:listOfFailedQueries)
				System.out.println(failedQuery);
		}
		connection.close();
		stmt.close();

	}

}
