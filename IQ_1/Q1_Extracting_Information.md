
# Potential Questions to ask your interviewer:

  1. #### Should I consider two strings anagrams if they are identical but the cases are different ? <br> I.E 'car' & 'Car' or "The eyes" & they SEE".
       * Do not consider those string combinations to be anagrams
  2. #### Should I expect 'white spaces' (" ") only or others such as 'tab spaces' (" \t"), and 'new line spaces' (" \n")?
      * For now only consider white spaces, but there can many consecutive white spaces.

  3. #### Am I dealing with reasonably size strings or extremely large string input?
      * The size is reasonable say 100 characters or less for each input.
  4. #### Although unlikely, are these string inputs sorted?
      * No, they are not sorted.
  5. #### Are the the string inputs in specific case (lower case, upper case, or mixed) ?
       * I'd like you to consider each scenario.
       * 1st Scenario: lower case only (i.e. "hello", 'there') are valid
       *  2nd Scenario: Mixed case, i.e. "HoW IS it GOIng", "how is it going", "HOW IS IT GOING are all possible" are all valid
