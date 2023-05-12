import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class TopicProbability {

	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		FileReader fr =new FileReader(args[0] + "/lda_output/part-m-00000");
		BufferedReader br = new BufferedReader(fr);
		String line,document,topicprob;
		br.readLine();
		while(( line=br.readLine())!=null)
		{
			if(!(line.equals("")))
			{
			document=line.split("\t")[0];
			topicprob=line.split("\t")[1];
			String[] topic=topicprob.split(",");
			for(int i=0;i<topic.length;i++)
			{
				System.out.println("Probability of Topic "+(i+1)+" appearing in document "+document+ " is "+topic[i]);
			}
			System.out.println("");
			System.out.println("");
			}
		}
		fr.close();
		br.close();
	}
	

}
