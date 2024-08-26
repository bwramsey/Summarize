
# Summarize
This is a small script to summarize student responses to a survey question (for instance, downloaded from a Canvas quiz or survey) for the instructor. It uses the python ollama library to summarize student responses (saved in a .csv file) to survey questions, writing the output to a .txt file. It can be easily modified to summarize any list of data stored in a file this way.

Dependancies:

  *Ollama* -> both [Ollama itself](https://ollama.com/) and the [python ollama module](https://ollama.com/blog/python-javascript-libraries).

  *[Ollama model of choice](https://ollama.com/library)* -> currently set to "gemma2", 
    but can be changed by modifying the "aiModel" variable at the top of the summarize.py file depending on the ollama module you prefer.

To use:
  
  Have the .csv file of student responses in the same directory as summarize.py. The student responses should all be in the same column.
  Update the "entryCol" variable to indicate which column these responses are located. For example, if your data is in Column A you would set entryCol=0, for Column B use entryCol=1, ... etc.
  
  To run:

    python summarize.py

  You will be prompted for the .csv file to use, and for the output filename to use. Depending on the size of your dataset, this could take several minutes.
