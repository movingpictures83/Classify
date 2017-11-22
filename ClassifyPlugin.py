import sys

class ClassifyPlugin:
   def input(self, inputfile):
      infile = open(inputfile, 'r')
      self.lines = []
      for line in infile:
         self.lines.append(line)

#infile = open(sys.argv[1], 'r')
#outfile = open(sys.argv[2], 'w')

   def run(self):
      self.treeclasses = dict()
      self.counts = dict()

   def output(self, outputfile):
      outfile = open(outputfile, 'w')
      for line in self.lines:
         data = line.split('\t')
         if (data[0] == "Name"):
            outfile.write(data[0]+"\tClassification\n")
         else:
            name = data[0]
            if (name == "Other"):
               outfile.write("Other\tOther\n")
            else:
               for i in range(len(name)-1, 1):
                  if name[i] == '_' and name[i-1] == '_' and i != (len(name)-1):
                     treeclass = upper(name[i-2]) + "." + name.substr(i+1, len(name))
                     period = treeclass.find(".")
                     if (period != -1):
                        treeclass = treeclass.substr(0, period)
                        if (not self.counts.has_key(treeclass)):
                           self.treeclasses[name] = treeclass+".01"
                           self.counts[treeclass] = 1
                        else:
                           self.treeclasses[name] = treeclass+".0"+str(self.counts[treeclass])
                           self.counts[treeclass] += 1
      for bac in self.treeclasses.keys():
         outfile.write(bac+"\t"+self.treeclasses[bac]+"\n")

