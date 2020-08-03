package org.myorg;

// Basic Java file IO 
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.net.URI;

// Java classes for working with sets
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

// Regular expression utility
import java.util.regex.Pattern;

// File I/O
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

// Mapper parent class and the Configuration class
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.mapreduce.Mapper;

// Wrappers for values
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.util.StringUtils;

// Configurable counters
import org.apache.hadoop.mapreduce.Counters;
import org.apache.hadoop.mapreduce.Counter;


public class Map extends Mapper<LongWritable, Text, Text, IntWritable> {

	// Enumeration used for custom counters
	enum Gauge{POSITIVE, NEGATIVE}
	
	// IntWritable object set to the value 1 as counting increment.
	private final static IntWritable one = new IntWritable(1);
	
	// Reusable variable for each word instance in the incoming data.
	private Text word = new Text();
	
	// Store case sensitivity setting from command line.
	private boolean caseSensitive = false;

	private String input;
	
	// HashSets for filter terms.
	private Set<String> patternsToSkip = new HashSet<String>();
	private Set<String> goodWords = new HashSet<String>();
	private Set<String> badWords = new HashSet<String>();
	
	// Word boundary defined as whitespace-characters-word boundary-whitespace 
	private static final 
			Pattern WORD_BOUNDARY = Pattern.compile("\\s*\\b\\s*");
    
	protected void 
		setup(Mapper<LongWritable, Text, Text, IntWritable>.Context context)
		throws IOException, InterruptedException
	{
		// If the input for this mapper is a file reference, read from the
		// referenced file. Otherwise, read from the InputSplit itself.
		if (context.getInputSplit() instanceof FileSplit)
		{
			this.input = 
					((FileSplit) context.getInputSplit()).getPath().toString();
		} else {
			this.input = context.getInputSplit().toString();
		}
		
		// Check for and set boolean runtime variables. 
		Configuration config = context.getConfiguration();
		
		this.caseSensitive = 
				config.getBoolean("mrmanager.case.sensitive", false);
		
		URI[] localPaths = context.getCacheFiles();
		
		int uriCount = 0;
		
		if (config.getBoolean("mrmanager.skip.patterns", false))
		{
        parseSkipFile(localPaths[uriCount++]);
		}
		parsePositive(localPaths[uriCount++]);
		parseNegative(localPaths[uriCount]);
	}
	
	// Parse the values to skip when reading input.
	private void parseSkipFile(URI patternsURI) {
		try {
			BufferedReader fis = new BufferedReader(new FileReader
					(new File(patternsURI.getPath()).getName()));
			String pattern;
			while ((pattern = fis.readLine()) != null) {
				patternsToSkip.add(pattern);
			}
		} catch (IOException ioe) {
			System.err.println("Caught exception parsing cached file '"
				+ patternsURI + "' : " + StringUtils.stringifyException(ioe));
		}
	}

	// Parse the positive words to match and capture during Map phase.
	private void parsePositive(URI goodWordsUri) {
		try {
			BufferedReader fis = new BufferedReader(new FileReader(
					new File(goodWordsUri.getPath()).getName()));
			String goodWord;
			while ((goodWord = fis.readLine()) != null) {
				goodWords.add(goodWord);
			}
		} catch (IOException ioe) {
			System.err.println("Caught exception parsing cached file '"
					+ goodWords + "' : " + StringUtils.stringifyException(ioe));
		}
	}
  
  // Parse the negative words to match and capture during Reduce phase.
	private void parseNegative(URI badWordsUri) {
		try {
			BufferedReader fis = new BufferedReader(new FileReader(
					new File(badWordsUri.getPath()).getName()));
			String badWord;
			while ((badWord = fis.readLine()) != null) {
				badWords.add(badWord);
			}
		} catch (IOException ioe) {
			System.err.println("Caught exception while parsing cached file '"
					+ badWords + "' : " + StringUtils.stringifyException(ioe));
		}
	}
  	
	public void map(LongWritable offset, Text lineText, Context context)
        throws IOException, InterruptedException {
					
		String line = lineText.toString();
		
		// If caseSensitive is false, convert everything to lower case.
		if (!caseSensitive) {
			line = line.toLowerCase();
		}
		
		// Store each the current word in the queue for processing.
		Text currentWord = new Text();

		for (String word : WORD_BOUNDARY.split(line))
		{
			if (word.isEmpty() || patternsToSkip.contains(word)) {
            continue;
      }
      // Count instances of each (non-skipped) word.
      currentWord = new Text(word);
			context.write(currentWord,one);         

			// Filter and count "good" words.
			if (goodWords.contains(word)) {
				context.getCounter(Gauge.POSITIVE).increment(1);
			}

			// Filter and count "bad" words.
			if (badWords.contains(word)) {
				context.getCounter(Gauge.NEGATIVE).increment(1);
			}
		}
	}
}
