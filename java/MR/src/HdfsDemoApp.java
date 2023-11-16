import java.io.IOException;
 
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;

public class HdfsDemoApp {
    public static void main(String[] args) {
        try {
 
            //创建Configuration对象
            Configuration conf = new Configuration();
            //设置Hadoop的dfs客户端使用hostname访问datanode
            //conf.set("dfs.client.use.datanode.hostname", "true");
            conf.set("fs.defaultFS", "hdfs://localhost:8020");
            FileSystem fs = FileSystem.get(conf);
            // 打开hdfs上的文件并读取输出
            Path hello = new Path("/data/wordcount/input.txt");
            FSDataInputStream ins = fs.open(hello);
            int ch = ins.read();
            while (ch != -1) {
                System.out.print((char) ch);
                ch = ins.read();
            }
            System.out.println();
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    }
}
