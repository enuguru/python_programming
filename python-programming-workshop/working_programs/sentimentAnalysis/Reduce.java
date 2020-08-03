package org.myorg;

import java.io.IOException;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;

public class Reduce extends 
	Reducer<Text, IntWritable, Text, IntWritable> {
@Override
	public void reduce(Text word, Iterable<IntWritable> instances, Context context)
			throws IOException, InterruptedException
	{
		int sum = 0;

		// Sum up the instances of the current word.
		for (IntWritable instance : instances) {
			sum += instance.get();
		}
		
		// Write the word and count to output.
		context.write(word, new IntWritable(sum));
	}
}
