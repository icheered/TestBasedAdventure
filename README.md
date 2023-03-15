# Text based adventure
One approach to a text based adventure. The story has been separated in a separate file as to not mix code and story.

Check out story.txt for an example of the syntax.
- +variablename[Text to print] - Ask for user input and store it in variablename
- {variablename} - Print the value of variablename
- [storyblock] - Start a storyblock
- @storyblock - Jump to a storyblock
    - If there are multiple jumps, the user is shown a prompt where they can choose which storyblock to jump to. The syntax is @storyblock[Text to print](valid user options)

The first storyblock must be called 'start' and the final storyblock must be called 'end'.