# Results 20


After looking at the benchmark tests, there seemed to be an optimized window where the  accuracy of the algorithm was
above 90% and the speed was greatly increased.

After rerunning benchmark tests on this window (grid was size 15-25), it is clear that this is where interesting 
information can be learned based off the data. At low ranges of randomization (especially 5), the algorithm has very poor
accuracy, yet high speeds. At higher ranges the accuracy is almost perfect, yet the speed gained is essentially negligible.

It is only once you examine the 20 grids in terms of speed and accuracy that this golden area appears, where
the accuracy is over 95%, yet the speed is anywhere from 5-20x that of the brute force method.

Optimizing for this region is the goal for the project moving forward. 