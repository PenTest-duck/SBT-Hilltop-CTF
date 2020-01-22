# Twin - Writeup

This creativity challenge has more than one solution, depending on how the solver approaches the given task.
This challenge tests the solver's ability to think of a solution, rather than the execution itself.
There were 4400 files, each containing 20 lines of 56 base-64 characters and the solver had to find a pair of identical lines.

After unzipping the .zip file, a possible solution is presented below:

The main aspect that makes the challenge difficult is that the 88000 lines are spread across 4400 different files.
In order to counter this obstacle, we can merge all the lines into a single file, then perform simple sorting to find the duplicate line.

A simple bash one-liner can accomplish this.

` for file in $(ls); do cat $file >> big.txt; done && sort big.txt | uniq -d && rm big.txt `

The for loop concatenates the contents of every file to 'big.txt'.
Then, 'big.txt' is sorted and searched for duplicate lines.
The line containing the flag should be printed.
Then, 'big.txt' is deleted.

The duplicate line should be converted from base-64 to ASCII, then ROT13-ed to give the final flag.

Flag: HilltopCTF{tw1n5_c4n_n3v3r_b3_s3p4r473d}
