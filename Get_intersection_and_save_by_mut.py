import pyranges as pr
import pandas as pd

def Read_files(file):
    

    cols = "Chromosome Start End Name Score Strand".split()

    df_file = pd.read_csv(file, sep='\t', comment='t', header=None)
    df_file.columns = cols
    
    return df_file


def Get_intersection_by_mutation(a,b, mutation, outfile):
    
    a_mut = a[a["Name"]== mutation]
    b_mut = b[b["Name"]== mutation]
    
    
    # create PyRanges-objects from the dfs
    gr1, gr2 = pr.PyRanges(a_mut), pr.PyRanges(b_mut)
    
    # intersect the two
    gr = gr1.intersect(gr2)
    
    gr.to_bed(outfile)
    
def main(Afile, Bfile, mutation, outfile):
    
    df_A = Read_files(Afile)
    df_B = Read_files(Bfile)   
    Get_intersection_by_mutation(df_A, df_B, mutation, outfile)

if __name__ == "__main__": 
    main("A.bed", "B.bed", "AC", "AC.bed")
    main("A.bed", "B.bed", "AT", "AT.bed")
    main("A.bed", "B.bed", "AG", "AG.bed")
