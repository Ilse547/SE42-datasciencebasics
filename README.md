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

After processing the data we can see which are the 10 most observed species in germany and france.  

![alt text](/graphs/q1.png "Graph for Q1")


## Q2: How do bird sightings vary over the year?  
Files:``` Q2.ipynb ``` and ``` /python/Q2.py ```
![alt text](/graphs/q2.png "Graph for Q2")  
We can see that at the begining of the year and at the end of the year are the least bird sightings.  
We see a spike in the months of september and october, which corresponds to the migration of geese to the south. 
During the colder months of November, December, January and February there are the least bird sightings, we can interpret it as a mix of 2 reasons:
1. People dont go out as often in winter than in warmer months.  
2. The birds that remain in Europe in those months are smaller birds such as Doves, Great Tits, Blue Tits, Moorhen etc.. which are birds that can hide pretty well  

During the months in the middle of the year there are bigger birds that are also more known like geese, mallard ducks etc..  
people also tend to spend more time outside because of the wamer temperatures.  

## Q3: Which species show the most significant changes in observation frequency over the years?  
Files:``` Q3.ipynb ``` and ``` /python/Q3.py ```
![alt text](/graphs/q3.png "Graph for Q3")  
We see that the biggest changes over the years are birds that mostly live in the cities like tits, pigeons, blackbirds and crows.  

## Q4: How does the number of sightings of Phylloscopus collybita vary per month and country?
Files:``` Q4.ipynb ``` and ``` /python/Q4.py ```  
![alt text](/graphs/q4.png "Graph for Q4")  

We can observe that the Chiffchaff (Phylloscopus collybita) is more observed in germany, especially in the months of april, may, and august where we have a really big difference. This is due to the german climate, they live in the north on europe and migrate to the south during the winter.  
Thats the reason we see a small spike in septermber were they start there migration and move to france.  

## Q5: How doe4s the diversity of different species changed over the years ?
Files:``` Q5.ipynb ``` and ``` /python/Q5.py ```  
![alt text](/graphs/q5.png "Graph for Q5")    

We see that the overall sightings of different spcies has gone up, probably not because there is a bigger diversity but rather because more people have found this hobby and started reporting birds they saw.  
We can see this a bit since there is a dip in observations in the year 2021 where there was the covid pandemic and less people went outside. In that time nature took over cities and animals like flamingoes returned in metropoles like Mumbai. 