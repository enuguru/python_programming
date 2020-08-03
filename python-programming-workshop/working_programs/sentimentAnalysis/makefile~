run: clean makedir shake poetry copy_files compile_MrManager
	hadoop jar complete.jar org.myorg.MrManager /user/cloudera/sentiment/input /user/cloudera/sentiment/output -skip stop-words.txt -pos pos-words.txt -neg neg-words.txt

# Run the application without the works of Shakespeare as input.
run_no_shake: clean makedir poetry copy_files compile_MrManager
	hadoop jar complete.jar org.myorg.MrManager /user/cloudera/sentiment/input /user/cloudera/sentiment/output -skip stop-words.txt -pos pos-words.txt -neg neg-words.txt

# Run the application to count all elements, including short words and punctuation.
run_no_skipwords: clean makedir shake poetry copy_files compile_MrManager
	hadoop jar complete.jar org.myorg.MrManager /user/cloudera/sentiment/input /user/cloudera/sentiment/output -pos pos-words.txt -neg neg-words.txt

# Run the application without case sensitivity.
run_no_case: clean makedir shake poetry  copy_files compile_MrManager
	hadoop jar complete.jar org.myorg.MrManager /user/cloudera/sentiment/input /user/cloudera/sentiment/output -no_case -skip stop-words.txt -pos pos-words.txt -neg neg-words.txt

# Create the input directory.
makedir:
	hadoop fs -mkdir /user/cloudera/sentiment 
	hadoop fs -mkdir /user/cloudera/sentiment/input

# Copy meta information files to the cluster.
copy_files:
	hadoop fs -copyFromLocal stop-words.txt .
	hadoop fs -copyFromLocal pos-words.txt .
	hadoop fs -copyFromLocal neg-words.txt .

# Compile the Map class.
compile_map: Map.java
	mkdir -p build/org/myorg/
	javac -cp /usr/lib/hadoop/*:/usr/lib/hadoop-mapreduce/* Map.java -d build -Xlint

# Compile the Reduce class.
compile_reduce: Reduce.java
	javac -cp /usr/lib/hadoop/*:/usr/lib/hadoop-mapreduce/* Reduce.java -d build -Xlint

# Compile the application. The interim build lets MrManager find its dependencies. 
compile_MrManager: MrManager.java
	mkdir -p build/org/myorg/
	javac -cp /usr/lib/hadoop/*:/usr/lib/hadoop-mapreduce/* Map.java -d build -Xlint
	javac -cp /usr/lib/hadoop/*:/usr/lib/hadoop-mapreduce/* Reduce.java -d build -Xlint
	jar -cvf mapreduce.jar -C build/ .
	javac -cp /usr/lib/hadoop/*:/usr/lib/hadoop-mapreduce/*:./mapreduce.jar MrManager.java -d build -Xlint
	jar -cvf complete.jar -C build/ .
	rm mapreduce.jar
	
# Commands for parcel-based compilation.
#
# compile_map: Map.java
#	mkdir -p build/org/myorg/
#	javac -cp /opt/cloudera/parcels/CDH/lib/hadoop/*:/opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/* Map.java -d build -Xlint

#compile_reduce: Reduce.java
#	javac -cp /opt/cloudera/parcels/CDH/lib/hadoop/*:/opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/* Reduce.java -d build -Xlint

#compile_MrManager: MrManager.java
#	mkdir -p build/org/myorg/
#	javac -cp /opt/cloudera/parcels/CDH/lib/hadoop/*:/opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/* Map.java -d build -Xlint
#	javac -cp /opt/cloudera/parcels/CDH/lib/hadoop/*:/opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/* Reduce.java -d build -Xlint
#	jar -cvf mapreduce.jar -C build/ .
#	javac -cp /opt/cloudera/parcels/CDH/lib/hadoop/*:/opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/*:./mapreduce.jar MrManager.java -d build -Xlint
#	jar -cvf complete.jar -C build/ .

# Delete the local and remote files created by the application.
clean:
	rm -rf build complete.jar mapreduce.jar
	hadoop fs -rm -f -r /user/cloudera/sentiment/
	hadoop fs -rm -f stop-words.txt pos-words.txt neg-words.txt	

# Create and upload small data files.
data:
	echo "Hadoop is an elephant" > file0
	echo "Hadoop is as yellow as can be" > file1
	echo "Oh what a yellow fellow is Hadoop" > file2
	hadoop fs -put file* /user/cloudera/sentiment/input
	rm file*

# Create and upload three short poems as input.
poetry: 
	echo -e "Hadoop is the Elephant King! \\nA yellow and elegant thing.\\nHe never forgets\\nUseful data, or lets\\nAn extraneous element cling! "> HadoopPoem0.txt
	echo -e "A wonderful king is Hadoop.\\nThe elephant plays well with Sqoop.\\nBut what helps him to thrive\\nAre Impala, and Hive,\\nAnd HDFS in the group." > HadoopPoem1.txt
	echo -e "Hadoop is an elegant fellow.\\nAn elephant gentle and mellow.\\nHe never gets mad,\\nOr does anything bad,\\nBecause, at his core, he is yellow." > HadoopPoem2.txt
	hadoop fs -put HadoopP* /user/cloudera/sentiment/input
	rm HadoopPoem*

# Upload the complete works of Shakespeare as input.
shake:
	hadoop fs -put shakespeare/* /user/cloudera/sentiment/input

# Write the results to the console.
showResult:
	hadoop fs -cat /user/cloudera/sentiment/output/*

# Create a list of stop words, send it to HDFS, delete the local copy.
stopwords:
	hadoop fs -rm -f user/cloudera/sentiment/stop-words.txt
	echo -e "a\\n\\nan\\nand\\nbut\\nis\\nor\\nthe\\nto\\n\\.\\n\\,\\n\\!" >stop-words.txt
	hadoop fs -put stop-words.txt /user/cloudera/sentiment/
	rm stop-words.txt
