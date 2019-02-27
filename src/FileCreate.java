// Pre-requisite before executing this Java class that createsafiles ann writes bytes to them
// export CLASSPATH="`hadoop classpath`:."

import org.apache.hadoop.fs.*;
import org.apache.hadoop.fs.permission.FsPermission;
import org.apache.hadoop.conf.*;
import java.net.URI;
import java.io.*;
import java.util.Random;
import org.apache.hadoop.fs.Path;

public class FileCreate {

  static int entriesPerDir = 400;
  static int numThreads = 8;
  static String srcDir = "/vol1/a1";

  static class CreateThread extends Thread {
    FileSystem fs;
    int myid;

    CreateThread(int id, FileSystem mfs) {
      this.myid = id;
      this.fs = mfs;
    }

    // Create files 
    public void doCreates() {
      try {
        byte[] data = new byte[1024 * 1024];
        for(int i = 0; i>=0; i++){
                String mySrcDir = srcDir + "/" + i + "/" + myid;
                fs.mkdirs(new Path(mySrcDir));
                for (int j = 0; j < entriesPerDir; ++j) {
                        String fname = mySrcDir + "/file" + j;
                        FSDataOutputStream fin = fs.create(new Path(fname));
                        fin.write(data, 0, data.length);
                        fin.close();
                }
        }
      } catch (Exception e) {
        System.err.println(e);
      }
    }

    public void run() {
        doCreates();
    }
  }

public static void main(String args[]) throws Exception {
    String uri = "maprfs:///";
    Configuration conf = new Configuration();
    conf.set("fs.default.name", uri);
    conf.set("fs.maprfs.impl", "com.mapr.fs.MapRFileSystem");

    FileSystem fs = FileSystem.get(URI.create(uri), conf);
    fs.mkdirs(new Path(srcDir));

    System.out.println("Creating files and writing bytes to them.");
    Thread[] tid = new Thread[numThreads];
    for (int i = 0; i < numThreads; ++i) {
      tid[i] = new CreateThread(i, fs);
      tid[i].start();
    }
    for (int i = 0; i < numThreads; ++i)
      tid[i].join();

  }
}
