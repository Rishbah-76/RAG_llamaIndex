from llama_index.core.tools import FunctionTool 
import os 

notr_file = os.path.join("data","notes.txt")
def save_file(note):
    if not os.path.exists(notr_file):
        open(notr_file,"w")
    with open(notr_file,"a") as f:
        f.write(note +  "\n")
        
    return "note saved"

note_engine =FunctionTool.from_defaults(
    fn=save_file,
    name="note_saver",
    description="This tool is used to save the text reported from the Output in a note.text file"
)