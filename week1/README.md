# Python Academy 2020 - Movie Dataset Exercise

## Project Structure

<img src="images/project_tree.png" width="200"/>

- **main:** File containing all the Exercises 
- **filters:** Package containing some filtering functions
- **impor_helper:**  Importing helper functions.

## Exercise 
**Note**: Some data samples contained errors or different format ending. Specifically, while importing the dataset not all data samples had a quotechar ending on 'whiteSpace' but on "breakline". 

-    list(csv.reader(csvfile, delimiter=',', quotechar='\n')
-    list(csv.reader(csvfile, delimiter=',', quotechar=' ')

This fact affected the result of our algorithms. As I had doubts on how to proceed on this,  I took the decision on skipping the data with no complete values and taking only data with quotechar ending in '\n'

#### - How many Black & White and color movies are in the list?
- 5024 Black and White and color movies are present - elapsed time : 6 ms
- 4815  Black and White and color movies are present - elapsed time : 3.9 ms 

#### -  How many movies were produced by director in the list?
Directors Histogram - Displaying first 10 results only <br/>
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
10 Days in a Madhouse  : 1 :  <br/>
The Bold and the Beautiful              : 1 :  <br/>
Barfi  : 1 :  <br/>
Down for Life  : 1 :  <br/>
The Secret              : 1 :  <br/>
The Opposite Sex  : 1 :  <br/>
Brave New Girl  : 1 :  <br/>
Sardaar Ji  : 1 :  <br/>
Elapse time in Seconds 0.014646053314208984
 
#### - Which are the 20 longest-running movies in the list?

20 longest movies are :<br/>
Trapped              : 511 : <br/>  
Carlos              : 334 :  <br/>
"Blood In : 330 :  <br/>
Heaven's Gate  : 325 :  <br/>
The Legend of Suriyothai  : 300 :  <br/>
Das Boot  : 293 :  <br/>
Apocalypse Now  : 289 : <br/> 
The Company              : 286 :  <br/>
Gods and Generals  : 280 :  <br/>
Gettysburg  : 271 :  <br/>
Arn: The Knight Templar  : 270 :  <br/>
Cleopatra  : 251 :  <br/>
Once Upon a Time in America  : 251 :  <br/>
The Wolf of Wall Street  : 240 :  <br/>
Gandhi  : 240 :  <br/>
Emma              : 240 :  <br/>
Dances with Wolves  : 236 :  <br/>
Lawrence of Arabia  : 227 :  <br/>
Gone with the Wind  : 226 :  <br/>
The Greatest Story Ever Told  : 225 :  <br/>
<br/>
Elapsed time 0.006849050521850586 seconds 

#### Which are the top 5 movies that raised more money in the list?
Avatar  : 760505847 :  <br/>
Titanic  : 658672302 :  <br/>
Jurassic World  : 652177271 :<br/>  
The Avengers  : 623279547 :  <br/>
The Avengers  : 623279547 :  <br/>
Elapsed time 0.006031990051269531 seconds <br/>

#### Which are the top 5 movies that made the least money in the list?
Skin Trade  : 162 :  <br/>
The Jimmy Show  : 703 :  <br/>
In Her Line of Fire  : 721 :  <br/>
Out of the Blue  : 728 :  <br/>
Perrier's Bounty  : 828 :  <br/>
Elapsed time 0.004686832427978516 seconds <br/>

#### Which are the top 3 movies that expend more money to be produced in the list?
Top 3 more expensive movies : <br/>
The Host  : 12215500000 :  <br/>
Lady Vengeance  : 4200000000 :  <br/>
Fateless  : 2500000000 :  <br/>
Elapsed time 0.0072977542877197266 seconds <br/>

#### Which are the top 3 movies that expend less money to be produced in the list?
Tarnation  : 218 :  <br/>
A Plague So Pleasant  : 1400 :  <br/>
The Mongol King  : 3250 :  <br/>
Elapsed time 0.004731893539428711 seconds <br/>

#### What year was the one who had more movies released ?
The year with more movies releases was : <br/>
' ('2009', 255) <br/>

Elapsed time 0.002627134323120117 seconds <br/>

#### What year was the one who had less movies released ?
The year with less movies releases was 1927 with 1 movie(s) <br/>
Elapse time in Seconds  0.0018129348754882812 <br/>

#### Create a actor ranking ordered by number of performances by:
#### - Number of movies where the actor performed
#### - Social Media Influence
#### - Best Movie

The algirthm consisted on summing up the quantity of times the actor appeared in different movies as principal, secondary and beyond. The Likes were summed but the IMB qualification was calculated with the average on the different results. <br/>

Actor ranking : <br/>
('Robert De Niro', 54, 1188000, 7.118836910088769) <br/>
('Morgan Freeman', 45, 495000, 7.8965078860196005) <br/>
('Johnny Depp', 41, 1640000, 6.568560059206175) <br/>
('Bruce Willis', 39, 507000, 6.231539757813152) <br/>
Elapsed time :  0.0437769889831543 <br/>

#### Create a “tag cloud” using tags or keywords of the movie: To do this you can create an ordered ranking
#### of the number of word occurrences.

The 1123 <br/>
of 481 <br/>
the 455 <br/>
and 138 <br/>
A 101 <br/>
in 100 <br/>
to 99 <br/>
a 84 <br/>
2 79 <br/>
Man 65 <br/>
& 57 <br/>
Love 53 <br/> 
<br/>
Elapsed time :  1.029115915298462 Seconds

#### What movie genre raised more money per year?

#### What movie genre raised less money per year?
<br/>
- Raised more money in  2009 Action <br/>
- Raised less money in  2009 Sci-Fi<br/>

- Raised more money in  2007 Adventure<br/>
- Raised less money in  2007 Western<br/>

- Raised more money in  2015 Animation <br/>
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
More Liked Movies by the Community <br/>
Drama 55762519<br/>
Comedy 27172616<br/>
Adventure 24387570<br/>
Crime 20474813<br/>
Family 19189809<br/>
Elapse timme in seconds  0.03395199775695801<br/>

#### Which are the top five best reputation directors?
Steven Spielberg 6582<br/>
Ridley Scott 4930<br/>
Peter Jackson 4542<br/>
Martin Scorsese 4285<br/>
Clint Eastwood 4244<br/>
The Top five Directors are : <br/>
Elapse time in seconds 0.008759021759033203<br/>
