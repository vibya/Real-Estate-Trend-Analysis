# Neighborhood Dynamics and Housing Price 
where does your dollar work the hardest if invested in Austin today?

## Background
- What is the average/median house price per neighborhood/zip code?
- What is house type demographics in Ausin?
- What is the impact of school quality on house prices? (Greatschools.org API)
- What is the impact of crime rate on house prices? (https://github.com/contra/spotcrime)
- How the average annual house hold income is related to house prices?
- What is the impact of population density on house prices?
- How the average construction age is related to house prices?
- How the average area in sqft is related to house prices?
- How the amount of public recreational facilities is related to house prices?
-  what zip code has the highest construction currently -->
   by # of permits,
   by dollar amt,
   by type (residential/commercial)

-  what zip code has the lowest construction currently -->
   by # of permits,
   by dollar amt,
   by type (residential /commercial)

-  which year had biggest percentage increase

-  which zip had the biggest increase but has now slowed down?

-  which zip was steady and then had a sudden increase?

-  take the top zips and pull school data,
   same with bottom zips

-  does greatschools api provide school history? 
   we can use this to track how a school performance changed depending on how many ppl moved in


## Methodology

## Data

## Report

## Requirements

- python=3.6.5
- jupyter=1.0.0
- nb_conda=2.2.1
- python-zillow=0.2.0  
- xmltodict=0.11.0
- uszipcodei=0.1.3
- quandl=3.3.0 

## Directory Structure
```
.
├── data		<- Data to besed in this project.
│   ├── ext
│   ├── int
│   └── raw
├── images		<- Image for `README.md` files.
├── notebooks		<- Ipython notebook files to be used in this project.
├── reports		<- Generated analysis as HTML, PDF, LatEx, etc.
│   ├── figures		<- Generated graphics and figures to be used in reporting.
│   └── logs		<- Generated log files.
├── scripts		<- Python scripts codes to be used in this project.
└── src			<- Source codes to be used in this project.
   
```
## Installation
TBA

## To Do

### Data collection / 06.07
- [ ] Construction demogaphics; zip codes that will give us the answer to our big question - where to buy in Austin (by Vib)
- [ ] Housing price demographics, housing price temporal trends: house median prices per zip code, historical housing prices (by Aidin/Karol)
- [x] Household income data.
- [ ] School quality demographics - by Keith [https://www.greatschools.org/api/request-api-key/] (by Keith)
- [x] Morgage data by Keith/Karol)
- [ ] Data interpolation (by Aidin)
- [ ] Data cleansing

### Visualization / 06.08
#### Gears
- [ ] Choropleth function (by Aidin)
- [ ] Scatter Plot (by Aidin)
- [ ] Bar chart 
- [ ] Pie chart
#### Plots
- [ ]

### Modeling / 06.10
- [ ] Build/develpe model
- [ ] Train model
- [ ] Evaluate
- [ ] Results

### Presentaion / 06.12
- [ ] Slides
- [ ] Scripts

## References

## License
TBA

















