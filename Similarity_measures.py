import pandas as pd
import pyranges as pr
import math

# Alternative similarity measure: Otsuka-Ochiai I (1957) (Also known as Ochiai coefficient)
# This measure is similar to Jaccard and is considered equivalent (Meyer, 2004)
# There are no negative controls in our data (corresponding to "d" in a contingency table).
# Therefore I chose a measure that only requires a, b and c.
# Meyer, 2004: http://dx.doi.org/10.1590/S1415-47572004000100014 



def Read_files(file):
    

    cols = "Chromosome Start End Name Score Strand".split()

    df_file = pd.read_csv(file, sep='\t', comment='t', header=None)
    df_file.columns = cols
    
    return df_file


def Compute_Ochiai(df_A, df_B, outfile):

    
    # create PyRanges-objects from the dfs
    grA, grB = pr.PyRanges(df_A), pr.PyRanges(df_B)
    
    
    # Establish values in a contingency table
    #
    #     |B=1  |B=0  | 
    # A=1 |a    |b    |
    # A=0 |c    |d    |
   
    #A intersection B
    gri = grA.set_intersect(grB)
    a = gri.length
    
    # calculate length of each set A and B 
    An = grA.length
    Bn = grB.length
    
    # length covered found in A, but not B
    b = An - a
    
    # length covered found in B, but not A
    c = Bn - a
    
    # Compute Ochiai coefficient
    
    sqr = math.sqrt((a+b)*(a+c))
    K = a/sqr


    print("Ochiai coefficient: ", K)
   

    
    with open(outfile, 'w') as outfile: 
      outfile.write("Calculate another similarity measure" + "\n")
      outfile.write("Ochiai coefficient: " + str(K))



        
  
def main(Afile, Bfile, outfile):
    
    df_A = Read_files(Afile)
    df_B = Read_files(Bfile)   
    Compute_Ochiai(df_A, df_B, outfile)

if __name__ == "__main__": 
    main("A.bed", "B.bed", "Results.txt")