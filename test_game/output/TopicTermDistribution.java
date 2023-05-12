import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.Map;
import java.util.TreeMap;

public class TopicTermDistribution {

	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		ArrayList<String> word = new ArrayList<String>();
		ArrayList<Double> prob = new ArrayList<Double>();
		File folder = new File(args[0] + "/lda_output/words");
		File[] listoffiles= folder.listFiles();
		//System.out.println(Arrays.toString(listoffiles));
		for(int i=0;i<listoffiles.length;i++)
		{
			FileReader fr = new FileReader(listoffiles[i]);
			BufferedReader br = new BufferedReader(fr);
			String line;
			line=br.readLine();
			String[] words=line.split(",");
			line=br.readLine();
			String[] probs=line.split(",");
			Map<Double,String> map = new TreeMap<Double,String>();
			for(int j=0;j<words.length;j++)
			{
				BigDecimal bd=new BigDecimal(probs[j]);
				map.put(bd.doubleValue(),words[j]);
			}
			Iterator<Double> iter = map.keySet().iterator();
			while(iter.hasNext())
			{
				Double key=iter.next();
				prob.add(key);
				//System.out.println("The key is "+key+" value is "+map.get(key));
			}
			for(int j=prob.size();j>prob.size()-10;j--)
			{
				System.out.println("For topic "+(i+1)+" word "+map.get(prob.get(j-1))+ " occurred at probability of "+prob.get(j-1));
			}
			System.out.println(" ");
			System.out.println(" ");
		}
		
	}

}
