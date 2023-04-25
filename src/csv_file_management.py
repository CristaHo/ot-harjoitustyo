from pathlib import Path

class CSVfiles:
    def write_to_file(self, filename, day, amount, what):
        name_of_file = f"{filename}.csv"
        with open(name_of_file, "a") as file:
            file.write(f"{day};{amount};{what}\n")
        self.read_file(filename)

    def read_file(self, name_of_file):
        filename = f"{name_of_file}.csv"
        dictionary = {}
        filepath = Path(filename)
        filepath.touch(exist_ok= True)
        open(filepath,"a")

        #if not filename:
         #   with open(filename, "w") as file:
          #      file.write("0;0;0\n")
        with open(filename) as file:
            for row in file:
                row = row.replace("\n", "")
                section = row.split(";")
                day = section[0]
                amount = section[1]
                what = section[2]
                dictionary[day] = [amount, what]
                #print(dictionary)
        return dictionary

#write = CSVfiles()
#write.write_to_file("testfile", 1, 50, "palkka")
#write.read_file("testfile")
