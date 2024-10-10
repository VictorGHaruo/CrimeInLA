Hypothesis One - Crime & Location
=================================

The distribution of crimes by LAPD is uneven across regions. Some crimes are more frequent in certain areas, 
and some regions are more "dangerous" than others.

Method
------

With the hypothesis that the occurrence of crimes in Los Angeles is uneven, as well as the safety of each region, an analysis
was conducted on the crime reports issued between 2020 and 2023 by the 21 LAPD divisions.

Due to the wide variety of crime types, they were categorized to facilitate data analysis and visualization. The crimes 
were separated into three categories based on their severity: "low," representing minor crimes like petty thefts; "medium," 
representing significantly more serious crimes like grand thefts and assaults; and "high," which includes the most severe 
crimes, such as heinous crimes.

For data analysis and visualization, three different types of graphs were used: bar charts, heat maps, and geographic heat maps,
as well as an additional database to plot the map of Los Angeles with the boundaries of the police departments.

The analysis focused solely on quantitative aspects of the occurrences, filtering for crimes that occurred at least once in each 
region.The graphs "Crimes_most_occorencys" and "Crimes_Occorrencys" show the crimes that were most reported and the total number of 
occurrences by region. It is noted that while crime '510' is the most frequent, it does not have the highest occurrence in the 
"Central" region, which has the highest number of overall occurrences. This indicates that the distribution of crimes may not be 
simply proportional, potentially conditioned by other factors such as historical and geographical contexts.

An analysis was also conducted to identify the most dangerous regions based on the categorization of crimes. The danger index of a 
region is calculated as the number of 'low' severity crimes plus three times the number of 'medium' severity crimes plus ten times 
the number of 'high' severity crimes.

Columns Used
------------
* AREA NAME
* Crm Cd (Crime Code)

.. figure:: ../../data/Crime_&_Location/Crimes_most_occurrences.png
   :width: 600px
   :height: 400px
   :align: center

.. list-table::
   :width: 100%
   :class: borderless

   * - .. figure:: ../../data/Crime_&_Location/Low_Crimes.png
          :width: 100%
          :align: right
     - .. figure:: ../../data/Crime_&_Location/Low_Crimes_map.png
          :width: 100%
          :align: left
   * - .. figure:: ../../data/Crime_&_Location/Medium_Crimes.png
          :width: 100%
          :align: right
     - .. figure:: ../../data/Crime_&_Location/Medium_Crimes_map.png
          :width: 100%
          :align: left
   * - .. figure:: ../../data/Crime_&_Location/High_Crimes.png
          :width: 100%
          :align: right
     - .. figure:: ../../data/Crime_&_Location/High_Crimes_map.png
          :width: 100%
          :align: left
   * - .. figure:: ../../data/Crime_&_Location/Crimes_Occurrences.png
          :width: 100%
          :align: right
     - .. figure:: ../../data/Crime_&_Location/Crimes_Occurrences_map.png
          :width: 100%
          :align: left
   * - .. figure:: ../../data/Crime_&_Location/Areas_severity.png
          :width: 100%
          :align: right
     - .. figure:: ../../data/Crime_&_Location/Areas_severity_map.png
          :width: 100%
          :align: left

Analysis
--------

Most Frequent Crimes (and Most Frequent Regions):
* 510 - 77th Street
* 330 - Central
* 354 - 77th Street
* 624 - Central
* 740 - Central

Regions with Most Occurrences (and Most Frequent Crime):
* Central - 330
* 77th Street - 510
* Pacific - 510 
* Southwest - 510 
* Wilshire - 510

Most Dangerous Regions (and Most Frequent Crime Type):
* Central - high
* 77th Street - high
* Southwest - high
* Pacific - high
* Hollywood - high

Regions with the highest number of occurrences are also the most dangerous, and conversely, the most dangerous regions have the 
highest number of serious crimes. Similarly, the most frequent crimes have a higher incidence in regions with higher crime rates, 
and regions with a higher number of occurrences generally have the most incident crimes that are most frequent overall. There are 
few cases like crime 330, where occurrences are significantly more frequent in the "Central" region; most crimes are distributed 
without major concentrations by region.

Conclusion
----------

There is some disparity in the occurrence of crimes by LAPD, but this inequality is not as significant. Although regions like "Central" 
and 77th Street have many more occurrences than others, these areas tend to not deviate much from the average occurrences of crimes 
overall. Moreover, the distribution of specific crimes tends to follow the distribution of general occurrences, with rare exceptions, 
leading to regions that already have a high number of occurrences also having significant numbers of high-severity crimes. In other words,
the danger level of a region is directly linked to the overall number of crime occurrences.
