# all_prime

<p><span style="color:#000000">In this article, I&#39;m going to be running you through how to write a very simple program that can be able to get the prime factors in index notation&nbsp;of a given number.&nbsp;</span></p>

<p><span style="color:#000000">First I would like to emphasize that python is a very vast programming language that you can learn and begin to use in a very short time with extended features through installable modules.</span></p>

<p><span style="color:#000000">If you don&#39;t want to read this article, you take a U-turn to my git repository of the program&nbsp;</span><a href="https://github.com/Ebonined/all_primes.git" target="_blank"><span style="color:#2980b9">here</span></a><span style="color:#000000">, If you need to continue, make sure you have a P.C with python 3.X installed also with a python IDE (Integrated Development Environment), like </span><a href="https://www.sublimetext.com/"><span style="color:#2980b9">Sublime Text</span></a><span style="color:#000000">, </span><a href="https://code.visualstudio.com/download"><span style="color:#2980b9">Visual Studio Code</span></a><span style="color:#000000">, </span><a href="https://www.jetbrains.com/pycharm/"><span style="color:#2980b9">Pycharm</span></a><span style="color:#000000">&nbsp;and many more, you can google for more.</span></p>

<ul>
	<li><span style="color:#000000">The first thing to do is to analyze the problem in&nbsp;hand, prime numbers are numbers that can be divided by themselves and 1. Examples of prime numbers are 2, 3, 5, 7 and so one.</span></li>
	<li><span style="color:#000000">So we need to find a way to generate these prime numbers with a python code by defining a function that can generate prime numbers until the number we want to get its prime factors.</span></li>
	<li>
	<div style="background:#eeeeee; border:1px solid #cccccc; padding:5px 10px">
	<p><code>01: def allprimes(number=997):</code></p>

	<p><code>02: &quot;&quot;&quot;</code></p>

	<p><code>03: Function to help get all the prime number from 1 to the intended number</code></p>

	<p><code>04: &quot;&quot;&quot;</code></p>

	<p><code>05:&nbsp; &nbsp; oddnum = [2]</code></p>

	<p><code>06:&nbsp; &nbsp; for num in range(2,number+1):</code></p>

	<p><code>07:&nbsp; &nbsp; &nbsp; &nbsp; if num%2 != 0:</code></p>

	<p><code>08:&nbsp; &nbsp; &nbsp; &nbsp; oddnum.append(num)</code></p>

	<p><code>09:</code></p>

	<p><code>10:&nbsp; &nbsp; size = len(oddnum)-1 # lenght of the list oddnum-1</code></p>

	<p><code>11:</code></p>

	<p><code>12:&nbsp; &nbsp; for num in oddnum:</code></p>

	<p><code>13:&nbsp; &nbsp; &nbsp; &nbsp; templist = []</code></p>

	<p><code>14:&nbsp; &nbsp; &nbsp; &nbsp; for div in oddnum:</code></p>

	<p><code>15:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if num != div and num%div != 0:</code></p>

	<p><code>16:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;templist.append(num)</code></p>

	<p><code>17:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;if len(templist) == size:&nbsp;</code></p>

	<p><code>18:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; yield templist[0] # appends that number to the list</code></p>
	</div>
	</li>
	<li><span style="color:#000000"><strong>Function definition 1: </strong>let&#39;s define a function</span><em> <span style="color:#2980b9"><strong>allprimes</strong>&nbsp;</span></em><span style="color:#000000">with the syntax below;</span><span style="color:#000000">​​​​​</span>
	<ul>
		<li>
		<div style="background:#eeeeee; border:1px solid #cccccc; padding:5px 10px"><code>01: def allprimes(number)</code></div>
		</li>
		<li>
		<p>The def syntax is used to define the function that takes in the local variable number which will be used in the function to generate the prime numbers</p>
		</li>
	</ul>
	</li>
	<li>
	<p><strong>Odd numbers:</strong> Remember all prime numbers are odd numbers except 2. So, therefore&nbsp;this will be used to bring up the odd numbers while making use of a for loop</p>

	<ul>
		<li>
		<div style="background:#eeeeee; border:1px solid #cccccc; padding:5px 10px"><span style="font-family:monospace">05: oddnum = [2] # create a list variable with 2 already in it</span></div>
		</li>
		<li>
		<p>the next block of code will be a for loop that runs through all the numbers from 2 to the number variable given when the function is called. Recall that an odd number cannot be divided by 2 without a remainder. Hence, this will be used to filter out the even number using the modulo&nbsp;operator (%) in&nbsp;python which brings the remainder of a division. example <code><span class="marker">3 mod 2 is equivalent to 3%2 which gives a remainder of 1.</span></code>&nbsp;Thus, any number that gives a mod other than 0 is an odd number.</p>
		</li>
		<li>
		<div style="background:#eeeeee; border:1px solid #cccccc; padding:5px 10px">
		<p><code>06: for num in range(2,number+1):</code></p>

		<p><code>07:&nbsp; &nbsp; &nbsp;if num%2 != 0:</code></p>

		<p><code>08:&nbsp; &nbsp; &nbsp; &nbsp; oddnum.append(num)</code></p>
		</div>
		</li>
		<li>The code above uses an inbuilt python function to generate a series of number from 2 to the number pass in the function + 1, the reason for +1 is that the range function only generates from the first number and does include the last number variable. Example, <span class="marker"><code>range(2, 5) while generate 2, 3, 4</code></span> but if i want to include the last number it should be written like this <span class="marker">range(2,5+1) which will generate 2, 3, 4, 5</span>. Thus, it includes the last number. The for loop <span class="marker">&quot;<code>for num in range(2,number+1):&quot;</code>&nbsp;</span>collects the number generated in the range function and assigns it to a variable num. the loop is done until the last number on the list is run.</li>
		<li>After assigning the number generated to num an if statement is used to filter out the even number&nbsp;<code>if num%2 != 0:</code>&nbsp;it only runs the code after the if statement only when the condition is satisfied, for example, if the assign generated number is 3, therefore 3%2 is not (!=) 0, hence the next code will run. If not it does nothing until the time the for loop expression assign a number to variable num that satisfies the condition. When the condition is satisfied,&nbsp;<code>oddnum.append(num)&nbsp;</code>adds the number to list object created before. It keeps adding the&nbsp;numbers to the loop until the for loop stops running. Example if number=10, the for loop will run for 2 which doesn&#39;t satisfy the if condition, the next is 3 which satisfies the condition and it is added to the list object oddnum, thus, the list will grow from [2] to [2,3,5,7,9] and for loop stops because it has reached the end of the range 10.</li>
		<li>
		<div style="background:#eeeeee; border:1px solid #cccccc; padding:5px 10px"><code>10:&nbsp; &nbsp; size = len(oddnum)-1 # lenght of the list oddnum-1</code></div>
		</li>
		<li>
		<p>Line 10 is used to discover the length&nbsp;of numbers in the oddnum list i.e. iTs provide the number of items in the list and subtract 1 from it to assign it to a variable <em>size</em>. This would be used later to form a list of prime numbers.</p>
		</li>
		<li>
		<p>The motive of the rest of the code after 10 is to bring out all the primes numbers in the range. consider this case/scenerio, if the odd number list is [2,3,5,7,9] and any number is picked to be divided by the other number if the number picked is a prime number it wont divisible by any number on the list except itself. Since all numbers are divisible by themselves we dont need to include the division of same. So, in the list above we have a lenght of 5 because there are 5 items in it but we only need to divide a number 4 times. Thus, 1 has to be subtracted from the original lenght of 5. Hence the variable <span class="marker"><code>size=5-1=4</code></span>.</p>
		</li>
		<li>
		<div style="background:#eeeeee; border:1px solid #cccccc; padding:5px 10px">
		<p><code>12:&nbsp; &nbsp; for num in oddnum:</code></p>

		<p><code>13:&nbsp; &nbsp; &nbsp; &nbsp; templist = []</code></p>

		<p><code>14:&nbsp; &nbsp; &nbsp; &nbsp; for div in oddnum:</code></p>

		<p><code>15:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if num != div and num%div != 0:</code></p>

		<p><code>16:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;templist.append(num)&nbsp;# appends that number to the list</code></p>

		<p><code>17:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;if len(templist) == size:&nbsp;</code></p>

		<p><code>18:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; yield templist[0] </code></p>
		</div>
		</li>
		<li>
		<p>line 12, is a for loop that runs through all the oddnum list object and assigns a variable num to it, it first creates an empty list in line 13 , line 14 is a nested for loop that runs through oddnum again and assigns a variable div to it. line 15 is an if statement that filters the prime numbers from the ordinary odd numbers. If the condition of the num variable satisfied the number is appended to the empty list&nbsp;templist. remember that if the num variable is a prime number it wont be divisible by any on other number in the list item. for example, if 9 is pick from [2,3,5,7,9] and we register how many times it is not divided without remainder we will have;</p>
		</li>
		<li>
		<div style="background:#eeeeee; border:1px solid #cccccc; padding:5px 10px">
		<p>9%2 = give remainder = 1 =&gt; 1</p>

		<p>9%3&nbsp;= give remainder = 0</p>

		<p>9%5&nbsp;= give remainder = 4 =&gt; 2</p>

		<p>9%7&nbsp;= give remainder = 2 =&gt; 3</p>

		<p>you can see it wont be divided just 3 times, meaning that 9 is not a prime number, take note if a number is divided by a greater number it is still not divisible by it example lets pick 5 and test.</p>

		<p>5%2 = give remainder = 1 =&gt; 1</p>

		<p>5%3&nbsp;= give remainder = 2 =&gt; 2</p>

		<p>5%7&nbsp;= give remainder = 5 =&gt; 3</p>

		<p>5%7&nbsp;= give remainder = 5 =&gt; 4</p>

		<p>&#39;5&#39; is not divided 4 times therefore its a prime. this method of analysis what is done in lines 12-18</p>
		</div>
		</li>
		<li>
		<p>The for loop in line 12 picks the first number as a num, the for loop in line 14 alternates the other number as dive, thus for the first for loop num is equal for different values of div, the if condition on line 15 runs only when num is not equal to div and if num mod div is not equal to zero, thus signifying its a prime number. num is the appended to templist as many times as it wasnt divided by other numbers on the list. The if statement on line 17 checks if the number of times the number wasnt divided is equal to the right number, if the number satisfies the condition it is then recorded or generated using the yield syntax on line 18. Therefore the function allprimes() will generate prime numbers only.</p>
		</li>
	</ul>
	</li>
	<li>
	<div style="background:#eeeeee; border:1px solid #cccccc; padding:5px 10px">
	<p><code>20: def primfact(number):</code></p>

	<p><code>21:&nbsp; &nbsp; &nbsp; &nbsp;&quot;&quot;&quot;</code></p>

	<p><code>22:&nbsp; &nbsp; &nbsp; &nbsp;#----example-----#</code></p>

	<p><code>23:&nbsp; &nbsp; &nbsp; &nbsp;print(primfact(55))</code></p>

	<p><code>24:</code></p>

	<p><code>25:&nbsp; &nbsp; &nbsp; &nbsp;#----outputs-----#</code></p>

	<p><code>26:&nbsp; &nbsp; &nbsp; &nbsp;{5: 1, 11: 1} # equivalent to 5^1*11^1</code></p>

	<p><code>27:&nbsp; &nbsp; &nbsp; &nbsp;&quot;&quot;&quot;</code></p>

	<p><code>28:&nbsp; &nbsp; &nbsp; &nbsp; from collections import Counter</code></p>

	<p><code>29:&nbsp; &nbsp; &nbsp; &nbsp; primefactlist =[]</code></p>

	<p><code>30:&nbsp; &nbsp; &nbsp; &nbsp; check = 0</code></p>

	<p><code>31:&nbsp; &nbsp; &nbsp; &nbsp; g = allprimes(number)</code></p>

	<p><code>32:</code></p>

	<p><code>33:&nbsp; &nbsp; &nbsp; &nbsp; while number != 1:</code></p>

	<p><code>34:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if check == 0:</code></p>

	<p><code>35:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; divider = next(g)</code></p>

	<p><code>36:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; check = 1</code></p>

	<p><code>37:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if number%divider != 0:</code></p>

	<p><code>38:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; check = 0</code></p>

	<p><code>39:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; continue</code></p>

	<p><code>40:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; number /= divider</code></p>

	<p><code>41:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; primefactlist.append(divider)</code></p>

	<p><code>42:</code></p>

	<p><code>43:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;countprime = Counter(primefactlist)</code></p>

	<p><code>44:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;indexnot = dict(countprime)</code></p>

	<p><code>45:</code></p>

	<p><code>46:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;return indexnot # returns a dictionary in which the keys are the prime numbers and the values are the power of the index notation</code></p>
	</div>
	</li>
	<li>
	<p><strong>Function definition 2:&nbsp;</strong>next we define a function&nbsp;<em><strong><span style="color:#2980b9">primfact</span></strong></em></p>

	<ul>
		<li>
		<p>&nbsp;</p>
		</li>
	</ul>
	</li>
</ul>
