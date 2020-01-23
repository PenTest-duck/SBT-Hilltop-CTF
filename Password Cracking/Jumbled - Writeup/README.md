# Jumbled - Writeup

This password cracking challenge requires the use of a rule-based attack on the given SHA1 hash to recover the password.

The challenge prompt lifted some load off our shoulders by telling us that the password is in rockyou.txt, but created a headache by setting some criteria the password had to follow.
Since the criteria includes the addition of 2 hex digits, creating a new wordlist containing all 256 possible variations of each word is impossible, as the size of the wordlist will become larger than 35GB.

A method that can be used to modify passwords before they are tested against the hash is by using a rule-based attack.
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

hashcat -m 100 -a 0 -r rules -o out hash jumbled_wordlist.txt && cat out


Flag: HilltopCTF{dCh47rum56@}
