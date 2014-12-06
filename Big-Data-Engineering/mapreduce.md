
It is able to run map reduce job on EMR both in streaming and java.

Here is a tutorial about how to write map-reduce program and how to deploy a java program on EMR.
* [MapReduce Tutorial](http://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)
* [How to Run Elastic MapReduce Hadoop Job Using Custom Jar - Amazon EMR Tutorial](http://muhammadkhojaye.blogspot.com/2012/04/how-to-run-amazon-elastic-mapreduce-job.html)

Compute distinct value by map reduce is intuitive, you can implement it by following the pseudocode below.
```
	map(key, value):
    	emit value, null
    reduce(key, values):
        emit key
    # A combiner should be put in use, 
    # if there are a lot of duplicate produced
    # by map function, which will save a lot communication
    # cost. 
    # Here, the combiner could be just the same as reduce fucntion
```
The map-reduce job will generate some number of output file on EMR based on the reducer size. Outout in one file should be of the format(in case of streaming):
```1
a_c_c_b_c_g None
c_g_i_a_a_g None
l_i_f_h_b_a None
```
Then you should download all the output file, and linear scan on them to count how many lines added up from them, which is the distinct value.

You can first test on the some dataset(data10000), which has 9925 distinct value.

**Note** that Amazon provides different tools access EMR and S3 storage service.[To see](http://aws.amazon.com/cli/)

