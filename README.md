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
2. How do bird sightings vary over the year?  
3. Which species show the most significant changes in observation frequency over the years?   
4. How does the number of sightings of Phylloscopus collybita vary per month and country?
5. How doe4s the diversity of different species changed over the years ?
## Files:
The questions are answered using the matching jupyter notebook or python file  
Question numbered as 1 is answered using the file:  
``` Q1.ipynb ``` or ``` Q1.python ```  
## Running the files:
The files ending with: ``` .ipynb ``` need to be run using a jupyter notebook.  
The files ending with : ``` .py ``` can be run using the command:  
``` python3 <filename> ``` or simply in vscode.  

The jupyter ntoebook files were transformed into python files using vscode.  

To rpoperly run the file and allow pandas to read the csv file, replace the path of the second cell ot the absolut path of the file:
```
df = pd.read_csv("<Path>/0035785-251025141854904.csv",
sep="\t",
skiprows=1,
names=[
    "species","specieskey","year","month","countrycode","occurences"
])
```

# Answers:
## Q1: Which bird species are the most commonly observed overall?
Files: ``` Q1.ipynb ``` and ``` /python/Q1.py ```
![alt text](/graphs/q1.png "Graph for Q1")

We can see that the most common species observed overall is the Black bird then the Common Wood pigeon. These birds are very common in the cities, which is where most people live. Thus they are observed more often than other species.

## Q2: How do bird sightings vary over the year?  
Files:``` Q2.ipynb ``` and ``` /python/Q2.py ```
![alt text](/graphs/q2.png "Graph for Q2")  

We can see that the Bird sightings vary a lot over the years, during the colder months there are less bird sightings then during the warm months. This is likely due to the migration of birds to the south, if there are less birds here then there are less birds that get seen. Furthermore we see a spike during the months of September and October. This is due to the migration of geese and birds alike to the south.

## Q3: Which species show the most significant changes in observation frequency over the years?  
Files:``` Q3.ipynb ``` and ``` /python/Q3.py ```
![alt text](/graphs/q3.png "Graph for Q3")  

We see that the birds with the most changes in sightings over the years are very similar to the birds with the most reported sightings overall. This is likely due to the fact that these are well established birds in cities like the blackbird, pigeon, tits, etc…  This is probably due to the fact that these Birds are dependent on humans in the cities and increase in population the more human activities there are. It helps them eat by finding food scraps on the floor for example.

## Q4: How does the number of sightings of Phylloscopus collybita vary per month and country?
Files:``` Q4.ipynb ``` and ``` /python/Q4.py ```  
![alt text](/graphs/q4.png "Graph for Q4")  

That Bar Graph looks very similar to the line graph of question 1, we have the same spikes during March, April and May and again in September and October where they migrate either back from south to north or from north to south. We also see that Germany has a lot more sightings of the Chiffchaff (Phylloscopus collybita) when we check the total number of occurrences we see that Germany has about 1.4 million more sightings than france, so that difference between france and germany seems normal and is to be expected.


## Q5: How doe4s the diversity of different species changed over the years ?
Files:``` Q5.ipynb ``` and ``` /python/Q5.py ```  
![alt text](/graphs/q5.png "Graph for Q5")    

We see that over the years there have been more different types of species observed, going from about 470 different species in 2016 to 530 in 2023. We can see a slight dip in the year 2018 and one in the year 2021. The dip in 2021 is caused by the lockdown not allowing people to go out and thus not being able to watch and observe birds. The dip in 2018 might be because there were less people going out to observe birds or maybe just a year with a lot of bad weather that might have discouraged people. We can see that overall the increase in sightings happens post covid-19 pandemic. Which makes sense since during the lockdown nature was able to heal and come back to the cities, such as the flamingoes in Mumbai. Also the ability to better record the data thanks to smartphones allows for more data collection.
