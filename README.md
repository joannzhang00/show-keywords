# show-keywords
Given a chunk of text (through a file) and a keyword, locate the first occurrence of the keyword in the text, output the sentence in which the keyword appears, along with the sentences before and after.

To describe the program, let’s start with a brief review of the requirements. The program should read the following input:
1. the name of a file, containing the text, located in the same folder as the program, and
2. a keyword to be found in the text, specified in any combination of upper and lowercase letters.
The program must output the context in which that word occurs for the first time in the text. By context here we mean
(1) the sentence right before the sentence that contains the keyword, followed by
(2) the sentence that contains the keyword, showing the keyword in all capital letters, followed by (3) the sentence right after the sentence that contains the keyword.
(4) In addition a set of five periods should be displayed in place of text before (1) and/or after (3).
If the text does not contain the keyword, the program should report that.
