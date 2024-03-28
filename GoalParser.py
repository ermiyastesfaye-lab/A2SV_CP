class Solution:
    def interpret(self, command: str) -> str:
        newCommand = ""
        for i in range(len(command)):
            if command[i] == "G":
                newCommand+="G"
            elif command[i:i+2] == "()":
                newCommand+="o"
            elif command[i:i+4] == "(al)":
                newCommand+="al"
        
        return newCommand
