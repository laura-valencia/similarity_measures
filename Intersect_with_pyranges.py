import pyranges as pr
import pandas as pd

def Read_files(file):
    

    cols = "Chromosome Start End Name Score Strand".split()

    df_file = pd.read_csv(file, sep='\t', comment='t', header=None)
    df_file.columns = cols
    
    return df_file

def Get_intersection(a,b, outfile):
    
    # create PyRanges-objects from the dfs
    gr1, gr2 = pr.PyRanges(a), pr.PyRanges(b)
    
    # intersect the two
    gr = gr1.intersect(gr2)
    
    gr.to_bed(outfile)
    
def main(Afile, Bfile, outfile):
    
    df_A = Read_files(Afile)
    df_B = Read_files(Bfile)   
    Get_intersection(df_A, df_B, outfile)

if __name__ == "__main__": 
    main("A.bed", "B.bed", "Valencia_Task1.bed")