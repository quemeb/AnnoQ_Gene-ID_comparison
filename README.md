# AnnoQ Gene IDs Comparison 

The following code was designed to be run using input from [AnnoQ](annoq.org), which compiles results 
from [ANNOVAR](annovar.openbioinformatics.org/en/latest/), [SnpEff](pcingola.github.io/SnpEff/), and 
[VEP](uswest.ensembl.org/index.html).

The goal of this project is to compare Gene IDs assigned by the different annotation tools to the same 
SNP in order to inform the end users of any potential mismatch information. 

The program was started in R. However, due to the file sizes R slew down significantly and required more resources
which made us transition to Python. The initial template in R can be found in this repository. However, be adviced
it is not inclusive of the VEP comparison and should be run only in small datasets (for your computer's sake).  
