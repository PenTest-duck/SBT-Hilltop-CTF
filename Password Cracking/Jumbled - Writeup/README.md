# Jumbled - Writeup

This password cracking challenge requires the use of a rule-based attack on the given SHA1 hash to recover the password.

The challenge prompt lifted some load off our shoulders by telling us that the password is in rockyou.txt, but has created a headache by setting some criteria the password had to follow.
Since the criteria includes the addition of 2 hex digits, creating a new wordlist containing all 256 possible variations of each word is impossible, as the size of the wordlist will become larger than 35GB.

A method that modifies passwords before they are tested against the hash is by performing a rule-based attack.
Multiple password cracking tools support this function but in our case, we will use Hashcat.

Before performing a rule-based attack using Hashcat, a rules file must be created, containing all of the modifications to the original word from the wordlist.
Therefore, the rules file includes 256 rules (for each hex digit combination) and a simple Python script can be used to generate all of the rules.

```
line = "$@ sa4 sb6 se3 sg9 si1 so0 ss5 st7 sz2"
for i in range(16):
  prefix = "c ^" + str(hex(i)[2:])
  for j in range(16):
    print(prefix, "$" + str(hex(j)[2:]), line)
```

Let's take a look at a single rule to see how it has been constructed.

`c ^3 $c $@ sa4 sb6 se3 sg9 si1 so0 ss5 st7 sz2`

  - The *c* instructs Hashcat to capitalise the first letter of the word.
  - The *^3* instructs Hashcat to prepend a '3' at the beginning of the word.
  - The *$c* instructs Hashcat to append a 'c' at the end of the word.
  - The *sAB* replaces A with B (e.g. sa4 => replace a with 4).
  
Once the rules file has been created, Hashcat can be used to crack the hash.
*Note that you may need to supply the --force option if Hashcat doesn't start.*

`hashcat -m 100 -a 0 -r rules -o out hash jumbled_wordlist.txt && cat out`

The *-m 100* specifies that the hash is SHA1, the *-a 0* specifies a dictionary attack, *-r rules* makes Hashcat use the rules in the 'rules' file and the *-o out* saves the result to an 'out' file, which is printed at the end.

Hashcat should take up to about a minute (time depends on the device it is running on) to crack the hash and return the password.

Flag: HilltopCTF{dCh47rum56@}
