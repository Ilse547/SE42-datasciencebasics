# Dataset  
GBIF.org (15 November 2025) GBIF Occurrence Download https://doi.org/10.15468/dl.3ydkae 

## Custom SQL used for getting the data:
```
SELECT
  species,
  specieskey,
  "year",
  "month",
  countrycode,
  COUNT(*) AS occurrences
FROM
  occurrence
WHERE
  occurrence.datasetkey = '4fa7b334-ce0d-4e88-aaae-2e0c138d049e'
  AND occurrence.countrycode IN ('DE', 'FR')
  AND occurrence."year" BETWEEN 2016 AND 2025
  AND occurrence.hasgeospatialissues = FALSE
  AND NOT GBIF_STRINGARRAYCONTAINS(occurrence.issue, 'TAXON_MATCH_FUZZY', TRUE)
  AND (
    occurrence.distancefromcentroidinmeters >= 2000.0
    OR occurrence.distancefromcentroidinmeters IS NULL
  )
  AND occurrence.basisofrecord NOT IN ('FOSSIL_SPECIMEN', 'LIVING_SPECIMEN')
  AND occurrence.occurrencestatus = 'PRESENT'
  AND occurrence.specieskey IS NOT NULL
  AND occurrence."month" IS NOT NULL
  AND occurrence.hascoordinate = TRUE
GROUP BY
  species,
  specieskey,
  "year",
  "month",
  countrycode;
  ```  

### Questions:
1. Which bird species are the most commonly observed overall?
2. Which bird species are the most commonly observed overall?
3. What are the seasonal patterns in bird observations?
4. Which species show the most significant changes in observation frequency over the years?
6. What are the top 5 most observed species in each country?

## Files:
The questions are answered using the matching jupyter notebook or python file  
Question numbered as 1 is answered using the file:  
``` Q1.ipynb ``` or ``` Q1.python ```  
## Running the files:
The files ending with: ``` .ipynb ``` need to be run using a jupyter notebook.  
The files ending with : ``` .py ``` can be run using the command:  
``` python3 <filename> ``` or simply in vscode.  

