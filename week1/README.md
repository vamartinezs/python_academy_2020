# Python Academy 2020 - Movie Dataset Exercise

## Project Structure

<img src="images/project_tree.png" width="200"/>

- **main:** File containing all the Exercises 
- **filters:** Package containing some filtering functions
- **impor_helper:**  Importing helper functions.

## Exercise 
**Note**: Some results presented errors importing the dataset as not all data had an ending quotechar in 'whiteSpace'. This is why some data  values may present different results.

-    list(csv.reader(csvfile, delimiter=',', quotechar='\n')
-    list(csv.reader(csvfile, delimiter=',', quotechar=' ')

I had doubts on how to proceed on this. Finally, I took the decision on skipping the data with no complete values and taking only data with quotechar ending in '\n'


#### - How many Black & White and color movies are in the list?
- 5024 Black and White and color movies are present - elapsed time : 6 ms
- 4815  Black and White and color movies are present - elapsed time : 3.9 ms 

#### -  How many movies were produced by director in the list?
Histogram on Directors field - Displayed first results <br/>
<br/>
Steven Spielberg : 26 :  <br/>
Woody Allen : 22 :  <br/>
Martin Scorsese : 20 : <br/>
Clint Eastwood : 20 :  <br/>
Ridley Scott : 17 :  <br/>
Tim Burton : 16 :  <br/>
Steven Soderbergh : 16 :  <br/>
Spike Lee : 16 :  <br/>
Renny Harlin : 15 : <br/>
Oliver Stone : 14 : <br/>
<br/>
Elapsed time :  6.8 ms 


#### - Which are the 10 less criticized movies in the list?

10 less criticized movies are : <br/>
Harry Potter and the Deathly Hallows: Part II  : 1 :  <br/>
The Border              : 1 :  <br/>
10 Days in a Madhouse  : 1 :  \\
The Bold and the Beautiful              : 1 :  \\
Barfi  : 1 :  \\
Down for Life  : 1 :  \\
The Secret              : 1 :  
The Opposite Sex  : 1 :  
Brave New Girl  : 1 :  
Sardaar Ji  : 1 :  
Elapse time in Seconds 0.014646053314208984
 
#### - Which are the 20 longest-running movies in the list?

20 longest movies are :<br/>
Trapped              : 511 : <br/>  
Carlos              : 334 :  <br/>
"Blood In : 330 :  <br/>
Heaven's Gate  : 325 :  
The Legend of Suriyothai  : 300 :  
Das Boot  : 293 :  
Apocalypse Now  : 289 :  
The Company              : 286 :  
Gods and Generals  : 280 :  
Gettysburg  : 271 :  
Arn: The Knight Templar  : 270 :  
Cleopatra  : 251 :  
Once Upon a Time in America  : 251 :  
The Wolf of Wall Street  : 240 :  
Gandhi  : 240 :  
Emma              : 240 :  
Dances with Wolves  : 236 :  
Lawrence of Arabia  : 227 :  
Gone with the Wind  : 226 :  
The Greatest Story Ever Told  : 225 :  
Elapsed time 0.006849050521850586 seconds 

Elapsed time 0.0059680938720703125 seconds 

#### Which are the top 5 movies that raised more money in the list?
Avatar  : 760505847 :  <br/>
Titanic  : 658672302 :  <br/>
Jurassic World  : 652177271 :<br/>  
The Avengers  : 623279547 :  <br/>
The Avengers  : 623279547 :  <br/>
Elapsed time 0.006031990051269531 seconds <br/>

#### Which are the top 5 movies that made the least money in the list?
Skin Trade  : 162 :  
The Jimmy Show  : 703 :  
In Her Line of Fire  : 721 :  
Out of the Blue  : 728 :  
Perrier's Bounty  : 828 :  
Elapsed time 0.004686832427978516 seconds 
Elapsed time 0.004220724105834961 seconds 

#### Which are the top 3 movies that expend more money to be produced in the list?
Top 3 more expensive movies : '
The Host  : 12215500000 :  
Lady Vengeance  : 4200000000 :  
Fateless  : 2500000000 :  
Elapsed time 0.0072977542877197266 seconds 

#### Which are the top 3 movies that expend less money to be produced in the list?
Tarnation  : 218 :  
A Plague So Pleasant  : 1400 :  
The Mongol King  : 3250 :  
Elapsed time 0.004731893539428711 seconds 

#### What year was the one who had more movies released ?
The year with more movies releases was : '
' ('2009', 255) 

Elapsed time 0.002627134323120117 seconds 

#### What year was the one who had less movies released ?
The year with less movies releases was 1927 with 1 movie(s)
Elapse time in Seconds  0.0018129348754882812

#### Create a actor ranking ordered by number of performances by:
#### - Number of movies where the actor performed
#### - Social Media Influence
#### - Best Movie

The algirthm consisted on summing up the quantity of times the actor appeared in different movies as principal, secondary and beyond. The Likes were summed but the IMB qualification was calculated with the average on the different results. 

Actor ranking : 
('Robert De Niro', 54, 1188000, 7.118836910088769)
('Morgan Freeman', 45, 495000, 7.8965078860196005)
('Johnny Depp', 41, 1640000, 6.568560059206175)
('Bruce Willis', 39, 507000, 6.231539757813152)
Elapsed time :  0.0437769889831543

#### Create a “tag cloud” using tags or keywords of the movie: To do this you can create an ordered ranking
#### of the number of word occurrences.

The 1123
of 481
the 455
and 138
A 101
in 100
to 99
a 84
2 79
Man 65
& 57
Love 53

Elapsed time :  1.029115915298462 Seconds

#### What movie genre raised more money per year?

#### What movie genre raised less money per year?

- Raised more money in  2009 Action
- Raised less money in  2009 Sci-Fi

- Raised more money in  2007 Adventure
- Raised less money in  2007 Western

- Raised more money in  2015 Animation
- Raised less money in  2015 Western

- Raised more money in  2012 Action
- Raised less money in  2012 War

- Raised more money in  2004 Adventure
- Raised less money in  2004 Drama

- Raised more money in  1997 Action
- Raised less money in  1997 Sci-Fi

- Raised more money in  2011 Comedy
- Raised less money in  2011 Horror

- Raised more money in  1992 Action
- Raised less money in  1992 Drama

- Raised more money in  2013 Comedy
- Raised less money in  2013 Thriller

- Raised more money in  2010 Comedy
- Raised less money in  2010 Sci-Fi

- Raised more money in  2008 Action
- Raised less money in  2008 Horror

- Raised more money in  2003 Action
- Raised less money in  2003 Horror

- Raised more money in  1999 Comedy
- Raised less money in  1999 Horror

- Raised more money in  1998 Comedy
- Raised less money in  1998 Drama

Elapse time in seconds :  0.021592140197753906

#### What movie genre does the public like most?
More Liked Movies by the Community 
More Liked Movies by the Community 
Drama 55762519
Comedy 27172616
Adventure 24387570
Crime 20474813
Family 19189809
Elapse timme in seconds  0.03395199775695801

#### Which are the top five best reputation directors?
Steven Spielberg 6582
Ridley Scott 4930
Peter Jackson 4542
Martin Scorsese 4285
Clint Eastwood 4244
The Top five Directors are : 
Elapse time in seconds 0.008759021759033203
