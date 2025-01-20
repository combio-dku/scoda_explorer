## Tissue selection
TISSUE = 'Breast'
## You can select one from 
##     ['Not specified', 'Generic', 'Blood', 'Brain', 'Bone', 'Breast', 
##      'Eye', 'Embryo', 'Heart', 'Intestine', 'Kidney', 'Liver', 
##      'Lung', 'Pancreas', 'Stomach', 'Skeletal muscle', 'Skin']
## If 'Not specified', the pipelie selects the best match among the tissues below.
## 'Generic' applies well for most of tissues, except for Brain, 'Bone', Eye, 'Embryo', 'Skeletal muscle'.

REF_NORMAL_CONDITIONS = 'Normal'

## Cell/Gene filtering params
N_GENES_MIN = 200
N_CELLS_MIN = 10 
PCT_COUNT_MT_MAX = 20

## Reference celltypes for InferCNV
INFERCNV_REF_CELLTYPES = ['T cell', 'B cell', 'Myeloid cell', 'Fibroblast'] 
INFERCNV_REF_CONDITION = None # ['Normal'] 

## minimum number of cells for cell-cell interaction analysis
## Celltypes with its number of cells less than this number will be excluded from CCI analysis
MIN_NUM_CELLS_FOR_CCI = 40  

## Unit of CCI run. It must be either 'sample'  or 'condition'
UNIT_OF_CCI_RUN = 'sample'  

## Valid when UNIT_OF_CCI_RUN = 'sample' 
## When UNIT_OF_CCI_RUN is 'sample', CCIs per condition will be 
## counted only if they appears at least this percentage of 
## samples belonging to that condition.
CCI_MIN_OCC_FREQ_TO_COUNT = 0.5   

## P-value cutoff to filter out CCIs
CCI_PVAL_CUTOFF = 0.1  

## Mean cutoff to filter out CCIs
CCI_MEAN_CUTOFF = 0.1  

## celltype taxonomy level for CCI & DEG analysis
## It can be one of celltype_major, celltype_minor, or celltype_subset.
## CCI and DEG will be performed based on this level of celltype taxonomy.
CCI_DEG_BASE = 'celltype_minor'  

## minimum number of cells for DEG analysis
## Celltypes with its number of cells less than this number will be excluded from DEG analysis
MIN_NUM_CELLS_FOR_DEG = 100  

## P-value cutoff to filter out GO terms
DEG_PVAL_CUTOFF_FOR_GSEA = 0.1

## Reference group (condition) for DEG analysis. 
## If None, DEG performed in one-against-the-rest basis
DEG_REF_GROUP = 'Normal'  

## P-value cutoff for DEGs to be used for GSA/GSEA
GSA_PVAL_CUTOFF = 0.1 

