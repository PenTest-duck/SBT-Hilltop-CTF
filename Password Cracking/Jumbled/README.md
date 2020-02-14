# Jumbled

I've found a hash of the password for the domain controller.

`Hash: 01F3273F68195C29A1A2365BE7AD2B1AAD469A73`

I've also found this note:

```
Company Password Policy:
  - A hex digit prepended  
  - A hex digit appended 
  - First letter capitalised
  - An '@' appended to the end
  - Leetspeak (a => 4, b => 6, e => 3, g => 9, i => 1, o => 0, s => 5, t => 7, z => 2) *Capital letters not included*
Example: rockme => fR0ckm37@
```

Can you crack the hash using rockyou.txt?


Hint 1: Rule-based attacks are very useful in applying modifications to passwords from the wordlist before they are matched against the hash.
